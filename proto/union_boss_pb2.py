# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: union_boss.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import monarch_pb2
import resource_pb2
import item_pb2
import battle_pb2
import conscript_pb2
import boss_pb2
import union_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='union_boss.proto',
  package='SanProto',
  serialized_pb=_b('\n\x10union_boss.proto\x12\x08SanProto\x1a\rmonarch.proto\x1a\x0eresource.proto\x1a\nitem.proto\x1a\x0c\x62\x61ttle.proto\x1a\x0f\x63onscript.proto\x1a\nboss.proto\x1a\x0bunion.proto\"\xbd\x01\n\x17StartUnionBossBattleReq\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.SanProto.BATTLE_TYPE\x12)\n\x06\x62\x61ttle\x18\x02 \x02(\x0b\x32\x19.SanProto.BattleInputInfo\x12\x10\n\x08union_id\x18\x03 \x02(\x05\x12\x11\n\tboss_step\x18\x04 \x02(\x05\x12\x1f\n\x17world_boss_choose_index\x18\x05 \x01(\x05\x12\x0c\n\x04gold\x18\x06 \x01(\x05\"\xf4\x01\n\x17StartUnionBossBattleRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12 \n\x03ret\x18\x02 \x01(\x0e\x32\x13.SanProto.UNION_RET\x12&\n\x06reward\x18\x03 \x01(\x0b\x32\x16.SanProto.BattleReward\x12(\n\x08resource\x18\x04 \x01(\x0b\x32\x16.SanProto.ResourceInfo\x12+\n\nconscripts\x18\x05 \x03(\x0b\x32\x17.SanProto.ConscriptInfo\x12(\n\nbattle_ret\x18\x06 \x01(\x0e\x32\x14.SanProto.BATTLE_RET\"\xc8\x01\n\x18\x46inishUnionBossBattleReq\x12#\n\x04type\x18\x01 \x02(\x0e\x32\x15.SanProto.BATTLE_TYPE\x12*\n\x06\x62\x61ttle\x18\x02 \x02(\x0b\x32\x1a.SanProto.BattleOutputInfo\x12\x10\n\x08union_id\x18\x03 \x02(\x05\x12!\n\x05items\x18\x04 \x03(\x0b\x32\x12.SanProto.ItemInfo\x12&\n\x07monarch\x18\x05 \x01(\x0b\x32\x15.SanProto.MonarchInfo\"\x97\x02\n\x18\x46inishUnionBossBattleRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12(\n\x08resource\x18\x02 \x01(\x0b\x32\x16.SanProto.ResourceInfo\x12+\n\nconscripts\x18\x03 \x03(\x0b\x32\x17.SanProto.ConscriptInfo\x12!\n\x05items\x18\x04 \x03(\x0b\x32\x12.SanProto.ItemInfo\x12%\n\x04\x62oss\x18\x05 \x01(\x0b\x32\x17.SanProto.WorldBossInfo\x12(\n\nbattle_ret\x18\x06 \x01(\x0e\x32\x14.SanProto.BATTLE_RET\x12 \n\x03ret\x18\x07 \x01(\x0e\x32\x13.SanProto.UNION_RET\"8\n\x14QueryUnionBossBoxReq\x12\x10\n\x08union_id\x18\x01 \x02(\x05\x12\x0e\n\x06\x62ox_id\x18\x02 \x02(\x05\"l\n\x14QueryUnionBossBoxRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12 \n\x03ret\x18\x02 \x01(\x0e\x32\x13.SanProto.UNION_RET\x12\"\n\x03\x62ox\x18\x03 \x01(\x0b\x32\x15.SanProto.BossBoxInfo\"F\n\x1d\x41\x63\x63\x65ptUnionBossIndividualsReq\x12\x10\n\x08union_id\x18\x01 \x02(\x05\x12\x13\n\x0btarget_step\x18\x02 \x02(\x05\"\xad\x01\n\x1d\x41\x63\x63\x65ptUnionBossIndividualsRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12 \n\x03ret\x18\x02 \x01(\x0e\x32\x13.SanProto.UNION_RET\x12(\n\x08resource\x18\x03 \x01(\x0b\x32\x16.SanProto.ResourceInfo\x12!\n\x05items\x18\x04 \x03(\x0b\x32\x12.SanProto.ItemInfo\x12\r\n\x05honor\x18\x05 \x01(\x05\";\n\x19RefreshUnionBossAttackReq\x12\x10\n\x08union_id\x18\x01 \x02(\x05\x12\x0c\n\x04gold\x18\x02 \x02(\x05\"M\n\x19RefreshUnionBossAttackRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12 \n\x03ret\x18\x02 \x01(\x0e\x32\x13.SanProto.UNION_RET\"%\n\x11QueryUnionBossReq\x12\x10\n\x08union_id\x18\x01 \x02(\x05\"r\n\x11QueryUnionBossRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12 \n\x03ret\x18\x02 \x01(\x0e\x32\x13.SanProto.UNION_RET\x12+\n\nunion_boss\x18\x03 \x01(\x0b\x32\x17.SanProto.UnionBossInfo\"^\n\x17UnionBossGroupBasicInfo\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\tbosses_id\x18\x02 \x03(\x05\x12\x12\n\nstart_date\x18\x03 \x01(\x0c\x12\x10\n\x08\x65nd_date\x18\x04 \x01(\x0c\"V\n\x1d\x41\x64\x64UnionBossGroupBasicDataReq\x12\x35\n\nboss_group\x18\x01 \x03(\x0b\x32!.SanProto.UnionBossGroupBasicInfo\"/\n\x1d\x41\x64\x64UnionBossGroupBasicDataRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\"&\n\x12UpdateUnionBossReq\x12\x10\n\x08union_id\x18\x01 \x02(\x05\"I\n\x12UpdateUnionBossRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12\x11\n\tis_update\x18\x02 \x01(\x08\x12\x10\n\x08is_reset\x18\x03 \x01(\x08')
  ,
  dependencies=[monarch_pb2.DESCRIPTOR,resource_pb2.DESCRIPTOR,item_pb2.DESCRIPTOR,battle_pb2.DESCRIPTOR,conscript_pb2.DESCRIPTOR,boss_pb2.DESCRIPTOR,union_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STARTUNIONBOSSBATTLEREQ = _descriptor.Descriptor(
  name='StartUnionBossBattleReq',
  full_name='SanProto.StartUnionBossBattleReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='SanProto.StartUnionBossBattleReq.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle', full_name='SanProto.StartUnionBossBattleReq.battle', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='union_id', full_name='SanProto.StartUnionBossBattleReq.union_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boss_step', full_name='SanProto.StartUnionBossBattleReq.boss_step', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='world_boss_choose_index', full_name='SanProto.StartUnionBossBattleReq.world_boss_choose_index', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='SanProto.StartUnionBossBattleReq.gold', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=130,
  serialized_end=319,
)


_STARTUNIONBOSSBATTLERES = _descriptor.Descriptor(
  name='StartUnionBossBattleRes',
  full_name='SanProto.StartUnionBossBattleRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.StartUnionBossBattleRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.StartUnionBossBattleRes.ret', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward', full_name='SanProto.StartUnionBossBattleRes.reward', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.StartUnionBossBattleRes.resource', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conscripts', full_name='SanProto.StartUnionBossBattleRes.conscripts', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_ret', full_name='SanProto.StartUnionBossBattleRes.battle_ret', index=5,
      number=6, type=14, cpp_type=8, label=1,
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
  serialized_start=322,
  serialized_end=566,
)


_FINISHUNIONBOSSBATTLEREQ = _descriptor.Descriptor(
  name='FinishUnionBossBattleReq',
  full_name='SanProto.FinishUnionBossBattleReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='SanProto.FinishUnionBossBattleReq.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle', full_name='SanProto.FinishUnionBossBattleReq.battle', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='union_id', full_name='SanProto.FinishUnionBossBattleReq.union_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='SanProto.FinishUnionBossBattleReq.items', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='monarch', full_name='SanProto.FinishUnionBossBattleReq.monarch', index=4,
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
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=569,
  serialized_end=769,
)


_FINISHUNIONBOSSBATTLERES = _descriptor.Descriptor(
  name='FinishUnionBossBattleRes',
  full_name='SanProto.FinishUnionBossBattleRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.FinishUnionBossBattleRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.FinishUnionBossBattleRes.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conscripts', full_name='SanProto.FinishUnionBossBattleRes.conscripts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='SanProto.FinishUnionBossBattleRes.items', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boss', full_name='SanProto.FinishUnionBossBattleRes.boss', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_ret', full_name='SanProto.FinishUnionBossBattleRes.battle_ret', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.FinishUnionBossBattleRes.ret', index=6,
      number=7, type=14, cpp_type=8, label=1,
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
  serialized_start=772,
  serialized_end=1051,
)


_QUERYUNIONBOSSBOXREQ = _descriptor.Descriptor(
  name='QueryUnionBossBoxReq',
  full_name='SanProto.QueryUnionBossBoxReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='union_id', full_name='SanProto.QueryUnionBossBoxReq.union_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_id', full_name='SanProto.QueryUnionBossBoxReq.box_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_end=1109,
)


_QUERYUNIONBOSSBOXRES = _descriptor.Descriptor(
  name='QueryUnionBossBoxRes',
  full_name='SanProto.QueryUnionBossBoxRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.QueryUnionBossBoxRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.QueryUnionBossBoxRes.ret', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box', full_name='SanProto.QueryUnionBossBoxRes.box', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1111,
  serialized_end=1219,
)


_ACCEPTUNIONBOSSINDIVIDUALSREQ = _descriptor.Descriptor(
  name='AcceptUnionBossIndividualsReq',
  full_name='SanProto.AcceptUnionBossIndividualsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='union_id', full_name='SanProto.AcceptUnionBossIndividualsReq.union_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_step', full_name='SanProto.AcceptUnionBossIndividualsReq.target_step', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=1221,
  serialized_end=1291,
)


_ACCEPTUNIONBOSSINDIVIDUALSRES = _descriptor.Descriptor(
  name='AcceptUnionBossIndividualsRes',
  full_name='SanProto.AcceptUnionBossIndividualsRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.AcceptUnionBossIndividualsRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.AcceptUnionBossIndividualsRes.ret', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.AcceptUnionBossIndividualsRes.resource', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='SanProto.AcceptUnionBossIndividualsRes.items', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='honor', full_name='SanProto.AcceptUnionBossIndividualsRes.honor', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=1294,
  serialized_end=1467,
)


_REFRESHUNIONBOSSATTACKREQ = _descriptor.Descriptor(
  name='RefreshUnionBossAttackReq',
  full_name='SanProto.RefreshUnionBossAttackReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='union_id', full_name='SanProto.RefreshUnionBossAttackReq.union_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='SanProto.RefreshUnionBossAttackReq.gold', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=1469,
  serialized_end=1528,
)


_REFRESHUNIONBOSSATTACKRES = _descriptor.Descriptor(
  name='RefreshUnionBossAttackRes',
  full_name='SanProto.RefreshUnionBossAttackRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.RefreshUnionBossAttackRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.RefreshUnionBossAttackRes.ret', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=1530,
  serialized_end=1607,
)


_QUERYUNIONBOSSREQ = _descriptor.Descriptor(
  name='QueryUnionBossReq',
  full_name='SanProto.QueryUnionBossReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='union_id', full_name='SanProto.QueryUnionBossReq.union_id', index=0,
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
  serialized_start=1609,
  serialized_end=1646,
)


_QUERYUNIONBOSSRES = _descriptor.Descriptor(
  name='QueryUnionBossRes',
  full_name='SanProto.QueryUnionBossRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.QueryUnionBossRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.QueryUnionBossRes.ret', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='union_boss', full_name='SanProto.QueryUnionBossRes.union_boss', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1648,
  serialized_end=1762,
)


_UNIONBOSSGROUPBASICINFO = _descriptor.Descriptor(
  name='UnionBossGroupBasicInfo',
  full_name='SanProto.UnionBossGroupBasicInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SanProto.UnionBossGroupBasicInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bosses_id', full_name='SanProto.UnionBossGroupBasicInfo.bosses_id', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='SanProto.UnionBossGroupBasicInfo.start_date', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='SanProto.UnionBossGroupBasicInfo.end_date', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
  serialized_start=1764,
  serialized_end=1858,
)


_ADDUNIONBOSSGROUPBASICDATAREQ = _descriptor.Descriptor(
  name='AddUnionBossGroupBasicDataReq',
  full_name='SanProto.AddUnionBossGroupBasicDataReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boss_group', full_name='SanProto.AddUnionBossGroupBasicDataReq.boss_group', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1860,
  serialized_end=1946,
)


_ADDUNIONBOSSGROUPBASICDATARES = _descriptor.Descriptor(
  name='AddUnionBossGroupBasicDataRes',
  full_name='SanProto.AddUnionBossGroupBasicDataRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.AddUnionBossGroupBasicDataRes.status', index=0,
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
  serialized_start=1948,
  serialized_end=1995,
)


_UPDATEUNIONBOSSREQ = _descriptor.Descriptor(
  name='UpdateUnionBossReq',
  full_name='SanProto.UpdateUnionBossReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='union_id', full_name='SanProto.UpdateUnionBossReq.union_id', index=0,
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
  serialized_start=1997,
  serialized_end=2035,
)


_UPDATEUNIONBOSSRES = _descriptor.Descriptor(
  name='UpdateUnionBossRes',
  full_name='SanProto.UpdateUnionBossRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.UpdateUnionBossRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_update', full_name='SanProto.UpdateUnionBossRes.is_update', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_reset', full_name='SanProto.UpdateUnionBossRes.is_reset', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=2037,
  serialized_end=2110,
)

_STARTUNIONBOSSBATTLEREQ.fields_by_name['type'].enum_type = battle_pb2._BATTLE_TYPE
_STARTUNIONBOSSBATTLEREQ.fields_by_name['battle'].message_type = battle_pb2._BATTLEINPUTINFO
_STARTUNIONBOSSBATTLERES.fields_by_name['ret'].enum_type = union_pb2._UNION_RET
_STARTUNIONBOSSBATTLERES.fields_by_name['reward'].message_type = battle_pb2._BATTLEREWARD
_STARTUNIONBOSSBATTLERES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_STARTUNIONBOSSBATTLERES.fields_by_name['conscripts'].message_type = conscript_pb2._CONSCRIPTINFO
_STARTUNIONBOSSBATTLERES.fields_by_name['battle_ret'].enum_type = battle_pb2._BATTLE_RET
_FINISHUNIONBOSSBATTLEREQ.fields_by_name['type'].enum_type = battle_pb2._BATTLE_TYPE
_FINISHUNIONBOSSBATTLEREQ.fields_by_name['battle'].message_type = battle_pb2._BATTLEOUTPUTINFO
_FINISHUNIONBOSSBATTLEREQ.fields_by_name['items'].message_type = item_pb2._ITEMINFO
_FINISHUNIONBOSSBATTLEREQ.fields_by_name['monarch'].message_type = monarch_pb2._MONARCHINFO
_FINISHUNIONBOSSBATTLERES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_FINISHUNIONBOSSBATTLERES.fields_by_name['conscripts'].message_type = conscript_pb2._CONSCRIPTINFO
_FINISHUNIONBOSSBATTLERES.fields_by_name['items'].message_type = item_pb2._ITEMINFO
_FINISHUNIONBOSSBATTLERES.fields_by_name['boss'].message_type = boss_pb2._WORLDBOSSINFO
_FINISHUNIONBOSSBATTLERES.fields_by_name['battle_ret'].enum_type = battle_pb2._BATTLE_RET
_FINISHUNIONBOSSBATTLERES.fields_by_name['ret'].enum_type = union_pb2._UNION_RET
_QUERYUNIONBOSSBOXRES.fields_by_name['ret'].enum_type = union_pb2._UNION_RET
_QUERYUNIONBOSSBOXRES.fields_by_name['box'].message_type = union_pb2._BOSSBOXINFO
_ACCEPTUNIONBOSSINDIVIDUALSRES.fields_by_name['ret'].enum_type = union_pb2._UNION_RET
_ACCEPTUNIONBOSSINDIVIDUALSRES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_ACCEPTUNIONBOSSINDIVIDUALSRES.fields_by_name['items'].message_type = item_pb2._ITEMINFO
_REFRESHUNIONBOSSATTACKRES.fields_by_name['ret'].enum_type = union_pb2._UNION_RET
_QUERYUNIONBOSSRES.fields_by_name['ret'].enum_type = union_pb2._UNION_RET
_QUERYUNIONBOSSRES.fields_by_name['union_boss'].message_type = union_pb2._UNIONBOSSINFO
_ADDUNIONBOSSGROUPBASICDATAREQ.fields_by_name['boss_group'].message_type = _UNIONBOSSGROUPBASICINFO
DESCRIPTOR.message_types_by_name['StartUnionBossBattleReq'] = _STARTUNIONBOSSBATTLEREQ
DESCRIPTOR.message_types_by_name['StartUnionBossBattleRes'] = _STARTUNIONBOSSBATTLERES
DESCRIPTOR.message_types_by_name['FinishUnionBossBattleReq'] = _FINISHUNIONBOSSBATTLEREQ
DESCRIPTOR.message_types_by_name['FinishUnionBossBattleRes'] = _FINISHUNIONBOSSBATTLERES
DESCRIPTOR.message_types_by_name['QueryUnionBossBoxReq'] = _QUERYUNIONBOSSBOXREQ
DESCRIPTOR.message_types_by_name['QueryUnionBossBoxRes'] = _QUERYUNIONBOSSBOXRES
DESCRIPTOR.message_types_by_name['AcceptUnionBossIndividualsReq'] = _ACCEPTUNIONBOSSINDIVIDUALSREQ
DESCRIPTOR.message_types_by_name['AcceptUnionBossIndividualsRes'] = _ACCEPTUNIONBOSSINDIVIDUALSRES
DESCRIPTOR.message_types_by_name['RefreshUnionBossAttackReq'] = _REFRESHUNIONBOSSATTACKREQ
DESCRIPTOR.message_types_by_name['RefreshUnionBossAttackRes'] = _REFRESHUNIONBOSSATTACKRES
DESCRIPTOR.message_types_by_name['QueryUnionBossReq'] = _QUERYUNIONBOSSREQ
DESCRIPTOR.message_types_by_name['QueryUnionBossRes'] = _QUERYUNIONBOSSRES
DESCRIPTOR.message_types_by_name['UnionBossGroupBasicInfo'] = _UNIONBOSSGROUPBASICINFO
DESCRIPTOR.message_types_by_name['AddUnionBossGroupBasicDataReq'] = _ADDUNIONBOSSGROUPBASICDATAREQ
DESCRIPTOR.message_types_by_name['AddUnionBossGroupBasicDataRes'] = _ADDUNIONBOSSGROUPBASICDATARES
DESCRIPTOR.message_types_by_name['UpdateUnionBossReq'] = _UPDATEUNIONBOSSREQ
DESCRIPTOR.message_types_by_name['UpdateUnionBossRes'] = _UPDATEUNIONBOSSRES

StartUnionBossBattleReq = _reflection.GeneratedProtocolMessageType('StartUnionBossBattleReq', (_message.Message,), dict(
  DESCRIPTOR = _STARTUNIONBOSSBATTLEREQ,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.StartUnionBossBattleReq)
  ))
