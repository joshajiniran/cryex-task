import logging
import random
from enum import IntEnum

import faker
from locust import SequentialTaskSet, TaskSet, task

from protobufs import vacancy_service_pb2, vacancy_service_pb2_grpc

from .auth import get_user_from_token

logger = logging.getLogger(__name__)

fake = faker.Faker()

class UserVacancyTaskSet(SequentialTaskSet):
    vacancy_id: str = ""

    @task
    def create_vacancy(self):
        vacancy_request = vacancy_service_pb2.rpc__create__vacancy__pb2.CreateVacancyRequest(Title=fake.job(), Description=fake.sentence(nb_words=50), Division=fake.random_int(min=0, max=3), Country=fake.country())
        response = self.client.CreateVacancy(vacancy_request)
        self.vacancy_id = response.vacancy.Id
        logger.info(f"Created vacancy {self.vacancy_id}")

    @task
    def update_vacancy(self):
        vacancy_update_request = vacancy_service_pb2.rpc__update__vacancy__pb2.UpdateVacancyRequest(Id=self.vacancy_id, Description=fake.sentence(nb_words=50), Division=fake.random_int(min=0, max=3))
        response = self.client.UpdateVacancy(vacancy_update_request)
        logger.info(f"Updated vacancy {response.vacancy}")

    @task
    def fetch_vacancy(self):
        response = self.client.GetVacancy(vacancy_service_pb2.VacancyRequest(Id=self.vacancy_id))
        logger.info(f"Fetched vacancy {response.vacancy}")

    @task
    def delete_vacancy(self):
        self.client.DeleteVacancy(vacancy_service_pb2.VacancyRequest(Id=self.vacancy_id))
        logger.info(f"Deleted vacancy {self.vacancy_id}")

    @task
    def stop(self):
        self.interrupt()