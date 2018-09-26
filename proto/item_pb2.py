# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: item.proto

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
import energy_pb2
import monarch_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='item.proto',
  package='SanProto',
  serialized_pb=_b('\n\nitem.proto\x12\x08SanProto\x1a\x0eresource.proto\x1a\x0c\x65nergy.proto\x1a\rmonarch.proto\")\n\x08ItemInfo\x12\x10\n\x08\x62\x61sic_id\x18\x01 \x02(\x05\x12\x0b\n\x03num\x18\x02 \x02(\x05\"J\n\x15UseItemForResourceReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12 \n\x04item\x18\x03 \x03(\x0b\x32\x12.SanProto.ItemInfo\"|\n\x15UseItemForResourceRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12(\n\x08resource\x18\x02 \x01(\x0b\x32\x16.SanProto.ResourceInfo\x12)\n\x0b\x65nergy_info\x18\x03 \x01(\x0b\x32\x14.SanProto.EnergyInfo\"g\n\nUseItemReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12&\n\x07monarch\x18\x02 \x01(\x0b\x32\x15.SanProto.MonarchInfo\x12 \n\x04item\x18\x03 \x03(\x0b\x32\x12.SanProto.ItemInfo\"q\n\nUseItemRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12(\n\x08resource\x18\x02 \x01(\x0b\x32\x16.SanProto.ResourceInfo\x12)\n\x0b\x65nergy_info\x18\x03 \x01(\x0b\x32\x14.SanProto.EnergyInfo\"m\n\x0f\x43omposeItemsReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12 \n\x04item\x18\x02 \x02(\x0b\x32\x12.SanProto.ItemInfo\x12\'\n\x0bitem_source\x18\x03 \x03(\x0b\x32\x12.SanProto.ItemInfo\"K\n\x0f\x43omposeItemsRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12(\n\x08resource\x18\x02 \x01(\x0b\x32\x16.SanProto.ResourceInfo\"n\n\x11UpgradeMonarchReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12&\n\x07monarch\x18\x02 \x02(\x0b\x32\x15.SanProto.MonarchInfo\x12 \n\x04item\x18\x03 \x02(\x0b\x32\x12.SanProto.ItemInfo\"#\n\x11UpgradeMonarchRes\x12\x0e\n\x06status\x18\x01 \x02(\x05')
  ,
  dependencies=[resource_pb2.DESCRIPTOR,energy_pb2.DESCRIPTOR,monarch_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ITEMINFO = _descriptor.Descriptor(
  name='ItemInfo',
  full_name='SanProto.ItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='basic_id', full_name='SanProto.ItemInfo.basic_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num', full_name='SanProto.ItemInfo.num', index=1,
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
  serialized_start=69,
  serialized_end=110,
)


_USEITEMFORRESOURCEREQ = _descriptor.Descriptor(
  name='UseItemForResourceReq',
  full_name='SanProto.UseItemForResourceReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.UseItemForResourceReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='SanProto.UseItemForResourceReq.item', index=1,
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
  serialized_start=112,
  serialized_end=186,
)


_USEITEMFORRESOURCERES = _descriptor.Descriptor(
  name='UseItemForResourceRes',
  full_name='SanProto.UseItemForResourceRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.UseItemForResourceRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.UseItemForResourceRes.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='energy_info', full_name='SanProto.UseItemForResourceRes.energy_info', index=2,
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
  serialized_start=188,
  serialized_end=312,
)


_USEITEMREQ = _descriptor.Descriptor(
  name='UseItemReq',
  full_name='SanProto.UseItemReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.UseItemReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='monarch', full_name='SanProto.UseItemReq.monarch', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='SanProto.UseItemReq.item', index=2,
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
  serialized_start=314,
  serialized_end=417,
)


_USEITEMRES = _descriptor.Descriptor(
  name='UseItemRes',
  full_name='SanProto.UseItemRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.UseItemRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.UseItemRes.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='energy_info', full_name='SanProto.UseItemRes.energy_info', index=2,
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
  serialized_start=419,
  serialized_end=532,
)


_COMPOSEITEMSREQ = _descriptor.Descriptor(
  name='ComposeItemsReq',
  full_name='SanProto.ComposeItemsReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.ComposeItemsReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='SanProto.ComposeItemsReq.item', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_source', full_name='SanProto.ComposeItemsReq.item_source', index=2,
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
  serialized_start=534,
  serialized_end=643,
)


_COMPOSEITEMSRES = _descriptor.Descriptor(
  name='ComposeItemsRes',
  full_name='SanProto.ComposeItemsRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.ComposeItemsRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.ComposeItemsRes.resource', index=1,
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
  serialized_start=645,
  serialized_end=720,
)


_UPGRADEMONARCHREQ = _descriptor.Descriptor(
  name='UpgradeMonarchReq',
  full_name='SanProto.UpgradeMonarchReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.UpgradeMonarchReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='monarch', full_name='SanProto.UpgradeMonarchReq.monarch', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='SanProto.UpgradeMonarchReq.item', index=2,
      number=3, type=11, cpp_type=10, label=2,
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
  serialized_start=722,
  serialized_end=832,
)


_UPGRADEMONARCHRES = _descriptor.Descriptor(
  name='UpgradeMonarchRes',
  full_name='SanProto.UpgradeMonarchRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.UpgradeMonarchRes.status', index=0,
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
  serialized_start=834,
  serialized_end=869,
)

_USEITEMFORRESOURCEREQ.fields_by_name['item'].message_type = _ITEMINFO
_USEITEMFORRESOURCERES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_USEITEMFORRESOURCERES.fields_by_name['energy_info'].message_type = energy_pb2._ENERGYINFO
_USEITEMREQ.fields_by_name['monarch'].message_type = monarch_pb2._MONARCHINFO
_USEITEMREQ.fields_by_name['item'].message_type = _ITEMINFO
_USEITEMRES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_USEITEMRES.fields_by_name['energy_info'].message_type = energy_pb2._ENERGYINFO
_COMPOSEITEMSREQ.fields_by_name['item'].message_type = _ITEMINFO
_COMPOSEITEMSREQ.fields_by_name['item_source'].message_type = _ITEMINFO
_COMPOSEITEMSRES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
_UPGRADEMONARCHREQ.fields_by_name['monarch'].message_type = monarch_pb2._MONARCHINFO
_UPGRADEMONARCHREQ.fields_by_name['item'].message_type = _ITEMINFO
DESCRIPTOR.message_types_by_name['ItemInfo'] = _ITEMINFO
DESCRIPTOR.message_types_by_name['UseItemForResourceReq'] = _USEITEMFORRESOURCEREQ
DESCRIPTOR.message_types_by_name['UseItemForResourceRes'] = _USEITEMFORRESOURCERES
DESCRIPTOR.message_types_by_name['UseItemReq'] = _USEITEMREQ
DESCRIPTOR.message_types_by_name['UseItemRes'] = _USEITEMRES
DESCRIPTOR.message_types_by_name['ComposeItemsReq'] = _COMPOSEITEMSREQ
DESCRIPTOR.message_types_by_name['ComposeItemsRes'] = _COMPOSEITEMSRES
DESCRIPTOR.message_types_by_name['UpgradeMonarchReq'] = _UPGRADEMONARCHREQ
DESCRIPTOR.message_types_by_name['UpgradeMonarchRes'] = _UPGRADEMONARCHRES

ItemInfo = _reflection.GeneratedProtocolMessageType('ItemInfo', (_message.Message,), dict(
  DESCRIPTOR = _ITEMINFO,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ItemInfo)
  ))