_sym_db.RegisterMessage(StartUnionBossBattleReq)

StartUnionBossBattleRes = _reflection.GeneratedProtocolMessageType('StartUnionBossBattleRes', (_message.Message,), dict(
  DESCRIPTOR = _STARTUNIONBOSSBATTLERES,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.StartUnionBossBattleRes)
  ))
_sym_db.RegisterMessage(StartUnionBossBattleRes)

FinishUnionBossBattleReq = _reflection.GeneratedProtocolMessageType('FinishUnionBossBattleReq', (_message.Message,), dict(
  DESCRIPTOR = _FINISHUNIONBOSSBATTLEREQ,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.FinishUnionBossBattleReq)
  ))
_sym_db.RegisterMessage(FinishUnionBossBattleReq)

FinishUnionBossBattleRes = _reflection.GeneratedProtocolMessageType('FinishUnionBossBattleRes', (_message.Message,), dict(
  DESCRIPTOR = _FINISHUNIONBOSSBATTLERES,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.FinishUnionBossBattleRes)
  ))
_sym_db.RegisterMessage(FinishUnionBossBattleRes)

QueryUnionBossBoxReq = _reflection.GeneratedProtocolMessageType('QueryUnionBossBoxReq', (_message.Message,), dict(
  DESCRIPTOR = _QUERYUNIONBOSSBOXREQ,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.QueryUnionBossBoxReq)
  ))
