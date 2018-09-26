# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: building.proto

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
import resource_pb2
import monarch_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='building.proto',
  package='SanProto',
  serialized_pb=_b('\n\x0e\x62uilding.proto\x12\x08SanProto\x1a\nhero.proto\x1a\x0eresource.proto\x1a\rmonarch.proto\"\xfa\x01\n\x0c\x42uildingInfo\x12\x10\n\x08\x62\x61sic_id\x18\x01 \x02(\x05\x12\x15\n\rcity_basic_id\x18\x02 \x02(\x05\x12\x16\n\x0elocation_index\x18\x03 \x02(\x05\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x15\n\rgarrision_num\x18\x05 \x01(\x05\x12\x16\n\x0ehero_basic_ids\x18\x06 \x03(\x05\x12\x14\n\x0cis_upgrading\x18\x07 \x01(\x08\x12\x1a\n\x12upgrade_start_time\x18\x08 \x01(\x05\x12\x1c\n\x14upgrade_consume_time\x18\t \x01(\x05\x12\x1b\n\x13upgrade_passed_time\x18\n \x01(\x05\"\xd8\x01\n\x12UpgradeBuildingReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12(\n\x08\x62uilding\x18\x02 \x02(\x0b\x32\x16.SanProto.BuildingInfo\x12\"\n\x06heroes\x18\x03 \x03(\x0b\x32\x12.SanProto.HeroInfo\x12)\n\tbuildings\x18\x04 \x03(\x0b\x32\x16.SanProto.BuildingInfo\x12&\n\x07monarch\x18\x05 \x01(\x0b\x32\x15.SanProto.MonarchInfo\x12\x10\n\x08use_gold\x18\x06 \x01(\x08\"\xdb\x01\n\x12UpgradeBuildingRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12(\n\x08resource\x18\x02 \x01(\x0b\x32\x16.SanProto.ResourceInfo\x12-\n\x03ret\x18\x03 \x01(\x0e\x32 .SanProto.UpgradeBuildingRes.RET\x12(\n\x08\x62uilding\x18\x04 \x01(\x0b\x32\x16.SanProto.BuildingInfo\"2\n\x03RET\x12\x06\n\x02OK\x10\x00\x12\x11\n\rNOT_UPGRADING\x10\x01\x12\x10\n\x0c\x43\x41NNT_FINISH\x10\x02\"\xa1\x01\n\x15UpdateGarrisonHeroReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12(\n\x08\x62uilding\x18\x02 \x02(\x0b\x32\x16.SanProto.BuildingInfo\x12\"\n\x06heroes\x18\x03 \x03(\x0b\x32\x12.SanProto.HeroInfo\x12)\n\tbuildings\x18\x04 \x03(\x0b\x32\x16.SanProto.BuildingInfo\"Q\n\x15UpdateGarrisonHeroRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12(\n\x08resource\x18\x02 \x01(\x0b\x32\x16.SanProto.ResourceInfo')
  ,
  dependencies=[hero_pb2.DESCRIPTOR,resource_pb2.DESCRIPTOR,monarch_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_UPGRADEBUILDINGRES_RET = _descriptor.EnumDescriptor(
  name='RET',
  full_name='SanProto.UpgradeBuildingRes.RET',
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
  serialized_start=713,
  serialized_end=763,
)
_sym_db.RegisterEnumDescriptor(_UPGRADEBUILDINGRES_RET)


_BUILDINGINFO = _descriptor.Descriptor(
  name='BuildingInfo',
  full_name='SanProto.BuildingInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic_id', full_name='SanProto.BuildingInfo.basic_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city_basic_id', full_name='SanProto.BuildingInfo.city_basic_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_index', full_name='SanProto.BuildingInfo.location_index', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='SanProto.BuildingInfo.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='garrision_num', full_name='SanProto.BuildingInfo.garrision_num', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_basic_ids', full_name='SanProto.BuildingInfo.hero_basic_ids', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_upgrading', full_name='SanProto.BuildingInfo.is_upgrading', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upgrade_start_time', full_name='SanProto.BuildingInfo.upgrade_start_time', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upgrade_consume_time', full_name='SanProto.BuildingInfo.upgrade_consume_time', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upgrade_passed_time', full_name='SanProto.BuildingInfo.upgrade_passed_time', index=9,
      number=10, type=5, cpp_type=1, label=1,
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
  serialized_start=72,
  serialized_end=322,
)


_UPGRADEBUILDINGREQ = _descriptor.Descriptor(
  name='UpgradeBuildingReq',
  full_name='SanProto.UpgradeBuildingReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.UpgradeBuildingReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building', full_name='SanProto.UpgradeBuildingReq.building', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heroes', full_name='SanProto.UpgradeBuildingReq.heroes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buildings', full_name='SanProto.UpgradeBuildingReq.buildings', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='monarch', full_name='SanProto.UpgradeBuildingReq.monarch', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_gold', full_name='SanProto.UpgradeBuildingReq.use_gold', index=5,
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
  serialized_start=325,
  serialized_end=541,
)


_UPGRADEBUILDINGRES = _descriptor.Descriptor(
  name='UpgradeBuildingRes',
  full_name='SanProto.UpgradeBuildingRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.UpgradeBuildingRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.UpgradeBuildingRes.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.UpgradeBuildingRes.ret', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building', full_name='SanProto.UpgradeBuildingRes.building', index=3,
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
    _UPGRADEBUILDINGRES_RET,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=763,
)


_UPDATEGARRISONHEROREQ = _descriptor.Descriptor(
  name='UpdateGarrisonHeroReq',
  full_name='SanProto.UpdateGarrisonHeroReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.UpdateGarrisonHeroReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='building', full_name='SanProto.UpdateGarrisonHeroReq.building', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heroes', full_name='SanProto.UpdateGarrisonHeroReq.heroes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buildings', full_name='SanProto.UpdateGarrisonHeroReq.buildings', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=766,
  serialized_end=927,
)


_UPDATEGARRISONHERORES = _descriptor.Descriptor(
  name='UpdateGarrisonHeroRes',
  full_name='SanProto.UpdateGarrisonHeroRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.UpdateGarrisonHeroRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.UpdateGarrisonHeroRes.resource', index=1,
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
  serialized_start=929,
  serialized_end=1010,
)

_UPGRADEBUILDINGREQ.fields_by_name['building'].message_type = _BUILDINGINFO
_UPGRADEBUILDINGREQ.fields_by_name['heroes'].message_type = hero_pb2._HEROINFO
_UPGRADEBUILDINGREQ.fields_by_name['buildings'].message_type = _BUILDINGINFO
_UPGRADEBUILDINGREQ.fields_by_name['monarch'].message_type = monarch_pb2._MONARCHINFO
_UPGRADEBUILDINGRES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_UPGRADEBUILDINGRES.fields_by_name['ret'].enum_type = _UPGRADEBUILDINGRES_RET
_UPGRADEBUILDINGRES.fields_by_name['building'].message_type = _BUILDINGINFO
_UPGRADEBUILDINGRES_RET.containing_type = _UPGRADEBUILDINGRES
_UPDATEGARRISONHEROREQ.fields_by_name['building'].message_type = _BUILDINGINFO
_UPDATEGARRISONHEROREQ.fields_by_name['heroes'].message_type = hero_pb2._HEROINFO
_UPDATEGARRISONHEROREQ.fields_by_name['buildings'].message_type = _BUILDINGINFO
_UPDATEGARRISONHERORES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
DESCRIPTOR.message_types_by_name['BuildingInfo'] = _BUILDINGINFO
DESCRIPTOR.message_types_by_name['UpgradeBuildingReq'] = _UPGRADEBUILDINGREQ
DESCRIPTOR.message_types_by_name['UpgradeBuildingRes'] = _UPGRADEBUILDINGRES
DESCRIPTOR.message_types_by_name['UpdateGarrisonHeroReq'] = _UPDATEGARRISONHEROREQ
DESCRIPTOR.message_types_by_name['UpdateGarrisonHeroRes'] = _UPDATEGARRISONHERORES

BuildingInfo = _reflection.GeneratedProtocolMessageType('BuildingInfo', (_message.Message,), dict(
  DESCRIPTOR = _BUILDINGINFO,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.BuildingInfo)
  ))
