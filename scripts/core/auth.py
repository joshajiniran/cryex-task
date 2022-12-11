import sys

import grpc
import jwt
from core import logger, SERVER_ADDRESS
from grpc import StatusCode

from protobufs import user_service_pb2, user_service_pb2_grpc


def get_user_from_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, options={"verify_signature": False})
    except jwt.exceptions.DecodeError:
        logger.info("Error decoding token: could not get user")
        return None

    with grpc.insecure_channel(SERVER_ADDRESS) as channel:
        stub = user_service_pb2_grpc.UserServiceStub(channel)
        resp = stub.GetMe(user_service_pb2.GetMeRequest(Id=payload.get("sub")))
        if resp.status != StatusCode.UNAVAILABLE:
            return resp.user
        logger.info("Failed to connect to server")
        sys.exit(0)
