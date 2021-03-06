# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dungeon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import resource_pb2
import team_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dungeon.proto',
  package='SanProto',
  serialized_pb=_b('\n\rdungeon.proto\x12\x08SanProto\x1a\x0eresource.proto\x1a\nteam.proto\"}\n\x0b\x44ungeonInfo\x12,\n\x06status\x18\x01 \x02(\x0e\x32\x1c.SanProto.DungeonInfo.STATUS\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x05\".\n\x06STATUS\x12\x0c\n\x08INACTIVE\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\n\n\x06LOCKED\x10\x03\"&\n\x13QueryDungeonInfoReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\"R\n\x13QueryDungeonInfoRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12+\n\x0c\x64ungeon_info\x18\x02 \x01(\x0b\x32\x15.SanProto.DungeonInfo\"\xad\x02\n\x11\x45xpandDungeonInfo\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x32\n\x06status\x18\x02 \x02(\x0e\x32\".SanProto.ExpandDungeonInfo.STATUS\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\x05\x12\'\n\x0b\x65nemy_teams\x18\x04 \x03(\x0b\x32\x12.SanProto.TeamInfo\x12%\n\town_teams\x18\x05 \x03(\x0b\x32\x12.SanProto.TeamInfo\x12\x12\n\nremain_num\x18\x06 \x01(\x05\x12\x11\n\treset_num\x18\x07 \x01(\x05\x12\x1f\n\x17\x64isplay_reward_item_ids\x18\x08 \x03(\x05\".\n\x06STATUS\x12\x0c\n\x08INACTIVE\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12\n\n\x06LOCKED\x10\x03\"=\n\x19QueryExpandDungeonInfoReq\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x14\n\x0c\x62\x61ttle_level\x18\x02 \x01(\x05\"\xb3\x01\n\x19QueryExpandDungeonInfoRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12)\n\x03ret\x18\x02 \x01(\x0e\x32\x1c.SanProto.EXPAND_DUNGEON_RET\x12\x31\n\x0c\x64ungeon_info\x18\x03 \x01(\x0b\x32\x1b.SanProto.ExpandDungeonInfo\x12(\n\x08resource\x18\x04 \x01(\x0b\x32\x16.SanProto.ResourceInfo*\xa3\x01\n\x12\x45XPAND_DUNGEON_RET\x12\x0e\n\nDUNGEON_OK\x10\x00\x12\x14\n\x10\x44UNGEON_NOT_OPEN\x10\x01\x12\x18\n\x14\x44UNGEON_NO_ENTER_NUM\x10\x02\x12\x1b\n\x17\x44UNGEON_GOLD_NOT_ENOUGH\x10\x03\x12\x16\n\x12\x44UNGEON_NO_DUNGEON\x10\x04\x12\x18\n\x14\x44UNGEON_NO_RESET_NUM\x10\x05')
  ,
  dependencies=[resource_pb2.DESCRIPTOR,team_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EXPAND_DUNGEON_RET = _descriptor.EnumDescriptor(
  name='EXPAND_DUNGEON_RET',
  full_name='SanProto.EXPAND_DUNGEON_RET',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DUNGEON_OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUNGEON_NOT_OPEN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUNGEON_NO_ENTER_NUM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUNGEON_GOLD_NOT_ENOUGH', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUNGEON_NO_DUNGEON', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUNGEON_NO_RESET_NUM', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=856,
  serialized_end=1019,
)
_sym_db.RegisterEnumDescriptor(_EXPAND_DUNGEON_RET)

EXPAND_DUNGEON_RET = enum_type_wrapper.EnumTypeWrapper(_EXPAND_DUNGEON_RET)
DUNGEON_OK = 0
DUNGEON_NOT_OPEN = 1
DUNGEON_NO_ENTER_NUM = 2
DUNGEON_GOLD_NOT_ENOUGH = 3
DUNGEON_NO_DUNGEON = 4
DUNGEON_NO_RESET_NUM = 5


_DUNGEONINFO_STATUS = _descriptor.EnumDescriptor(
  name='STATUS',
  full_name='SanProto.DungeonInfo.STATUS',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INACTIVE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCKED', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=134,
  serialized_end=180,
)
_sym_db.RegisterEnumDescriptor(_DUNGEONINFO_STATUS)

_EXPANDDUNGEONINFO_STATUS = _descriptor.EnumDescriptor(
  name='STATUS',
  full_name='SanProto.ExpandDungeonInfo.STATUS',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INACTIVE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCKED', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=134,
  serialized_end=180,
)
_sym_db.RegisterEnumDescriptor(_EXPANDDUNGEONINFO_STATUS)


_DUNGEONINFO = _descriptor.Descriptor(
  name='DungeonInfo',
  full_name='SanProto.DungeonInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.DungeonInfo.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='SanProto.DungeonInfo.end_time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DUNGEONINFO_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=180,
)


_QUERYDUNGEONINFOREQ = _descriptor.Descriptor(
  name='QueryDungeonInfoReq',
  full_name='SanProto.QueryDungeonInfoReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.QueryDungeonInfoReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
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
  serialized_start=182,
  serialized_end=220,
)


_QUERYDUNGEONINFORES = _descriptor.Descriptor(
  name='QueryDungeonInfoRes',
  full_name='SanProto.QueryDungeonInfoRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.QueryDungeonInfoRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dungeon_info', full_name='SanProto.QueryDungeonInfoRes.dungeon_info', index=1,
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
  serialized_start=222,
  serialized_end=304,
)


_EXPANDDUNGEONINFO = _descriptor.Descriptor(
  name='ExpandDungeonInfo',
  full_name='SanProto.ExpandDungeonInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SanProto.ExpandDungeonInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.ExpandDungeonInfo.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='SanProto.ExpandDungeonInfo.end_time', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enemy_teams', full_name='SanProto.ExpandDungeonInfo.enemy_teams', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='own_teams', full_name='SanProto.ExpandDungeonInfo.own_teams', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remain_num', full_name='SanProto.ExpandDungeonInfo.remain_num', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reset_num', full_name='SanProto.ExpandDungeonInfo.reset_num', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_reward_item_ids', full_name='SanProto.ExpandDungeonInfo.display_reward_item_ids', index=7,
      number=8, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXPANDDUNGEONINFO_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=608,
)


_QUERYEXPANDDUNGEONINFOREQ = _descriptor.Descriptor(
  name='QueryExpandDungeonInfoReq',
  full_name='SanProto.QueryExpandDungeonInfoReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SanProto.QueryExpandDungeonInfoReq.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_level', full_name='SanProto.QueryExpandDungeonInfoReq.battle_level', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=610,
  serialized_end=671,
)


_QUERYEXPANDDUNGEONINFORES = _descriptor.Descriptor(
  name='QueryExpandDungeonInfoRes',
  full_name='SanProto.QueryExpandDungeonInfoRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.QueryExpandDungeonInfoRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.QueryExpandDungeonInfoRes.ret', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dungeon_info', full_name='SanProto.QueryExpandDungeonInfoRes.dungeon_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.QueryExpandDungeonInfoRes.resource', index=3,
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
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=674,
  serialized_end=853,
)

_DUNGEONINFO.fields_by_name['status'].enum_type = _DUNGEONINFO_STATUS
_DUNGEONINFO_STATUS.containing_type = _DUNGEONINFO
_QUERYDUNGEONINFORES.fields_by_name['dungeon_info'].message_type = _DUNGEONINFO
_EXPANDDUNGEONINFO.fields_by_name['status'].enum_type = _EXPANDDUNGEONINFO_STATUS
_EXPANDDUNGEONINFO.fields_by_name['enemy_teams'].message_type = team_pb2._TEAMINFO
_EXPANDDUNGEONINFO.fields_by_name['own_teams'].message_type = team_pb2._TEAMINFO
_EXPANDDUNGEONINFO_STATUS.containing_type = _EXPANDDUNGEONINFO
_QUERYEXPANDDUNGEONINFORES.fields_by_name['ret'].enum_type = _EXPAND_DUNGEON_RET
_QUERYEXPANDDUNGEONINFORES.fields_by_name['dungeon_info'].message_type = _EXPANDDUNGEONINFO
_QUERYEXPANDDUNGEONINFORES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
DESCRIPTOR.message_types_by_name['DungeonInfo'] = _DUNGEONINFO
DESCRIPTOR.message_types_by_name['QueryDungeonInfoReq'] = _QUERYDUNGEONINFOREQ
DESCRIPTOR.message_types_by_name['QueryDungeonInfoRes'] = _QUERYDUNGEONINFORES
DESCRIPTOR.message_types_by_name['ExpandDungeonInfo'] = _EXPANDDUNGEONINFO
DESCRIPTOR.message_types_by_name['QueryExpandDungeonInfoReq'] = _QUERYEXPANDDUNGEONINFOREQ
DESCRIPTOR.message_types_by_name['QueryExpandDungeonInfoRes'] = _QUERYEXPANDDUNGEONINFORES
DESCRIPTOR.enum_types_by_name['EXPAND_DUNGEON_RET'] = _EXPAND_DUNGEON_RET

DungeonInfo = _reflection.GeneratedProtocolMessageType('DungeonInfo', (_message.Message,), dict(
  DESCRIPTOR = _DUNGEONINFO,
  __module__ = 'dungeon_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.DungeonInfo)
  ))
_sym_db.RegisterMessage(DungeonInfo)

QueryDungeonInfoReq = _reflection.GeneratedProtocolMessageType('QueryDungeonInfoReq', (_message.Message,), dict(
  DESCRIPTOR = _QUERYDUNGEONINFOREQ,
  __module__ = 'dungeon_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.QueryDungeonInfoReq)
  ))
_sym_db.RegisterMessage(QueryDungeonInfoReq)

QueryDungeonInfoRes = _reflection.GeneratedProtocolMessageType('QueryDungeonInfoRes', (_message.Message,), dict(
  DESCRIPTOR = _QUERYDUNGEONINFORES,
  __module__ = 'dungeon_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.QueryDungeonInfoRes)
  ))
_sym_db.RegisterMessage(QueryDungeonInfoRes)

ExpandDungeonInfo = _reflection.GeneratedProtocolMessageType('ExpandDungeonInfo', (_message.Message,), dict(
  DESCRIPTOR = _EXPANDDUNGEONINFO,
  __module__ = 'dungeon_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ExpandDungeonInfo)
  ))
_sym_db.RegisterMessage(ExpandDungeonInfo)

QueryExpandDungeonInfoReq = _reflection.GeneratedProtocolMessageType('QueryExpandDungeonInfoReq', (_message.Message,), dict(
  DESCRIPTOR = _QUERYEXPANDDUNGEONINFOREQ,
  __module__ = 'dungeon_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.QueryExpandDungeonInfoReq)
  ))
_sym_db.RegisterMessage(QueryExpandDungeonInfoReq)

QueryExpandDungeonInfoRes = _reflection.GeneratedProtocolMessageType('QueryExpandDungeonInfoRes', (_message.Message,), dict(
  DESCRIPTOR = _QUERYEXPANDDUNGEONINFORES,
  __module__ = 'dungeon_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.QueryExpandDungeonInfoRes)
  ))
_sym_db.RegisterMessage(QueryExpandDungeonInfoRes)


# @@protoc_insertion_point(module_scope)