_sym_db.RegisterMessage(ItemInfo)

UseItemForResourceReq = _reflection.GeneratedProtocolMessageType('UseItemForResourceReq', (_message.Message,), dict(
  DESCRIPTOR = _USEITEMFORRESOURCEREQ,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UseItemForResourceReq)
  ))
_sym_db.RegisterMessage(UseItemForResourceReq)

UseItemForResourceRes = _reflection.GeneratedProtocolMessageType('UseItemForResourceRes', (_message.Message,), dict(
  DESCRIPTOR = _USEITEMFORRESOURCERES,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UseItemForResourceRes)
  ))
_sym_db.RegisterMessage(UseItemForResourceRes)

UseItemReq = _reflection.GeneratedProtocolMessageType('UseItemReq', (_message.Message,), dict(
  DESCRIPTOR = _USEITEMREQ,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UseItemReq)
  ))
_sym_db.RegisterMessage(UseItemReq)

UseItemRes = _reflection.GeneratedProtocolMessageType('UseItemRes', (_message.Message,), dict(
  DESCRIPTOR = _USEITEMRES,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UseItemRes)
  ))
_sym_db.RegisterMessage(UseItemRes)

ComposeItemsReq = _reflection.GeneratedProtocolMessageType('ComposeItemsReq', (_message.Message,), dict(
  DESCRIPTOR = _COMPOSEITEMSREQ,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ComposeItemsReq)
  ))
_sym_db.RegisterMessage(ComposeItemsReq)

ComposeItemsRes = _reflection.GeneratedProtocolMessageType('ComposeItemsRes', (_message.Message,), dict(
  DESCRIPTOR = _COMPOSEITEMSRES,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ComposeItemsRes)
  ))
_sym_db.RegisterMessage(ComposeItemsRes)

UpgradeMonarchReq = _reflection.GeneratedProtocolMessageType('UpgradeMonarchReq', (_message.Message,), dict(
  DESCRIPTOR = _UPGRADEMONARCHREQ,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpgradeMonarchReq)
  ))
_sym_db.RegisterMessage(UpgradeMonarchReq)

UpgradeMonarchRes = _reflection.GeneratedProtocolMessageType('UpgradeMonarchRes', (_message.Message,), dict(
  DESCRIPTOR = _UPGRADEMONARCHRES,
  __module__ = 'item_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UpgradeMonarchRes)
  ))
_sym_db.RegisterMessage(UpgradeMonarchRes)


# @@protoc_insertion_point(module_scope)
