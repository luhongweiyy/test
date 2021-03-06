# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transfer_arena.proto

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
import battle_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transfer_arena.proto',
  package='SanProto',
  serialized_pb=_b('\n\x14transfer_arena.proto\x12\x08SanProto\x1a\x0eresource.proto\x1a\x0c\x62\x61ttle.proto\"x\n\x11TransferArenaInfo\x12\x14\n\x0cremain_times\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x64_end_time\x18\x02 \x01(\x05\x12\x38\n\x07records\x18\x03 \x03(\x0b\x32\'.SanProto.TransferArenaBattleRecordInfo\"\xa0\x02\n\x1dTransferArenaBattleRecordInfo\x12\r\n\x05index\x18\x01 \x02(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x04\x12\x0c\n\x04name\x18\x03 \x01(\x0c\x12\r\n\x05level\x18\x04 \x01(\x05\x12\x0f\n\x07icon_id\x18\x05 \x01(\x05\x12>\n\x06status\x18\x06 \x01(\x0e\x32..SanProto.TransferArenaBattleRecordInfo.STATUS\x12\x11\n\tself_rank\x18\x07 \x01(\x05\x12\x12\n\nrival_rank\x18\x08 \x01(\x05\"J\n\x06STATUS\x12\x0e\n\nATTACK_WIN\x10\x01\x12\x0f\n\x0b\x41TTACK_LOSE\x10\x02\x12\x0e\n\nDEFEND_WIN\x10\x03\x12\x0f\n\x0b\x44\x45\x46\x45ND_LOSE\x10\x04\"\x17\n\x15QueryTransferArenaReq\"X\n\x15QueryTransferArenaRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12/\n\narena_info\x18\x02 \x01(\x0b\x32\x1b.SanProto.TransferArenaInfo\"\x16\n\x14\x42uyChallengeTimesReq\"\xe6\x01\n\x14\x42uyChallengeTimesRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12/\n\x03ret\x18\x02 \x01(\x0e\x32\".SanProto.BuyChallengeTimesRes.RET\x12/\n\narena_info\x18\x03 \x01(\x0b\x32\x1b.SanProto.TransferArenaInfo\x12(\n\x08resource\x18\x04 \x01(\x0b\x32\x16.SanProto.ResourceInfo\"2\n\x03RET\x12\x06\n\x02OK\x10\x00\x12\x12\n\x0eNO_ENOUGH_GOLD\x10\x01\x12\x0f\n\x0bUPPER_LIMIT\x10\x02\"\x0c\n\nResetCDReq\"\xc1\x01\n\nResetCDRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12%\n\x03ret\x18\x02 \x01(\x0e\x32\x18.SanProto.ResetCDRes.RET\x12/\n\narena_info\x18\x03 \x01(\x0b\x32\x1b.SanProto.TransferArenaInfo\x12(\n\x08resource\x18\x04 \x01(\x0b\x32\x16.SanProto.ResourceInfo\"!\n\x03RET\x12\x06\n\x02OK\x10\x00\x12\x12\n\x0eNO_ENOUGH_GOLD\x10\x01\"0\n\x1bStartTransferArenaBattleReq\x12\x11\n\ttarget_id\x18\x01 \x02(\x04\"\xab\x01\n\x1bStartTransferArenaBattleRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12\x36\n\x03ret\x18\x02 \x01(\x0e\x32).SanProto.StartTransferArenaBattleRes.RET\"D\n\x03RET\x12\x06\n\x02OK\x10\x00\x12\x16\n\x12NO_CHALLENGE_TIMES\x10\x01\x12\x0b\n\x07\x43OOLING\x10\x02\x12\x10\n\x0cTARGET_ERROR\x10\x03\"]\n\x1c\x46inishTransferArenaBattleReq\x12*\n\x06\x62\x61ttle\x18\x01 \x01(\x0b\x32\x1a.SanProto.BattleOutputInfo\x12\x11\n\ttarget_id\x18\x02 \x01(\x04\"\x88\x01\n\x1c\x46inishTransferArenaBattleRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12\x37\n\x03ret\x18\x02 \x01(\x0e\x32*.SanProto.FinishTransferArenaBattleRes.RET\"\x1f\n\x03RET\x12\x06\n\x02OK\x10\x00\x12\x10\n\x0cTARGET_ERROR\x10\x01\":\n\x16TransferArenaRewardReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12\x0f\n\x07ranking\x18\x02 \x02(\x05\"(\n\x16TransferArenaRewardRes\x12\x0e\n\x06status\x18\x01 \x02(\x05')
  ,
  dependencies=[resource_pb2.DESCRIPTOR,battle_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TRANSFERARENABATTLERECORDINFO_STATUS = _descriptor.EnumDescriptor(
  name='STATUS',
  full_name='SanProto.TransferArenaBattleRecordInfo.STATUS',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ATTACK_WIN', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ATTACK_LOSE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFEND_WIN', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFEND_LOSE', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=401,
  serialized_end=475,
)
_sym_db.RegisterEnumDescriptor(_TRANSFERARENABATTLERECORDINFO_STATUS)

_BUYCHALLENGETIMESRES_RET = _descriptor.EnumDescriptor(
  name='RET',
  full_name='SanProto.BuyChallengeTimesRes.RET',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ENOUGH_GOLD', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPPER_LIMIT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=797,
  serialized_end=847,
)
_sym_db.RegisterEnumDescriptor(_BUYCHALLENGETIMESRES_RET)

_RESETCDRES_RET = _descriptor.EnumDescriptor(
  name='RET',
  full_name='SanProto.ResetCDRes.RET',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ENOUGH_GOLD', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=797,
  serialized_end=830,
)
_sym_db.RegisterEnumDescriptor(_RESETCDRES_RET)

_STARTTRANSFERARENABATTLERES_RET = _descriptor.EnumDescriptor(
  name='RET',
  full_name='SanProto.StartTransferArenaBattleRes.RET',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_CHALLENGE_TIMES', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COOLING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_ERROR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1213,
  serialized_end=1281,
)
_sym_db.RegisterEnumDescriptor(_STARTTRANSFERARENABATTLERES_RET)

_FINISHTRANSFERARENABATTLERES_RET = _descriptor.EnumDescriptor(
  name='RET',
  full_name='SanProto.FinishTransferArenaBattleRes.RET',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_ERROR', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1484,
  serialized_end=1515,
)
_sym_db.RegisterEnumDescriptor(_FINISHTRANSFERARENABATTLERES_RET)


_TRANSFERARENAINFO = _descriptor.Descriptor(
  name='TransferArenaInfo',
  full_name='SanProto.TransferArenaInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remain_times', full_name='SanProto.TransferArenaInfo.remain_times', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cd_end_time', full_name='SanProto.TransferArenaInfo.cd_end_time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='records', full_name='SanProto.TransferArenaInfo.records', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=64,
  serialized_end=184,
)


_TRANSFERARENABATTLERECORDINFO = _descriptor.Descriptor(
  name='TransferArenaBattleRecordInfo',
  full_name='SanProto.TransferArenaBattleRecordInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='SanProto.TransferArenaBattleRecordInfo.index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.TransferArenaBattleRecordInfo.user_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='SanProto.TransferArenaBattleRecordInfo.name', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='SanProto.TransferArenaBattleRecordInfo.level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon_id', full_name='SanProto.TransferArenaBattleRecordInfo.icon_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.TransferArenaBattleRecordInfo.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='self_rank', full_name='SanProto.TransferArenaBattleRecordInfo.self_rank', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rival_rank', full_name='SanProto.TransferArenaBattleRecordInfo.rival_rank', index=7,
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
    _TRANSFERARENABATTLERECORDINFO_STATUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=475,
)


_QUERYTRANSFERARENAREQ = _descriptor.Descriptor(
  name='QueryTransferArenaReq',
  full_name='SanProto.QueryTransferArenaReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=477,
  serialized_end=500,
)


_QUERYTRANSFERARENARES = _descriptor.Descriptor(
  name='QueryTransferArenaRes',
  full_name='SanProto.QueryTransferArenaRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.QueryTransferArenaRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arena_info', full_name='SanProto.QueryTransferArenaRes.arena_info', index=1,
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
  serialized_start=502,
  serialized_end=590,
)


_BUYCHALLENGETIMESREQ = _descriptor.Descriptor(
  name='BuyChallengeTimesReq',
  full_name='SanProto.BuyChallengeTimesReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=592,
  serialized_end=614,
)


_BUYCHALLENGETIMESRES = _descriptor.Descriptor(
  name='BuyChallengeTimesRes',
  full_name='SanProto.BuyChallengeTimesRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.BuyChallengeTimesRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.BuyChallengeTimesRes.ret', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arena_info', full_name='SanProto.BuyChallengeTimesRes.arena_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.BuyChallengeTimesRes.resource', index=3,
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
    _BUYCHALLENGETIMESRES_RET,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=617,
  serialized_end=847,
)


_RESETCDREQ = _descriptor.Descriptor(
  name='ResetCDReq',
  full_name='SanProto.ResetCDReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=849,
  serialized_end=861,
)


_RESETCDRES = _descriptor.Descriptor(
  name='ResetCDRes',
  full_name='SanProto.ResetCDRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.ResetCDRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.ResetCDRes.ret', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arena_info', full_name='SanProto.ResetCDRes.arena_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.ResetCDRes.resource', index=3,
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
    _RESETCDRES_RET,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=864,
  serialized_end=1057,
)


_STARTTRANSFERARENABATTLEREQ = _descriptor.Descriptor(
  name='StartTransferArenaBattleReq',
  full_name='SanProto.StartTransferArenaBattleReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_id', full_name='SanProto.StartTransferArenaBattleReq.target_id', index=0,
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
  serialized_start=1059,
  serialized_end=1107,
)


_STARTTRANSFERARENABATTLERES = _descriptor.Descriptor(
  name='StartTransferArenaBattleRes',
  full_name='SanProto.StartTransferArenaBattleRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.StartTransferArenaBattleRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.StartTransferArenaBattleRes.ret', index=1,
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
    _STARTTRANSFERARENABATTLERES_RET,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1110,
  serialized_end=1281,
)


_FINISHTRANSFERARENABATTLEREQ = _descriptor.Descriptor(
  name='FinishTransferArenaBattleReq',
  full_name='SanProto.FinishTransferArenaBattleReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='battle', full_name='SanProto.FinishTransferArenaBattleReq.battle', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='SanProto.FinishTransferArenaBattleReq.target_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=1283,
  serialized_end=1376,
)


_FINISHTRANSFERARENABATTLERES = _descriptor.Descriptor(
  name='FinishTransferArenaBattleRes',
  full_name='SanProto.FinishTransferArenaBattleRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.FinishTransferArenaBattleRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ret', full_name='SanProto.FinishTransferArenaBattleRes.ret', index=1,
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
    _FINISHTRANSFERARENABATTLERES_RET,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1379,
  serialized_end=1515,
)


_TRANSFERARENAREWARDREQ = _descriptor.Descriptor(
  name='TransferArenaRewardReq',
  full_name='SanProto.TransferArenaRewardReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.TransferArenaRewardReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ranking', full_name='SanProto.TransferArenaRewardReq.ranking', index=1,
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
  serialized_start=1517,
  serialized_end=1575,
)


_TRANSFERARENAREWARDRES = _descriptor.Descriptor(
  name='TransferArenaRewardRes',
  full_name='SanProto.TransferArenaRewardRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.TransferArenaRewardRes.status', index=0,
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
  serialized_start=1577,
  serialized_end=1617,
)

_TRANSFERARENAINFO.fields_by_name['records'].message_type = _TRANSFERARENABATTLERECORDINFO
_TRANSFERARENABATTLERECORDINFO.fields_by_name['status'].enum_type = _TRANSFERARENABATTLERECORDINFO_STATUS
_TRANSFERARENABATTLERECORDINFO_STATUS.containing_type = _TRANSFERARENABATTLERECORDINFO
_QUERYTRANSFERARENARES.fields_by_name['arena_info'].message_type = _TRANSFERARENAINFO
_BUYCHALLENGETIMESRES.fields_by_name['ret'].enum_type = _BUYCHALLENGETIMESRES_RET
_BUYCHALLENGETIMESRES.fields_by_name['arena_info'].message_type = _TRANSFERARENAINFO
_BUYCHALLENGETIMESRES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_BUYCHALLENGETIMESRES_RET.containing_type = _BUYCHALLENGETIMESRES
_RESETCDRES.fields_by_name['ret'].enum_type = _RESETCDRES_RET
_RESETCDRES.fields_by_name['arena_info'].message_type = _TRANSFERARENAINFO
_RESETCDRES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_RESETCDRES_RET.containing_type = _RESETCDRES
_STARTTRANSFERARENABATTLERES.fields_by_name['ret'].enum_type = _STARTTRANSFERARENABATTLERES_RET
_STARTTRANSFERARENABATTLERES_RET.containing_type = _STARTTRANSFERARENABATTLERES
_FINISHTRANSFERARENABATTLEREQ.fields_by_name['battle'].message_type = battle_pb2._BATTLEOUTPUTINFO
_FINISHTRANSFERARENABATTLERES.fields_by_name['ret'].enum_type = _FINISHTRANSFERARENABATTLERES_RET
_FINISHTRANSFERARENABATTLERES_RET.containing_type = _FINISHTRANSFERARENABATTLERES
DESCRIPTOR.message_types_by_name['TransferArenaInfo'] = _TRANSFERARENAINFO
DESCRIPTOR.message_types_by_name['TransferArenaBattleRecordInfo'] = _TRANSFERARENABATTLERECORDINFO
DESCRIPTOR.message_types_by_name['QueryTransferArenaReq'] = _QUERYTRANSFERARENAREQ
DESCRIPTOR.message_types_by_name['QueryTransferArenaRes'] = _QUERYTRANSFERARENARES
DESCRIPTOR.message_types_by_name['BuyChallengeTimesReq'] = _BUYCHALLENGETIMESREQ
DESCRIPTOR.message_types_by_name['BuyChallengeTimesRes'] = _BUYCHALLENGETIMESRES
DESCRIPTOR.message_types_by_name['ResetCDReq'] = _RESETCDREQ
DESCRIPTOR.message_types_by_name['ResetCDRes'] = _RESETCDRES
DESCRIPTOR.message_types_by_name['StartTransferArenaBattleReq'] = _STARTTRANSFERARENABATTLEREQ
DESCRIPTOR.message_types_by_name['StartTransferArenaBattleRes'] = _STARTTRANSFERARENABATTLERES
DESCRIPTOR.message_types_by_name['FinishTransferArenaBattleReq'] = _FINISHTRANSFERARENABATTLEREQ
DESCRIPTOR.message_types_by_name['FinishTransferArenaBattleRes'] = _FINISHTRANSFERARENABATTLERES
DESCRIPTOR.message_types_by_name['TransferArenaRewardReq'] = _TRANSFERARENAREWARDREQ
DESCRIPTOR.message_types_by_name['TransferArenaRewardRes'] = _TRANSFERARENAREWARDRES

TransferArenaInfo = _reflection.GeneratedProtocolMessageType('TransferArenaInfo', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERARENAINFO,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.TransferArenaInfo)
  ))
