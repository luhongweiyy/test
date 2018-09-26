# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: technology.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import hero_pb2
import building_pb2
import resource_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='technology.proto',
  package='SanProto',
  serialized_pb=_b('\n\x10technology.proto\x12\x08SanProto\x1a\nhero.proto\x1a\x0e\x62uilding.proto\x1a\x0eresource.proto\"\xcc\x02\n\x0eTechnologyInfo\x12\x10\n\x08\x62\x61sic_id\x18\x01 \x02(\x05\x12/\n\x04type\x18\x02 \x02(\x0e\x32!.SanProto.TechnologyInfo.TechType\x12\x14\n\x0cis_upgrading\x18\x03 \x01(\x08\x12\x1a\n\x12upgrade_start_time\x18\x04 \x01(\x05\x12\x1c\n\x14upgrade_consume_time\x18\x05 \x01(\x05\x12\x19\n\x11\x62uilding_basic_id\x18\x06 \x01(\x05\x12\x15\n\rcity_basic_id\x18\x07 \x01(\x05\x12\x16\n\x0elocation_index\x18\x08 \x01(\x05\x12\x1b\n\x13upgrade_passed_time\x18\t \x01(\x05\"@\n\x08TechType\x12\x0f\n\x0b\x42\x41TTLE_TECH\x10\x00\x12\x11\n\rINTERIOR_TECH\x10\x01\x12\x10\n\x0cSOLDIER_TECH\x10\x02\"\xd4\x01\n\x0eUpgradeTechReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12&\n\x04tech\x18\x02 \x02(\x0b\x32\x18.SanProto.TechnologyInfo\x12(\n\x08\x62uilding\x18\x03 \x02(\x0b\x32\x16.SanProto.BuildingInfo\x12\"\n\x06heroes\x18\x04 \x03(\x0b\x32\x12.SanProto.HeroInfo\x12)\n\tbuildings\x18\x05 \x03(\x0b\x32\x16.SanProto.BuildingInfo\x12\x10\n\x08use_gold\x18\x06 \x01(\x08\"\xd1\x01\n\x0eUpgradeTechRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12(\n\x08resource\x18\x02 \x01(\x0b\x32\x16.SanProto.ResourceInfo\x12)\n\x03ret\x18\x03 \x01(\x0e\x32\x1c.SanProto.UpgradeTechRes.RET\x12&\n\x04tech\x18\x04 \x01(\x0b\x32\x18.SanProto.TechnologyInfo\"2\n\x03RET\x12\x06\n\x02OK\x10\x00\x12\x11\n\rNOT_UPGRADING\x10\x01\x12\x10\n\x0c\x43\x41NNT_FINISH\x10\x02')
  ,
  dependencies=[hero_pb2.DESCRIPTOR,building_pb2.DESCRIPTOR,resource_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TECHNOLOGYINFO_TECHTYPE = _descriptor.EnumDescriptor(
  name='TechType',
  full_name='SanProto.TechnologyInfo.TechType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BATTLE_TECH', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERIOR_TECH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOLDIER_TECH', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=343,
  serialized_end=407,
)
_sym_db.RegisterEnumDescriptor(_TECHNOLOGYINFO_TECHTYPE)

_UPGRADETECHRES_RET = _descriptor.EnumDescriptor(
  name='RET',
  full_name='SanProto.UpgradeTechRes.RET',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_UPGRADING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNT_FINISH', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=784,
  serialized_end=834,
)
_sym_db.RegisterEnumDescriptor(_UPGRADETECHRES_RET)


_TECHNOLOGYINFO = _descriptor.Descriptor(
  name='TechnologyInfo',
  full_name='SanProto.TechnologyInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic_id', full_name='SanProto.TechnologyInfo.basic_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='SanProto.TechnologyInfo.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_upgrading', full_name='SanProto.TechnologyInfo.is_upgrading', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upgrade_start_time', full_name='SanProto.TechnologyInfo.upgrade_start_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upgrade_consume_time', full_name='SanProto.TechnologyInfo.upgrade_consume_time', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building_basic_id', full_name='SanProto.TechnologyInfo.building_basic_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city_basic_id', full_name='SanProto.TechnologyInfo.city_basic_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_index', full_name='SanProto.TechnologyInfo.location_index', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upgrade_passed_time', full_name='SanProto.TechnologyInfo.upgrade_passed_time', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TECHNOLOGYINFO_TECHTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=407,
)


_UPGRADETECHREQ = _descriptor.Descriptor(
  name='UpgradeTechReq',
  full_name='SanProto.UpgradeTechReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.UpgradeTechReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tech', full_name='SanProto.UpgradeTechReq.tech', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building', full_name='SanProto.UpgradeTechReq.building', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heroes', full_name='SanProto.UpgradeTechReq.heroes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buildings', full_name='SanProto.UpgradeTechReq.buildings', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_gold', full_name='SanProto.UpgradeTechReq.use_gold', index=5,
      number=6, type=8, cpp_type=7, label=1,
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
  serialized_start=410,
  serialized_end=622,
)


_UPGRADETECHRES = _descriptor.Descriptor(
  name='UpgradeTechRes',
  full_name='SanProto.UpgradeTechRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.UpgradeTechRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.UpgradeTechRes.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.UpgradeTechRes.ret', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tech', full_name='SanProto.UpgradeTechRes.tech', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPGRADETECHRES_RET,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=625,
  serialized_end=834,
)

_TECHNOLOGYINFO.fields_by_name['type'].enum_type = _TECHNOLOGYINFO_TECHTYPE
_TECHNOLOGYINFO_TECHTYPE.containing_type = _TECHNOLOGYINFO
_UPGRADETECHREQ.fields_by_name['tech'].message_type = _TECHNOLOGYINFO
_UPGRADETECHREQ.fields_by_name['building'].message_type = building_pb2._BUILDINGINFO
_UPGRADETECHREQ.fields_by_name['heroes'].message_type = hero_pb2._HEROINFO
_UPGRADETECHREQ.fields_by_name['buildings'].message_type = building_pb2._BUILDINGINFO
_UPGRADETECHRES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_UPGRADETECHRES.fields_by_name['ret'].enum_type = _UPGRADETECHRES_RET
_UPGRADETECHRES.fields_by_name['tech'].message_type = _TECHNOLOGYINFO
_UPGRADETECHRES_RET.containing_type = _UPGRADETECHRES
DESCRIPTOR.message_types_by_name['TechnologyInfo'] = _TECHNOLOGYINFO
DESCRIPTOR.message_types_by_name['UpgradeTechReq'] = _UPGRADETECHREQ
DESCRIPTOR.message_types_by_name['UpgradeTechRes'] = _UPGRADETECHRES

TechnologyInfo = _reflection.GeneratedProtocolMessageType('TechnologyInfo', (_message.Message,), dict(
  DESCRIPTOR = _TECHNOLOGYINFO,
  __module__ = 'technology_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.TechnologyInfo)
  ))
_sym_db.RegisterMessage(TechnologyInfo)

UpgradeTechReq = _reflection.GeneratedProtocolMessageType('UpgradeTechReq', (_message.Message,), dict(
  DESCRIPTOR = _UPGRADETECHREQ,
  __module__ = 'technology_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpgradeTechReq)
  ))
_sym_db.RegisterMessage(UpgradeTechReq)

UpgradeTechRes = _reflection.GeneratedProtocolMessageType('UpgradeTechRes', (_message.Message,), dict(
  DESCRIPTOR = _UPGRADETECHRES,
  __module__ = 'technology_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpgradeTechRes)
  ))
_sym_db.RegisterMessage(UpgradeTechRes)


# @@protoc_insertion_point(module_scope)
