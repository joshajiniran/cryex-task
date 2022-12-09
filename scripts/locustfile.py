import logging
import os
import time

import gevent
import grpc

# patch grpc so that it uses gevent instead of asyncio
import grpc.experimental.gevent as grpc_gevent
from core.user_credentials import *
from core.vacancy import UserVacancyTaskSet
from locust import User, constant, task
from locust.exception import LocustError
from locust.user.task import LOCUST_STATE_STOPPING

from protobufs import (
    auth_service_pb2,
    auth_service_pb2_grpc,
    vacancy_service_pb2,
    vacancy_service_pb2_grpc,
)

grpc_gevent.init_gevent()

logger = logging.getLogger(__name__)

SERVER_ADDRESS = os.environ.get("SERVER_ADDRESS", "138.197.190.181:7823")


class GrpcClient:
    def __init__(self, environment, stub):
        self.env = environment
        self._stub_class = stub.__class__
        self._stub = stub

    def __getattr__(self, name):
        func = self._stub_class.__getattribute__(self._stub, name)

        def wrapper(*args, **kwargs):
            request_meta = {
                "request_type": "grpc",
                "name": name,
                "start_time": time.time(),
                "response_length": 0,
                "exception": None,
                "context": None,
                "response": None,
            }
            start_perf_counter = time.perf_counter()
            try:
                request_meta["response"] = func(*args, **kwargs)
                # request_meta["response_length"] = len(request_meta["response"].message)
            except grpc.RpcError as e:
                request_meta["exception"] = e
            request_meta["response_time"] = (
                time.perf_counter() - start_perf_counter
            ) * 1000
            self.env.events.request.fire(**request_meta)
            return request_meta["response"]

        return wrapper


class GrpcUser(User):
    abstract = True

    stub_class = None

    def __init__(self, environment):
        super().__init__(environment)
        for attr_value, attr_name in (
            (self.host, "host"),
            (self.stub_class, "stub_class"),
        ):
            if attr_value is None:
                raise LocustError(f"You must specify the {attr_name}.")

        self._channel = grpc.insecure_channel(self.host)
        self._channel_closed = False
        stub = self.stub_class(self._channel)
        self.client = GrpcClient(environment, stub)


class SignedInGrpcUser(GrpcUser):
    tasks = [UserVacancyTaskSet]
    host = "138.197.190.181:7823"
    stub_class = vacancy_service_pb2_grpc.VacancyServiceStub
    token = ""
    wait_time = constant(30)

    def on_start(self):
        if len(USERS) > 0:
            self.email, self.password = USERS.pop()
            self.token = self.login(self.email, self.password)

    def login(self, email: str, pswd: str) -> str:
        client = GrpcClient(
            self.environment, auth_service_pb2_grpc.AuthServiceStub(self._channel)
        )
        if not self._channel_closed:
            response = client.SignInUser(
                auth_service_pb2.rpc__signin__user__pb2.SignInUserInput(
                    email=email, password=pswd
                )
            )
        return response.access_token


class SignedInGrpcUserAllVacancies(GrpcUser):
    host = "138.197.190.181:7823"
    stub_class = vacancy_service_pb2_grpc.VacancyServiceStub
    wait_time = constant(45)

    @task
    def fetch_all_vacancies(self):

        if not self._channel_closed:
            stream_response = self.client.GetVacancies(
                vacancy_service_pb2.GetVacanciesRequest(page=1, limit=10)
            )
            for resp in stream_response:
                logger.info(resp)
