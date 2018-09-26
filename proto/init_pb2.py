# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: init.proto

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
import city_pb2
import hero_pb2
import team_pb2
import technology_pb2
import mission_pb2
import building_pb2
import conscript_pb2
import mail_pb2
import user_pb2
import node_pb2
import wineShop_pb2
import guide_pb2
import arena_pb2
import dungeon_pb2
import energy_pb2
import pray_pb2
import chest_pb2
import union_pb2
import anneal_pb2
import boss_pb2
import activity_pb2
import tips_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='init.proto',
  package='SanProto',
  serialized_pb=_b('\n\ninit.proto\x12\x08SanProto\x1a\rmonarch.proto\x1a\x0eresource.proto\x1a\nitem.proto\x1a\ncity.proto\x1a\nhero.proto\x1a\nteam.proto\x1a\x10technology.proto\x1a\rmission.proto\x1a\x0e\x62uilding.proto\x1a\x0f\x63onscript.proto\x1a\nmail.proto\x1a\nuser.proto\x1a\nnode.proto\x1a\x0ewineShop.proto\x1a\x0bguide.proto\x1a\x0b\x61rena.proto\x1a\rdungeon.proto\x1a\x0c\x65nergy.proto\x1a\npray.proto\x1a\x0b\x63hest.proto\x1a\x0bunion.proto\x1a\x0c\x61nneal.proto\x1a\nboss.proto\x1a\x0e\x61\x63tivity.proto\x1a\ntips.proto\":\n\x08LoginReq\x12\x0c\n\x04name\x18\x01 \x02(\x0c\x12\x10\n\x08password\x18\x02 \x02(\x0c\x12\x0e\n\x06region\x18\x03 \x02(\x05\"+\n\x08LoginRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x04\"*\n\x04\x46lag\x12\x11\n\tflag_name\x18\x01 \x02(\x0c\x12\x0f\n\x07is_open\x18\x02 \x01(\x08\"\xdd\t\n\x08InitInfo\x12&\n\x07monarch\x18\x01 \x02(\x0b\x32\x15.SanProto.MonarchInfo\x12(\n\x08resource\x18\x02 \x02(\x0b\x32\x16.SanProto.ResourceInfo\x12!\n\x05items\x18\x03 \x03(\x0b\x32\x12.SanProto.ItemInfo\x12\"\n\x06heroes\x18\x04 \x03(\x0b\x32\x12.SanProto.HeroInfo\x12!\n\x05teams\x18\x05 \x03(\x0b\x32\x12.SanProto.TeamInfo\x12\x1e\n\x03map\x18\x06 \x02(\x0b\x32\x11.SanProto.MapInfo\x12\"\n\x06\x63ities\x18\x07 \x03(\x0b\x32\x12.SanProto.CityInfo\x12)\n\tbuildings\x18\x08 \x03(\x0b\x32\x16.SanProto.BuildingInfo\x12\'\n\x05techs\x18\t \x03(\x0b\x32\x18.SanProto.TechnologyInfo\x12+\n\nconscripts\x18\n \x03(\x0b\x32\x17.SanProto.ConscriptInfo\x12\'\n\x08missions\x18\x0c \x03(\x0b\x32\x15.SanProto.MissionInfo\x12!\n\x05mails\x18\r \x03(\x0b\x32\x12.SanProto.MailInfo\x12%\n\x07sign_in\x18\x0e \x01(\x0b\x32\x14.SanProto.SignInInfo\x12&\n\nmoney_draw\x18\x10 \x01(\x0b\x32\x12.SanProto.DrawInfo\x12%\n\tgold_draw\x18\x11 \x01(\x0b\x32\x12.SanProto.DrawInfo\x12\"\n\x05guide\x18\x12 \x01(\x0b\x32\x13.SanProto.GuideInfo\x12\"\n\x05\x61rena\x18\x13 \x01(\x0b\x32\x13.SanProto.ArenaInfo\x12&\n\x07\x64ungeon\x18\x14 \x01(\x0b\x32\x15.SanProto.DungeonInfo\x12)\n\x0b\x65nergy_info\x18\x15 \x01(\x0b\x32\x14.SanProto.EnergyInfo\x12 \n\x04pray\x18\x16 \x01(\x0b\x32\x12.SanProto.PrayInfo\x12\"\n\x05\x63hest\x18\x17 \x01(\x0b\x32\x13.SanProto.ChestInfo\x12;\n\x12union_battle_stage\x18\x18 \x01(\x0e\x32\x1f.SanProto.UnionBattleInfo.STAGE\x12$\n\x06\x61nneal\x18\x19 \x01(\x0b\x32\x14.SanProto.AnnealInfo\x12\x11\n\thero_star\x18\x1a \x03(\x05\x12+\n\nworld_boss\x18\x1b \x01(\x0b\x32\x17.SanProto.WorldBossInfo\x12(\n\x0bmelee_arena\x18\x1c \x01(\x0b\x32\x13.SanProto.ArenaInfo\x12&\n\nmelee_team\x18\x1d \x01(\x0b\x32\x12.SanProto.TeamInfo\x12\x1d\n\x05\x66lags\x18  \x03(\x0b\x32\x0e.SanProto.Flag\x12*\n\nactivities\x18! \x03(\x0b\x32\x16.SanProto.ActivityInfo\x12\x34\n\x0f\x65xpand_dungeons\x18\" \x03(\x0b\x32\x1b.SanProto.ExpandDungeonInfo\x12\x0c\n\x04luas\x18# \x03(\x0c\x12)\n\x0b\x62utton_tips\x18$ \x03(\x0b\x32\x14.SanProto.ButtonTips\"\xa9\x01\n\x07InitReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12\x0f\n\x07version\x18\x02 \x01(\x0c\x12\x0c\n\x04\x63uid\x18\x03 \x01(\x0c\x12\x10\n\x08platform\x18\x04 \x01(\x0c\x12\x13\n\x0b\x64\x65vice_type\x18\x05 \x01(\x0c\x12\x11\n\tdevice_id\x18\x06 \x01(\x0c\x12\x14\n\x0cnetwork_type\x18\x07 \x01(\x0c\x12\n\n\x02os\x18\x08 \x01(\x0c\x12\x12\n\nchannel_id\x18\t \x01(\x0c\"O\n\x07InitRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12 \n\x04info\x18\x02 \x01(\x0b\x32\x12.SanProto.InitInfo\x12\x12\n\nfirst_init\x18\x03 \x01(\x08')
  ,
  dependencies=[monarch_pb2.DESCRIPTOR,resource_pb2.DESCRIPTOR,item_pb2.DESCRIPTOR,city_pb2.DESCRIPTOR,hero_pb2.DESCRIPTOR,team_pb2.DESCRIPTOR,technology_pb2.DESCRIPTOR,mission_pb2.DESCRIPTOR,building_pb2.DESCRIPTOR,conscript_pb2.DESCRIPTOR,mail_pb2.DESCRIPTOR,user_pb2.DESCRIPTOR,node_pb2.DESCRIPTOR,wineShop_pb2.DESCRIPTOR,guide_pb2.DESCRIPTOR,arena_pb2.DESCRIPTOR,dungeon_pb2.DESCRIPTOR,energy_pb2.DESCRIPTOR,pray_pb2.DESCRIPTOR,chest_pb2.DESCRIPTOR,union_pb2.DESCRIPTOR,anneal_pb2.DESCRIPTOR,boss_pb2.DESCRIPTOR,activity_pb2.DESCRIPTOR,tips_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LOGINREQ = _descriptor.Descriptor(
  name='LoginReq',
  full_name='SanProto.LoginReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SanProto.LoginReq.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='SanProto.LoginReq.password', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='region', full_name='SanProto.LoginReq.region', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=368,
  serialized_end=426,
)


_LOGINRES = _descriptor.Descriptor(
  name='LoginRes',
  full_name='SanProto.LoginRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.LoginRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.LoginRes.user_id', index=1,
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
  serialized_start=428,
  serialized_end=471,
)


_FLAG = _descriptor.Descriptor(
  name='Flag',
  full_name='SanProto.Flag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='flag_name', full_name='SanProto.Flag.flag_name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_open', full_name='SanProto.Flag.is_open', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=473,
  serialized_end=515,
)


_INITINFO = _descriptor.Descriptor(
  name='InitInfo',
  full_name='SanProto.InitInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='monarch', full_name='SanProto.InitInfo.monarch', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.InitInfo.resource', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='SanProto.InitInfo.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heroes', full_name='SanProto.InitInfo.heroes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='teams', full_name='SanProto.InitInfo.teams', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map', full_name='SanProto.InitInfo.map', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cities', full_name='SanProto.InitInfo.cities', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buildings', full_name='SanProto.InitInfo.buildings', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='techs', full_name='SanProto.InitInfo.techs', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conscripts', full_name='SanProto.InitInfo.conscripts', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='missions', full_name='SanProto.InitInfo.missions', index=10,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mails', full_name='SanProto.InitInfo.mails', index=11,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sign_in', full_name='SanProto.InitInfo.sign_in', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='money_draw', full_name='SanProto.InitInfo.money_draw', index=13,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold_draw', full_name='SanProto.InitInfo.gold_draw', index=14,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guide', full_name='SanProto.InitInfo.guide', index=15,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arena', full_name='SanProto.InitInfo.arena', index=16,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dungeon', full_name='SanProto.InitInfo.dungeon', index=17,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='energy_info', full_name='SanProto.InitInfo.energy_info', index=18,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pray', full_name='SanProto.InitInfo.pray', index=19,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chest', full_name='SanProto.InitInfo.chest', index=20,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='union_battle_stage', full_name='SanProto.InitInfo.union_battle_stage', index=21,
      number=24, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='anneal', full_name='SanProto.InitInfo.anneal', index=22,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_star', full_name='SanProto.InitInfo.hero_star', index=23,
      number=26, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='world_boss', full_name='SanProto.InitInfo.world_boss', index=24,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='melee_arena', full_name='SanProto.InitInfo.melee_arena', index=25,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='melee_team', full_name='SanProto.InitInfo.melee_team', index=26,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='SanProto.InitInfo.flags', index=27,
      number=32, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activities', full_name='SanProto.InitInfo.activities', index=28,
      number=33, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expand_dungeons', full_name='SanProto.InitInfo.expand_dungeons', index=29,
      number=34, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='luas', full_name='SanProto.InitInfo.luas', index=30,
      number=35, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='button_tips', full_name='SanProto.InitInfo.button_tips', index=31,
      number=36, type=11, cpp_type=10, label=3,
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
  serialized_start=518,
  serialized_end=1763,
)


_INITREQ = _descriptor.Descriptor(
  name='InitReq',
  full_name='SanProto.InitReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.InitReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='SanProto.InitReq.version', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cuid', full_name='SanProto.InitReq.cuid', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform', full_name='SanProto.InitReq.platform', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='SanProto.InitReq.device_type', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='SanProto.InitReq.device_id', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='network_type', full_name='SanProto.InitReq.network_type', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='os', full_name='SanProto.InitReq.os', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='SanProto.InitReq.channel_id', index=8,
      number=9, type=12, cpp_type=9, label=1,
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
  serialized_start=1766,
  serialized_end=1935,
)


_INITRES = _descriptor.Descriptor(
  name='InitRes',
  full_name='SanProto.InitRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.InitRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='SanProto.InitRes.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_init', full_name='SanProto.InitRes.first_init', index=2,
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
  serialized_start=1937,
  serialized_end=2016,
)

_INITINFO.fields_by_name['monarch'].message_type = monarch_pb2._MONARCHINFO
_INITINFO.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_INITINFO.fields_by_name['items'].message_type = item_pb2._ITEMINFO
_INITINFO.fields_by_name['heroes'].message_type = hero_pb2._HEROINFO
_INITINFO.fields_by_name['teams'].message_type = team_pb2._TEAMINFO
_INITINFO.fields_by_name['map'].message_type = node_pb2._MAPINFO
_INITINFO.fields_by_name['cities'].message_type = city_pb2._CITYINFO
_INITINFO.fields_by_name['buildings'].message_type = building_pb2._BUILDINGINFO
_INITINFO.fields_by_name['techs'].message_type = technology_pb2._TECHNOLOGYINFO
_INITINFO.fields_by_name['conscripts'].message_type = conscript_pb2._CONSCRIPTINFO
_INITINFO.fields_by_name['missions'].message_type = mission_pb2._MISSIONINFO
_INITINFO.fields_by_name['mails'].message_type = mail_pb2._MAILINFO
_INITINFO.fields_by_name['sign_in'].message_type = user_pb2._SIGNININFO
_INITINFO.fields_by_name['money_draw'].message_type = wineShop_pb2._DRAWINFO
_INITINFO.fields_by_name['gold_draw'].message_type = wineShop_pb2._DRAWINFO
_INITINFO.fields_by_name['guide'].message_type = guide_pb2._GUIDEINFO
_INITINFO.fields_by_name['arena'].message_type = arena_pb2._ARENAINFO
_INITINFO.fields_by_name['dungeon'].message_type = dungeon_pb2._DUNGEONINFO
_INITINFO.fields_by_name['energy_info'].message_type = energy_pb2._ENERGYINFO
_INITINFO.fields_by_name['pray'].message_type = pray_pb2._PRAYINFO
_INITINFO.fields_by_name['chest'].message_type = chest_pb2._CHESTINFO
_INITINFO.fields_by_name['union_battle_stage'].enum_type = union_pb2._UNIONBATTLEINFO_STAGE
_INITINFO.fields_by_name['anneal'].message_type = anneal_pb2._ANNEALINFO
_INITINFO.fields_by_name['world_boss'].message_type = boss_pb2._WORLDBOSSINFO
_INITINFO.fields_by_name['melee_arena'].message_type = arena_pb2._ARENAINFO
_INITINFO.fields_by_name['melee_team'].message_type = team_pb2._TEAMINFO
_INITINFO.fields_by_name['flags'].message_type = _FLAG
_INITINFO.fields_by_name['activities'].message_type = activity_pb2._ACTIVITYINFO
_INITINFO.fields_by_name['expand_dungeons'].message_type = dungeon_pb2._EXPANDDUNGEONINFO
_INITINFO.fields_by_name['button_tips'].message_type = tips_pb2._BUTTONTIPS
_INITRES.fields_by_name['info'].message_type = _INITINFO
DESCRIPTOR.message_types_by_name['LoginReq'] = _LOGINREQ
DESCRIPTOR.message_types_by_name['LoginRes'] = _LOGINRES
DESCRIPTOR.message_types_by_name['Flag'] = _FLAG
DESCRIPTOR.message_types_by_name['InitInfo'] = _INITINFO
DESCRIPTOR.message_types_by_name['InitReq'] = _INITREQ
DESCRIPTOR.message_types_by_name['InitRes'] = _INITRES

LoginReq = _reflection.GeneratedProtocolMessageType('LoginReq', (_message.Message,), dict(
  DESCRIPTOR = _LOGINREQ,
  __module__ = 'init_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.LoginReq)
  ))
_sym_db.RegisterMessage(LoginReq)

LoginRes = _reflection.GeneratedProtocolMessageType('LoginRes', (_message.Message,), dict(
  DESCRIPTOR = _LOGINRES,
  __module__ = 'init_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.LoginRes)
  ))
_sym_db.RegisterMessage(LoginRes)

Flag = _reflection.GeneratedProtocolMessageType('Flag', (_message.Message,), dict(
  DESCRIPTOR = _FLAG,
  __module__ = 'init_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.Flag)
  ))
_sym_db.RegisterMessage(Flag)

InitInfo = _reflection.GeneratedProtocolMessageType('InitInfo', (_message.Message,), dict(
  DESCRIPTOR = _INITINFO,
  __module__ = 'init_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.InitInfo)
  ))
_sym_db.RegisterMessage(InitInfo)

InitReq = _reflection.GeneratedProtocolMessageType('InitReq', (_message.Message,), dict(
  DESCRIPTOR = _INITREQ,
  __module__ = 'init_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.InitReq)
  ))
_sym_db.RegisterMessage(InitReq)

InitRes = _reflection.GeneratedProtocolMessageType('InitRes', (_message.Message,), dict(
  DESCRIPTOR = _INITRES,
  __module__ = 'init_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.InitRes)
  ))
_sym_db.RegisterMessage(InitRes)


# @@protoc_insertion_point(module_scope)
