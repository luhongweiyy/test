# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: conscript.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import building_pb2
import resource_pb2
import hero_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='conscript.proto',
  package='SanProto',
  serialized_pb=_b('\n\x0f\x63onscript.proto\x12\x08SanProto\x1a\x0e\x62uilding.proto\x1a\x0eresource.proto\x1a\nhero.proto\"\xe4\x01\n\rConscriptInfo\x12\x19\n\x11\x62uilding_basic_id\x18\x01 \x02(\x05\x12\x15\n\rcity_basic_id\x18\x02 \x02(\x05\x12\x16\n\x0elocation_index\x18\x03 \x02(\x05\x12\x1b\n\x13\x63urrent_soldier_num\x18\x04 \x02(\x05\x12\x18\n\x10lock_soldier_num\x18\x05 \x02(\x05\x12\x15\n\rconscript_num\x18\x06 \x02(\x05\x12\x1c\n\x14total_conscript_time\x18\x07 \x01(\x05\x12\x1d\n\x15\x63onscript_passed_time\x18\x08 \x01(\x05\"\xc9\x01\n\x11StartConscriptReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12*\n\tconscript\x18\x02 \x02(\x0b\x32\x17.SanProto.ConscriptInfo\x12(\n\x08\x62uilding\x18\x03 \x01(\x0b\x32\x16.SanProto.BuildingInfo\x12\"\n\x06heroes\x18\x04 \x03(\x0b\x32\x12.SanProto.HeroInfo\x12)\n\tbuildings\x18\x05 \x03(\x0b\x32\x16.SanProto.BuildingInfo\"M\n\x11StartConscriptRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12(\n\x08resource\x18\x02 \x01(\x0b\x32\x16.SanProto.ResourceInfo\"\xae\x01\n\x0f\x45ndConscriptReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12*\n\tconscript\x18\x02 \x02(\x0b\x32\x17.SanProto.ConscriptInfo\x12(\n\x08\x62uilding\x18\x03 \x02(\x0b\x32\x16.SanProto.BuildingInfo\x12\"\n\x06heroes\x18\x04 \x03(\x0b\x32\x12.SanProto.HeroInfo\x12\x10\n\x08use_gold\x18\x05 \x01(\x08\"\x81\x02\n\x0f\x45ndConscriptRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12(\n\x08resource\x18\x02 \x01(\x0b\x32\x16.SanProto.ResourceInfo\x12*\n\x03ret\x18\x03 \x01(\x0e\x32\x1d.SanProto.EndConscriptRes.RET\x12*\n\tconscript\x18\x04 \x01(\x0b\x32\x17.SanProto.ConscriptInfo\x12(\n\x08\x62uilding\x18\x05 \x01(\x0b\x32\x16.SanProto.BuildingInfo\"2\n\x03RET\x12\x06\n\x02OK\x10\x00\x12\x14\n\x10NOT_CONSCRIPTING\x10\x01\x12\r\n\tCANNT_END\x10\x02')
  ,
  dependencies=[building_pb2.DESCRIPTOR,resource_pb2.DESCRIPTOR,hero_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ENDCONSCRIPTRES_RET = _descriptor.EnumDescriptor(
  name='RET',
  full_name='SanProto.EndConscriptRes.RET',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_CONSCRIPTING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNT_END', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=972,
  serialized_end=1022,
)
_sym_db.RegisterEnumDescriptor(_ENDCONSCRIPTRES_RET)


_CONSCRIPTINFO = _descriptor.Descriptor(
  name='ConscriptInfo',
  full_name='SanProto.ConscriptInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='building_basic_id', full_name='SanProto.ConscriptInfo.building_basic_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city_basic_id', full_name='SanProto.ConscriptInfo.city_basic_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_index', full_name='SanProto.ConscriptInfo.location_index', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_soldier_num', full_name='SanProto.ConscriptInfo.current_soldier_num', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lock_soldier_num', full_name='SanProto.ConscriptInfo.lock_soldier_num', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conscript_num', full_name='SanProto.ConscriptInfo.conscript_num', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_conscript_time', full_name='SanProto.ConscriptInfo.total_conscript_time', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conscript_passed_time', full_name='SanProto.ConscriptInfo.conscript_passed_time', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=74,
  serialized_end=302,
)


_STARTCONSCRIPTREQ = _descriptor.Descriptor(
  name='StartConscriptReq',
  full_name='SanProto.StartConscriptReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.StartConscriptReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conscript', full_name='SanProto.StartConscriptReq.conscript', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building', full_name='SanProto.StartConscriptReq.building', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heroes', full_name='SanProto.StartConscriptReq.heroes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buildings', full_name='SanProto.StartConscriptReq.buildings', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=305,
  serialized_end=506,
)


_STARTCONSCRIPTRES = _descriptor.Descriptor(
  name='StartConscriptRes',
  full_name='SanProto.StartConscriptRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.StartConscriptRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.StartConscriptRes.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=508,
  serialized_end=585,
)


_ENDCONSCRIPTREQ = _descriptor.Descriptor(
  name='EndConscriptReq',
  full_name='SanProto.EndConscriptReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.EndConscriptReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conscript', full_name='SanProto.EndConscriptReq.conscript', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building', full_name='SanProto.EndConscriptReq.building', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heroes', full_name='SanProto.EndConscriptReq.heroes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_gold', full_name='SanProto.EndConscriptReq.use_gold', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=588,
  serialized_end=762,
)


_ENDCONSCRIPTRES = _descriptor.Descriptor(
  name='EndConscriptRes',
  full_name='SanProto.EndConscriptRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.EndConscriptRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.EndConscriptRes.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.EndConscriptRes.ret', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conscript', full_name='SanProto.EndConscriptRes.conscript', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building', full_name='SanProto.EndConscriptRes.building', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENDCONSCRIPTRES_RET,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=765,
  serialized_end=1022,
)

_STARTCONSCRIPTREQ.fields_by_name['conscript'].message_type = _CONSCRIPTINFO
_STARTCONSCRIPTREQ.fields_by_name['building'].message_type = building_pb2._BUILDINGINFO
_STARTCONSCRIPTREQ.fields_by_name['heroes'].message_type = hero_pb2._HEROINFO
_STARTCONSCRIPTREQ.fields_by_name['buildings'].message_type = building_pb2._BUILDINGINFO
_STARTCONSCRIPTRES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_ENDCONSCRIPTREQ.fields_by_name['conscript'].message_type = _CONSCRIPTINFO
_ENDCONSCRIPTREQ.fields_by_name['building'].message_type = building_pb2._BUILDINGINFO
_ENDCONSCRIPTREQ.fields_by_name['heroes'].message_type = hero_pb2._HEROINFO
_ENDCONSCRIPTRES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_ENDCONSCRIPTRES.fields_by_name['ret'].enum_type = _ENDCONSCRIPTRES_RET
_ENDCONSCRIPTRES.fields_by_name['conscript'].message_type = _CONSCRIPTINFO
_ENDCONSCRIPTRES.fields_by_name['building'].message_type = building_pb2._BUILDINGINFO
_ENDCONSCRIPTRES_RET.containing_type = _ENDCONSCRIPTRES
DESCRIPTOR.message_types_by_name['ConscriptInfo'] = _CONSCRIPTINFO
DESCRIPTOR.message_types_by_name['StartConscriptReq'] = _STARTCONSCRIPTREQ
DESCRIPTOR.message_types_by_name['StartConscriptRes'] = _STARTCONSCRIPTRES
DESCRIPTOR.message_types_by_name['EndConscriptReq'] = _ENDCONSCRIPTREQ
DESCRIPTOR.message_types_by_name['EndConscriptRes'] = _ENDCONSCRIPTRES

ConscriptInfo = _reflection.GeneratedProtocolMessageType('ConscriptInfo', (_message.Message,), dict(
  DESCRIPTOR = _CONSCRIPTINFO,
  __module__ = 'conscript_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ConscriptInfo)
  ))
_sym_db.RegisterMessage(ConscriptInfo)

StartConscriptReq = _reflection.GeneratedProtocolMessageType('StartConscriptReq', (_message.Message,), dict(
  DESCRIPTOR = _STARTCONSCRIPTREQ,
  __module__ = 'conscript_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.StartConscriptReq)
  ))
_sym_db.RegisterMessage(StartConscriptReq)

StartConscriptRes = _reflection.GeneratedProtocolMessageType('StartConscriptRes', (_message.Message,), dict(
  DESCRIPTOR = _STARTCONSCRIPTRES,
  __module__ = 'conscript_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.StartConscriptRes)
  ))
_sym_db.RegisterMessage(StartConscriptRes)

EndConscriptReq = _reflection.GeneratedProtocolMessageType('EndConscriptReq', (_message.Message,), dict(
  DESCRIPTOR = _ENDCONSCRIPTREQ,
  __module__ = 'conscript_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.EndConscriptReq)
  ))
_sym_db.RegisterMessage(EndConscriptReq)

EndConscriptRes = _reflection.GeneratedProtocolMessageType('EndConscriptRes', (_message.Message,), dict(
  DESCRIPTOR = _ENDCONSCRIPTRES,
  __module__ = 'conscript_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.EndConscriptRes)
  ))
_sym_db.RegisterMessage(EndConscriptRes)


# @@protoc_insertion_point(module_scope)