_sym_db.RegisterMessage(QueryUnionBossBoxReq)

QueryUnionBossBoxRes = _reflection.GeneratedProtocolMessageType('QueryUnionBossBoxRes', (_message.Message,), dict(
  DESCRIPTOR = _QUERYUNIONBOSSBOXRES,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.QueryUnionBossBoxRes)
  ))
_sym_db.RegisterMessage(QueryUnionBossBoxRes)

AcceptUnionBossIndividualsReq = _reflection.GeneratedProtocolMessageType('AcceptUnionBossIndividualsReq', (_message.Message,), dict(
  DESCRIPTOR = _ACCEPTUNIONBOSSINDIVIDUALSREQ,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.AcceptUnionBossIndividualsReq)
  ))
_sym_db.RegisterMessage(AcceptUnionBossIndividualsReq)

AcceptUnionBossIndividualsRes = _reflection.GeneratedProtocolMessageType('AcceptUnionBossIndividualsRes', (_message.Message,), dict(
  DESCRIPTOR = _ACCEPTUNIONBOSSINDIVIDUALSRES,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.AcceptUnionBossIndividualsRes)
  ))
_sym_db.RegisterMessage(AcceptUnionBossIndividualsRes)

RefreshUnionBossAttackReq = _reflection.GeneratedProtocolMessageType('RefreshUnionBossAttackReq', (_message.Message,), dict(
  DESCRIPTOR = _REFRESHUNIONBOSSATTACKREQ,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.RefreshUnionBossAttackReq)
  ))