_sym_db.RegisterMessage(BuildingInfo)

UpgradeBuildingReq = _reflection.GeneratedProtocolMessageType('UpgradeBuildingReq', (_message.Message,), dict(
  DESCRIPTOR = _UPGRADEBUILDINGREQ,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpgradeBuildingReq)
  ))
_sym_db.RegisterMessage(UpgradeBuildingReq)

UpgradeBuildingRes = _reflection.GeneratedProtocolMessageType('UpgradeBuildingRes', (_message.Message,), dict(
  DESCRIPTOR = _UPGRADEBUILDINGRES,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpgradeBuildingRes)
  ))
_sym_db.RegisterMessage(UpgradeBuildingRes)

UpdateGarrisonHeroReq = _reflection.GeneratedProtocolMessageType('UpdateGarrisonHeroReq', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEGARRISONHEROREQ,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpdateGarrisonHeroReq)
  ))
_sym_db.RegisterMessage(UpdateGarrisonHeroReq)

UpdateGarrisonHeroRes = _reflection.GeneratedProtocolMessageType('UpdateGarrisonHeroRes', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEGARRISONHERORES,
  __module__ = 'building_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpdateGarrisonHeroRes)
  ))
_sym_db.RegisterMessage(UpdateGarrisonHeroRes)


# @@protoc_insertion_point(module_scope)
