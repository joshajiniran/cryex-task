# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc_update_vacancy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import vacancy_pb2 as vacancy__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18rpc_update_vacancy.proto\x12\x02pb\x1a\rvacancy.proto\"\xe4\x01\n\x14UpdateVacancyRequest\x12\n\n\x02Id\x18\x01 \x01(\t\x12\x12\n\x05Title\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x44\x65scription\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05Views\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12+\n\x08\x44ivision\x18\x05 \x01(\x0e\x32\x14.pb.Vacancy.DIVISIONH\x03\x88\x01\x01\x12\x14\n\x07\x43ountry\x18\x06 \x01(\tH\x04\x88\x01\x01\x42\x08\n\x06_TitleB\x0e\n\x0c_DescriptionB\x08\n\x06_ViewsB\x0b\n\t_DivisionB\n\n\x08_CountryB\x14Z\x12\x63yrex/vacancies/pbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rpc_update_vacancy_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\022cyrex/vacancies/pb'
  _UPDATEVACANCYREQUEST._serialized_start=48
  _UPDATEVACANCYREQUEST._serialized_end=276
# @@protoc_insertion_point(module_scope)