_sym_db.RegisterMessage(TransferArenaInfo)

TransferArenaBattleRecordInfo = _reflection.GeneratedProtocolMessageType('TransferArenaBattleRecordInfo', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERARENABATTLERECORDINFO,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.TransferArenaBattleRecordInfo)
  ))
_sym_db.RegisterMessage(TransferArenaBattleRecordInfo)

QueryTransferArenaReq = _reflection.GeneratedProtocolMessageType('QueryTransferArenaReq', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTRANSFERARENAREQ,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.QueryTransferArenaReq)
  ))
_sym_db.RegisterMessage(QueryTransferArenaReq)

QueryTransferArenaRes = _reflection.GeneratedProtocolMessageType('QueryTransferArenaRes', (_message.Message,), dict(
  DESCRIPTOR = _QUERYTRANSFERARENARES,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.QueryTransferArenaRes)
  ))
_sym_db.RegisterMessage(QueryTransferArenaRes)

BuyChallengeTimesReq = _reflection.GeneratedProtocolMessageType('BuyChallengeTimesReq', (_message.Message,), dict(
  DESCRIPTOR = _BUYCHALLENGETIMESREQ,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.BuyChallengeTimesReq)
  ))
_sym_db.RegisterMessage(BuyChallengeTimesReq)

