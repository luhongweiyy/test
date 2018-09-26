# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: city.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='city.proto',
  package='SanProto',
  serialized_pb=_b('\n\ncity.proto\x12\x08SanProto\"*\n\x08\x43ityInfo\x12\x10\n\x08\x62\x61sic_id\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\x0c\"B\n\rUpdateCityReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12 \n\x04\x63ity\x18\x02 \x02(\x0b\x32\x12.SanProto.CityInfo\"\x1f\n\rUpdateCityRes\x12\x0e\n\x06status\x18\x01 \x02(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CITYINFO = _descriptor.Descriptor(
  name='CityInfo',
  full_name='SanProto.CityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic_id', full_name='SanProto.CityInfo.basic_id', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='SanProto.CityInfo.name', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=66,
)


_UPDATECITYREQ = _descriptor.Descriptor(
  name='UpdateCityReq',
  full_name='SanProto.UpdateCityReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.UpdateCityReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city', full_name='SanProto.UpdateCityReq.city', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=134,
)


_UPDATECITYRES = _descriptor.Descriptor(
  name='UpdateCityRes',
  full_name='SanProto.UpdateCityRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.UpdateCityRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=167,
)

_UPDATECITYREQ.fields_by_name['city'].message_type = _CITYINFO
DESCRIPTOR.message_types_by_name['CityInfo'] = _CITYINFO
DESCRIPTOR.message_types_by_name['UpdateCityReq'] = _UPDATECITYREQ
DESCRIPTOR.message_types_by_name['UpdateCityRes'] = _UPDATECITYRES

CityInfo = _reflection.GeneratedProtocolMessageType('CityInfo', (_message.Message,), dict(
  DESCRIPTOR = _CITYINFO,
  __module__ = 'city_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.CityInfo)
  ))
_sym_db.RegisterMessage(CityInfo)

UpdateCityReq = _reflection.GeneratedProtocolMessageType('UpdateCityReq', (_message.Message,), dict(
  DESCRIPTOR = _UPDATECITYREQ,
  __module__ = 'city_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpdateCityReq)
  ))
_sym_db.RegisterMessage(UpdateCityReq)

UpdateCityRes = _reflection.GeneratedProtocolMessageType('UpdateCityRes', (_message.Message,), dict(
  DESCRIPTOR = _UPDATECITYRES,
  __module__ = 'city_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpdateCityRes)
  ))
_sym_db.RegisterMessage(UpdateCityRes)


# @@protoc_insertion_point(module_scope)