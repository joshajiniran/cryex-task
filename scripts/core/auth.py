import grpc
import jwt

from protobufs import user_service_pb2, user_service_pb2_grpc

# helper functions related to authentication/authorization

def get_user_from_token(token: str) -> str|None:
    try:
        payload = jwt.decode(token, options={"verify_signature": False})
    except jwt.exceptions.DecodeError:
        return None

    with grpc.insecure_channel('138.197.190.181:7823') as channel:
        stub = user_service_pb2_grpc.UserServiceStub(channel)
        resp = stub.GetMe(user_service_pb2.GetMeRequest(Id=payload.get('sub')))
        return resp.user.name