_sym_db.RegisterMessage(RefreshUnionBossAttackReq)

RefreshUnionBossAttackRes = _reflection.GeneratedProtocolMessageType('RefreshUnionBossAttackRes', (_message.Message,), dict(
  DESCRIPTOR = _REFRESHUNIONBOSSATTACKRES,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.RefreshUnionBossAttackRes)
  ))
_sym_db.RegisterMessage(RefreshUnionBossAttackRes)

QueryUnionBossReq = _reflection.GeneratedProtocolMessageType('QueryUnionBossReq', (_message.Message,), dict(
  DESCRIPTOR = _QUERYUNIONBOSSREQ,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.QueryUnionBossReq)
  ))
_sym_db.RegisterMessage(QueryUnionBossReq)

QueryUnionBossRes = _reflection.GeneratedProtocolMessageType('QueryUnionBossRes', (_message.Message,), dict(
  DESCRIPTOR = _QUERYUNIONBOSSRES,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.QueryUnionBossRes)
  ))
_sym_db.RegisterMessage(QueryUnionBossRes)

UnionBossGroupBasicInfo = _reflection.GeneratedProtocolMessageType('UnionBossGroupBasicInfo', (_message.Message,), dict(
  DESCRIPTOR = _UNIONBOSSGROUPBASICINFO,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UnionBossGroupBasicInfo)
  ))