BuyChallengeTimesRes = _reflection.GeneratedProtocolMessageType('BuyChallengeTimesRes', (_message.Message,), dict(
  DESCRIPTOR = _BUYCHALLENGETIMESRES,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.BuyChallengeTimesRes)
  ))
_sym_db.RegisterMessage(BuyChallengeTimesRes)

ResetCDReq = _reflection.GeneratedProtocolMessageType('ResetCDReq', (_message.Message,), dict(
  DESCRIPTOR = _RESETCDREQ,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ResetCDReq)
  ))
_sym_db.RegisterMessage(ResetCDReq)

ResetCDRes = _reflection.GeneratedProtocolMessageType('ResetCDRes', (_message.Message,), dict(
  DESCRIPTOR = _RESETCDRES,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ResetCDRes)
  ))
_sym_db.RegisterMessage(ResetCDRes)

StartTransferArenaBattleReq = _reflection.GeneratedProtocolMessageType('StartTransferArenaBattleReq', (_message.Message,), dict(
  DESCRIPTOR = _STARTTRANSFERARENABATTLEREQ,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.StartTransferArenaBattleReq)
  ))
_sym_db.RegisterMessage(StartTransferArenaBattleReq)

StartTransferArenaBattleRes = _reflection.GeneratedProtocolMessageType('StartTransferArenaBattleRes', (_message.Message,), dict(
  DESCRIPTOR = _STARTTRANSFERARENABATTLERES,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.StartTransferArenaBattleRes)
  ))
