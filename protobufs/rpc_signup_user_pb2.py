# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc_signup_user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import user_pb2 as user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x15rpc_signup_user.proto\x12\x02pb\x1a\nuser.proto"Y\n\x0fSignUpUserInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x17\n\x0fpasswordConfirm\x18\x04 \x01(\t",\n\x12SignUpUserResponse\x12\x16\n\x04user\x18\x01 \x01(\x0b\x32\x08.pb.UserB\x14Z\x12\x63yrex/vacancies/pbb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "rpc_signup_user_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z\022cyrex/vacancies/pb"
    _SIGNUPUSERINPUT._serialized_start = 41
    _SIGNUPUSERINPUT._serialized_end = 130
    _SIGNUPUSERRESPONSE._serialized_start = 132
    _SIGNUPUSERRESPONSE._serialized_end = 176
# @@protoc_insertion_point(module_scope)