_sym_db.RegisterMessage(UnionBossGroupBasicInfo)

AddUnionBossGroupBasicDataReq = _reflection.GeneratedProtocolMessageType('AddUnionBossGroupBasicDataReq', (_message.Message,), dict(
  DESCRIPTOR = _ADDUNIONBOSSGROUPBASICDATAREQ,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.AddUnionBossGroupBasicDataReq)
  ))
_sym_db.RegisterMessage(AddUnionBossGroupBasicDataReq)

AddUnionBossGroupBasicDataRes = _reflection.GeneratedProtocolMessageType('AddUnionBossGroupBasicDataRes', (_message.Message,), dict(
  DESCRIPTOR = _ADDUNIONBOSSGROUPBASICDATARES,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.AddUnionBossGroupBasicDataRes)
  ))
_sym_db.RegisterMessage(AddUnionBossGroupBasicDataRes)

UpdateUnionBossReq = _reflection.GeneratedProtocolMessageType('UpdateUnionBossReq', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUNIONBOSSREQ,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpdateUnionBossReq)
  ))
_sym_db.RegisterMessage(UpdateUnionBossReq)

UpdateUnionBossRes = _reflection.GeneratedProtocolMessageType('UpdateUnionBossRes', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUNIONBOSSRES,
  __module__ = 'union_boss_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpdateUnionBossRes)
  ))
_sym_db.RegisterMessage(UpdateUnionBossRes)


# @@protoc_insertion_point(module_scope)