_sym_db.RegisterMessage(StartTransferArenaBattleRes)

FinishTransferArenaBattleReq = _reflection.GeneratedProtocolMessageType('FinishTransferArenaBattleReq', (_message.Message,), dict(
  DESCRIPTOR = _FINISHTRANSFERARENABATTLEREQ,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.FinishTransferArenaBattleReq)
  ))
_sym_db.RegisterMessage(FinishTransferArenaBattleReq)

FinishTransferArenaBattleRes = _reflection.GeneratedProtocolMessageType('FinishTransferArenaBattleRes', (_message.Message,), dict(
  DESCRIPTOR = _FINISHTRANSFERARENABATTLERES,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.FinishTransferArenaBattleRes)
  ))
_sym_db.RegisterMessage(FinishTransferArenaBattleRes)

TransferArenaRewardReq = _reflection.GeneratedProtocolMessageType('TransferArenaRewardReq', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERARENAREWARDREQ,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.TransferArenaRewardReq)
  ))
_sym_db.RegisterMessage(TransferArenaRewardReq)

TransferArenaRewardRes = _reflection.GeneratedProtocolMessageType('TransferArenaRewardRes', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERARENAREWARDRES,
  __module__ = 'transfer_arena_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.TransferArenaRewardRes)
  ))
_sym_db.RegisterMessage(TransferArenaRewardRes)


# @@protoc_insertion_point(module_scope)
