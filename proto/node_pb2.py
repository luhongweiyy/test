# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: node.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import item_pb2
import rival_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='node.proto',
  package='SanProto',
  serialized_pb=_b('\n\nnode.proto\x12\x08SanProto\x1a\nitem.proto\x1a\x0brival.proto\"\x8c\x03\n\x10\x45xploitationInfo\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12-\n\x04type\x18\x02 \x02(\x0e\x32\x1f.SanProto.ExploitationInfo.TYPE\x12\r\n\x05level\x18\x03 \x01(\x05\x12\x14\n\x0cgather_speed\x18\x04 \x01(\x02\x12\x17\n\x0fgather_duration\x18\x05 \x01(\x05\x12\x12\n\ntotal_time\x18\x06 \x01(\x05\x12\x10\n\x08\x64uration\x18\x07 \x01(\x05\x12\x13\n\x0btotal_money\x18\x08 \x01(\x05\x12\x12\n\ntotal_food\x18\t \x01(\x05\x12\x12\n\ntotal_gold\x18\n \x01(\x05\x12\x16\n\x0ehero_basic_ids\x18\x0b \x03(\x05\x12\x10\n\x08progress\x18\x0c \x01(\x02\"m\n\x04TYPE\x12\t\n\x05MONEY\x10\x01\x12\x08\n\x04\x46OOD\x10\x02\x12\x08\n\x04GOLD\x10\x03\x12\x0c\n\x08MATERIAL\x10\x04\x12\x0f\n\x0bRANDOM_ITEM\x10\x05\x12\x13\n\x0f\x45\x43HANT_MATERIAL\x10\x06\x12\x12\n\x0eHERO_STAR_SOUL\x10\x07\"\xec\x02\n\x0eLuckyEventInfo\x12+\n\x04type\x18\x01 \x02(\x0e\x32\x1d.SanProto.LuckyEventInfo.TYPE\x12\x16\n\x0e\x61rise_duration\x18\x02 \x01(\x05\x12\x13\n\x0bis_launched\x18\x03 \x01(\x08\x12\x17\n\x0flaunch_duration\x18\x04 \x01(\x05\"\xe6\x01\n\x04TYPE\x12\x07\n\x03TAX\x10\x01\x12\x08\n\x04\x46\x41RM\x10\x02\x12\n\n\x06MINING\x10\x03\x12\x08\n\x04GOLD\x10\x04\x12\x0b\n\x07UPGRADE\x10\x05\x12\n\n\x06\x44\x45\x46\x45ND\x10\x06\x12\x0c\n\x08QUESTION\x10\x07\x12\t\n\x05VISIT\x10\x08\x12\x07\n\x03SPY\x10\t\x12\n\n\x06JUNGLE\x10\n\x12\x0b\n\x07\x44UNGEON\x10\x0b\x12\t\n\x05\x41RENA\x10\x0c\x12\t\n\x05SCOUT\x10\r\x12\n\n\x06SEARCH\x10\x0e\x12\x0f\n\x0b\x44\x45\x45P_MINING\x10\x0f\x12\n\n\x06HERMIT\x10\x10\x12\x0e\n\nWORLD_BOSS\x10\x11\x12\x12\n\x0e\x45XPAND_DUNGEON\x10\x12\"L\n\x0b\x41ppointInfo\x12\x14\n\x0cteam_indexes\x18\x01 \x03(\x05\x12\x12\n\ntotal_time\x18\x02 \x01(\x05\x12\x13\n\x0bpassed_time\x18\x03 \x01(\x05\"\x9d\x01\n\x0eProtectionInfo\x12+\n\x04type\x18\x01 \x02(\x0e\x32\x1d.SanProto.ProtectionInfo.TYPE\x12\x10\n\x08use_gold\x18\x02 \x01(\x08\x12\x12\n\ntotal_time\x18\x03 \x01(\x05\x12\x13\n\x0bpassed_time\x18\x04 \x01(\x05\"#\n\x04TYPE\x12\x08\n\x04\x43ITY\x10\x01\x12\x11\n\rRESOURCE_NODE\x10\x02\"W\n\x0cIncreaseInfo\x12\x10\n\x08use_gold\x18\x01 \x01(\x08\x12\x12\n\ntotal_time\x18\x02 \x01(\x05\x12\x13\n\x0bpassed_time\x18\x03 \x01(\x05\x12\x0c\n\x04rate\x18\x04 \x01(\x02\"\xf7\x03\n\x08NodeInfo\x12\x10\n\x08\x62\x61sic_id\x18\x01 \x02(\x05\x12%\n\x04type\x18\x02 \x02(\x0e\x32\x17.SanProto.NodeInfo.TYPE\x12)\n\x06status\x18\x03 \x02(\x0e\x32\x19.SanProto.NodeInfo.STATUS\x12\x15\n\rhold_duration\x18\x04 \x01(\x05\x12\"\n\x05rival\x18\x05 \x01(\x0b\x32\x13.SanProto.RivalInfo\x12\x30\n\x0c\x65xploitation\x18\x06 \x01(\x0b\x32\x1a.SanProto.ExploitationInfo\x12-\n\x0blucky_event\x18\t \x01(\x0b\x32\x18.SanProto.LuckyEventInfo\x12&\n\x07\x61ppoint\x18\n \x01(\x0b\x32\x15.SanProto.AppointInfo\x12)\n\x07protect\x18\x0b \x01(\x0b\x32\x18.SanProto.ProtectionInfo\x12(\n\x08increase\x18\x0c \x01(\x0b\x32\x16.SanProto.IncreaseInfo\x12\x12\n\ncity_level\x18\r \x01(\x05\"(\n\x04TYPE\x12\x07\n\x03OWN\x10\x01\x12\x07\n\x03KEY\x10\x02\x12\x0e\n\nDEPENDENCY\x10\x03\"0\n\x06STATUS\x12\t\n\x05\x45NEMY\x10\x01\x12\x0c\n\x08\x44OMINATE\x10\x02\x12\r\n\tINVISIBLE\x10\x03\"Y\n\x07MapInfo\x12!\n\x05nodes\x18\x01 \x03(\x0b\x32\x12.SanProto.NodeInfo\x12\x14\n\x0cnext_war_gap\x18\x02 \x01(\x05\x12\x15\n\rnext_luck_gap\x18\x03 \x01(\x05')
  ,
  dependencies=[item_pb2.DESCRIPTOR,rival_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_EXPLOITATIONINFO_TYPE = _descriptor.EnumDescriptor(
  name='TYPE',
  full_name='SanProto.ExploitationInfo.TYPE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MONEY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOOD', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOLD', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MATERIAL', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANDOM_ITEM', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ECHANT_MATERIAL', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HERO_STAR_SOUL', index=6, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=337,
  serialized_end=446,
)
_sym_db.RegisterEnumDescriptor(_EXPLOITATIONINFO_TYPE)

_LUCKYEVENTINFO_TYPE = _descriptor.EnumDescriptor(
  name='TYPE',
  full_name='SanProto.LuckyEventInfo.TYPE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TAX', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FARM', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINING', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOLD', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPGRADE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFEND', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUESTION', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VISIT', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPY', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JUNGLE', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DUNGEON', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARENA', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCOUT', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEARCH', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEEP_MINING', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HERMIT', index=15, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORLD_BOSS', index=16, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPAND_DUNGEON', index=17, number=18,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=583,
  serialized_end=813,
)
_sym_db.RegisterEnumDescriptor(_LUCKYEVENTINFO_TYPE)

_PROTECTIONINFO_TYPE = _descriptor.EnumDescriptor(
  name='TYPE',
  full_name='SanProto.ProtectionInfo.TYPE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CITY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_NODE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1016,
  serialized_end=1051,
)
_sym_db.RegisterEnumDescriptor(_PROTECTIONINFO_TYPE)

_NODEINFO_TYPE = _descriptor.EnumDescriptor(
  name='TYPE',
  full_name='SanProto.NodeInfo.TYPE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OWN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEY', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEPENDENCY', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1556,
  serialized_end=1596,
)
_sym_db.RegisterEnumDescriptor(_NODEINFO_TYPE)

_NODEINFO_STATUS = _descriptor.EnumDescriptor(
  name='STATUS',
  full_name='SanProto.NodeInfo.STATUS',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENEMY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOMINATE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVISIBLE', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1598,
  serialized_end=1646,
)
_sym_db.RegisterEnumDescriptor(_NODEINFO_STATUS)


_EXPLOITATIONINFO = _descriptor.Descriptor(
  name='ExploitationInfo',
  full_name='SanProto.ExploitationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='SanProto.ExploitationInfo.node_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='SanProto.ExploitationInfo.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='SanProto.ExploitationInfo.level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gather_speed', full_name='SanProto.ExploitationInfo.gather_speed', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gather_duration', full_name='SanProto.ExploitationInfo.gather_duration', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_time', full_name='SanProto.ExploitationInfo.total_time', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='SanProto.ExploitationInfo.duration', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_money', full_name='SanProto.ExploitationInfo.total_money', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_food', full_name='SanProto.ExploitationInfo.total_food', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_gold', full_name='SanProto.ExploitationInfo.total_gold', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_basic_ids', full_name='SanProto.ExploitationInfo.hero_basic_ids', index=10,
      number=11, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='progress', full_name='SanProto.ExploitationInfo.progress', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXPLOITATIONINFO_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=446,
)


_LUCKYEVENTINFO = _descriptor.Descriptor(
  name='LuckyEventInfo',
  full_name='SanProto.LuckyEventInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='SanProto.LuckyEventInfo.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arise_duration', full_name='SanProto.LuckyEventInfo.arise_duration', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_launched', full_name='SanProto.LuckyEventInfo.is_launched', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='launch_duration', full_name='SanProto.LuckyEventInfo.launch_duration', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LUCKYEVENTINFO_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=449,
  serialized_end=813,
)


_APPOINTINFO = _descriptor.Descriptor(
  name='AppointInfo',
  full_name='SanProto.AppointInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='team_indexes', full_name='SanProto.AppointInfo.team_indexes', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_time', full_name='SanProto.AppointInfo.total_time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passed_time', full_name='SanProto.AppointInfo.passed_time', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=815,
  serialized_end=891,
)


_PROTECTIONINFO = _descriptor.Descriptor(
  name='ProtectionInfo',
  full_name='SanProto.ProtectionInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='SanProto.ProtectionInfo.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_gold', full_name='SanProto.ProtectionInfo.use_gold', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_time', full_name='SanProto.ProtectionInfo.total_time', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passed_time', full_name='SanProto.ProtectionInfo.passed_time', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROTECTIONINFO_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=894,
  serialized_end=1051,
)


_INCREASEINFO = _descriptor.Descriptor(
  name='IncreaseInfo',
  full_name='SanProto.IncreaseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='use_gold', full_name='SanProto.IncreaseInfo.use_gold', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_time', full_name='SanProto.IncreaseInfo.total_time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passed_time', full_name='SanProto.IncreaseInfo.passed_time', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rate', full_name='SanProto.IncreaseInfo.rate', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=1053,
  serialized_end=1140,
)


_NODEINFO = _descriptor.Descriptor(
  name='NodeInfo',
  full_name='SanProto.NodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic_id', full_name='SanProto.NodeInfo.basic_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='SanProto.NodeInfo.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.NodeInfo.status', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hold_duration', full_name='SanProto.NodeInfo.hold_duration', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rival', full_name='SanProto.NodeInfo.rival', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exploitation', full_name='SanProto.NodeInfo.exploitation', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lucky_event', full_name='SanProto.NodeInfo.lucky_event', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appoint', full_name='SanProto.NodeInfo.appoint', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protect', full_name='SanProto.NodeInfo.protect', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='increase', full_name='SanProto.NodeInfo.increase', index=9,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city_level', full_name='SanProto.NodeInfo.city_level', index=10,
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
    _NODEINFO_TYPE,
    _NODEINFO_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1143,
  serialized_end=1646,
)


_MAPINFO = _descriptor.Descriptor(
  name='MapInfo',
  full_name='SanProto.MapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='SanProto.MapInfo.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_war_gap', full_name='SanProto.MapInfo.next_war_gap', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_luck_gap', full_name='SanProto.MapInfo.next_luck_gap', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=1648,
  serialized_end=1737,
)

_EXPLOITATIONINFO.fields_by_name['type'].enum_type = _EXPLOITATIONINFO_TYPE
_EXPLOITATIONINFO_TYPE.containing_type = _EXPLOITATIONINFO
_LUCKYEVENTINFO.fields_by_name['type'].enum_type = _LUCKYEVENTINFO_TYPE
_LUCKYEVENTINFO_TYPE.containing_type = _LUCKYEVENTINFO
_PROTECTIONINFO.fields_by_name['type'].enum_type = _PROTECTIONINFO_TYPE
_PROTECTIONINFO_TYPE.containing_type = _PROTECTIONINFO
_NODEINFO.fields_by_name['type'].enum_type = _NODEINFO_TYPE
_NODEINFO.fields_by_name['status'].enum_type = _NODEINFO_STATUS
_NODEINFO.fields_by_name['rival'].message_type = rival_pb2._RIVALINFO
_NODEINFO.fields_by_name['exploitation'].message_type = _EXPLOITATIONINFO
_NODEINFO.fields_by_name['lucky_event'].message_type = _LUCKYEVENTINFO
_NODEINFO.fields_by_name['appoint'].message_type = _APPOINTINFO
_NODEINFO.fields_by_name['protect'].message_type = _PROTECTIONINFO
_NODEINFO.fields_by_name['increase'].message_type = _INCREASEINFO
_NODEINFO_TYPE.containing_type = _NODEINFO
_NODEINFO_STATUS.containing_type = _NODEINFO
_MAPINFO.fields_by_name['nodes'].message_type = _NODEINFO
DESCRIPTOR.message_types_by_name['ExploitationInfo'] = _EXPLOITATIONINFO
DESCRIPTOR.message_types_by_name['LuckyEventInfo'] = _LUCKYEVENTINFO
DESCRIPTOR.message_types_by_name['AppointInfo'] = _APPOINTINFO
DESCRIPTOR.message_types_by_name['ProtectionInfo'] = _PROTECTIONINFO
DESCRIPTOR.message_types_by_name['IncreaseInfo'] = _INCREASEINFO
DESCRIPTOR.message_types_by_name['NodeInfo'] = _NODEINFO
DESCRIPTOR.message_types_by_name['MapInfo'] = _MAPINFO

ExploitationInfo = _reflection.GeneratedProtocolMessageType('ExploitationInfo', (_message.Message,), dict(
  DESCRIPTOR = _EXPLOITATIONINFO,
  __module__ = 'node_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ExploitationInfo)
  ))
_sym_db.RegisterMessage(ExploitationInfo)

LuckyEventInfo = _reflection.GeneratedProtocolMessageType('LuckyEventInfo', (_message.Message,), dict(
  DESCRIPTOR = _LUCKYEVENTINFO,
  __module__ = 'node_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.LuckyEventInfo)
  ))
_sym_db.RegisterMessage(LuckyEventInfo)

AppointInfo = _reflection.GeneratedProtocolMessageType('AppointInfo', (_message.Message,), dict(
  DESCRIPTOR = _APPOINTINFO,
  __module__ = 'node_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.AppointInfo)
  ))
_sym_db.RegisterMessage(AppointInfo)

ProtectionInfo = _reflection.GeneratedProtocolMessageType('ProtectionInfo', (_message.Message,), dict(
  DESCRIPTOR = _PROTECTIONINFO,
  __module__ = 'node_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ProtectionInfo)
  ))
_sym_db.RegisterMessage(ProtectionInfo)

IncreaseInfo = _reflection.GeneratedProtocolMessageType('IncreaseInfo', (_message.Message,), dict(
  DESCRIPTOR = _INCREASEINFO,
  __module__ = 'node_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.IncreaseInfo)
  ))
_sym_db.RegisterMessage(IncreaseInfo)

NodeInfo = _reflection.GeneratedProtocolMessageType('NodeInfo', (_message.Message,), dict(
  DESCRIPTOR = _NODEINFO,
  __module__ = 'node_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.NodeInfo)
  ))
_sym_db.RegisterMessage(NodeInfo)

MapInfo = _reflection.GeneratedProtocolMessageType('MapInfo', (_message.Message,), dict(
  DESCRIPTOR = _MAPINFO,
  __module__ = 'node_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.MapInfo)
  ))
_sym_db.RegisterMessage(MapInfo)


# @@protoc_insertion_point(module_scope)
