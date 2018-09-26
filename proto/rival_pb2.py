# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rival.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import resource_pb2
import item_pb2
import team_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rival.proto',
  package='SanProto',
  serialized_pb=_b('\n\x0brival.proto\x12\x08SanProto\x1a\x0eresource.proto\x1a\nitem.proto\x1a\nteam.proto\"\xd0\x04\n\tRivalInfo\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12&\n\x04type\x18\x02 \x02(\x0e\x32\x18.SanProto.RivalInfo.TYPE\x12\x10\n\x08rival_id\x18\x03 \x01(\x05\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x0c\n\x04name\x18\x05 \x01(\x0c\x12\x0f\n\x07icon_id\x18\x06 \x01(\x05\x12\r\n\x05score\x18\x07 \x01(\x05\x12!\n\x05teams\x18\x08 \x03(\x0b\x32\x12.SanProto.TeamInfo\x12\x10\n\x08\x62uff_ids\x18\t \x03(\x05\x12\x17\n\x0f\x62\x61ttle_tech_ids\x18\n \x03(\x05\x12/\n\x0freward_resource\x18\x0b \x01(\x0b\x32\x16.SanProto.ResourceInfo\x12(\n\x0creward_items\x18\x0c \x03(\x0b\x32\x12.SanProto.ItemInfo\x12\x0f\n\x07\x63ountry\x18\r \x01(\x05\"\x80\x02\n\x04TYPE\x12\x10\n\x0cPVE_RESOURCE\x10\x01\x12\x0c\n\x08PVP_CITY\x10\x02\x12\x10\n\x0cPVP_RESOURCE\x10\x03\x12\x0e\n\nPVE_BANDIT\x10\x04\x12\r\n\tPVE_REBEL\x10\x05\x12\x0f\n\x0bPVE_DUNGEON\x10\x06\x12\r\n\tPVP_ARENA\x10\x07\x12\x12\n\x0ePVP_LEGENDCITY\x10\x08\x12\x11\n\rPVE_WORLDBOSS\x10\t\x12\r\n\tPVP_MELEE\x10\n\x12\x11\n\rPVE_UNIONBOSS\x10\x0b\x12\x16\n\x12PVE_EXPAND_DUNGEON\x10\x0c\x12\x0f\n\x0bPVP_PLUNDER\x10\r\x12\x15\n\x11PVP_PLUNDER_ENEMY\x10\x0e')
  ,
  dependencies=[resource_pb2.DESCRIPTOR,item_pb2.DESCRIPTOR,team_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_RIVALINFO_TYPE = _descriptor.EnumDescriptor(
  name='TYPE',
  full_name='SanProto.RivalInfo.TYPE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PVE_RESOURCE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVP_CITY', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVP_RESOURCE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVE_BANDIT', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVE_REBEL', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVE_DUNGEON', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVP_ARENA', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVP_LEGENDCITY', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVE_WORLDBOSS', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVP_MELEE', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVE_UNIONBOSS', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVE_EXPAND_DUNGEON', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVP_PLUNDER', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PVP_PLUNDER_ENEMY', index=13, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=402,
  serialized_end=658,
)
_sym_db.RegisterEnumDescriptor(_RIVALINFO_TYPE)


_RIVALINFO = _descriptor.Descriptor(
  name='RivalInfo',
  full_name='SanProto.RivalInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='SanProto.RivalInfo.node_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='SanProto.RivalInfo.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rival_id', full_name='SanProto.RivalInfo.rival_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='SanProto.RivalInfo.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='SanProto.RivalInfo.name', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon_id', full_name='SanProto.RivalInfo.icon_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='SanProto.RivalInfo.score', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='teams', full_name='SanProto.RivalInfo.teams', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buff_ids', full_name='SanProto.RivalInfo.buff_ids', index=8,
      number=9, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_tech_ids', full_name='SanProto.RivalInfo.battle_tech_ids', index=9,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward_resource', full_name='SanProto.RivalInfo.reward_resource', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward_items', full_name='SanProto.RivalInfo.reward_items', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country', full_name='SanProto.RivalInfo.country', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RIVALINFO_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=658,
)

_RIVALINFO.fields_by_name['type'].enum_type = _RIVALINFO_TYPE
_RIVALINFO.fields_by_name['teams'].message_type = team_pb2._TEAMINFO
_RIVALINFO.fields_by_name['reward_resource'].message_type = resource_pb2._RESOURCEINFO
_RIVALINFO.fields_by_name['reward_items'].message_type = item_pb2._ITEMINFO
_RIVALINFO_TYPE.containing_type = _RIVALINFO
DESCRIPTOR.message_types_by_name['RivalInfo'] = _RIVALINFO

RivalInfo = _reflection.GeneratedProtocolMessageType('RivalInfo', (_message.Message,), dict(
  DESCRIPTOR = _RIVALINFO,
  __module__ = 'rival_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.RivalInfo)
  ))
_sym_db.RegisterMessage(RivalInfo)


# @@protoc_insertion_point(module_scope)
