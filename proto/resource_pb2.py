# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: resource.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='resource.proto',
  package='SanProto',
  serialized_pb=_b('\n\x0eresource.proto\x12\x08SanProto\"m\n\x0cResourceInfo\x12\r\n\x05money\x18\x01 \x01(\x05\x12\x0c\n\x04\x66ood\x18\x02 \x01(\x05\x12\x0c\n\x04gold\x18\x03 \x01(\x05\x12\x13\n\x0b\x61\x63hievement\x18\x04 \x01(\x05\x12\x0f\n\x07soldier\x18\x05 \x01(\x05\x12\x0c\n\x04soul\x18\x06 \x01(\x05\"l\n\nUseGoldReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12\x10\n\x08use_gold\x18\x02 \x02(\x05\x12\x12\n\nlack_money\x18\x03 \x01(\x05\x12\x11\n\tlack_food\x18\x04 \x01(\x05\x12\x14\n\x0clack_soldier\x18\x05 \x01(\x05\"F\n\nUseGoldRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12(\n\x08resource\x18\x02 \x01(\x0b\x32\x16.SanProto.ResourceInfo')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RESOURCEINFO = _descriptor.Descriptor(
  name='ResourceInfo',
  full_name='SanProto.ResourceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='money', full_name='SanProto.ResourceInfo.money', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='food', full_name='SanProto.ResourceInfo.food', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='SanProto.ResourceInfo.gold', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='achievement', full_name='SanProto.ResourceInfo.achievement', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soldier', full_name='SanProto.ResourceInfo.soldier', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soul', full_name='SanProto.ResourceInfo.soul', index=5,
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
  serialized_start=28,
  serialized_end=137,
)


_USEGOLDREQ = _descriptor.Descriptor(
  name='UseGoldReq',
  full_name='SanProto.UseGoldReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.UseGoldReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_gold', full_name='SanProto.UseGoldReq.use_gold', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lack_money', full_name='SanProto.UseGoldReq.lack_money', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lack_food', full_name='SanProto.UseGoldReq.lack_food', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lack_soldier', full_name='SanProto.UseGoldReq.lack_soldier', index=4,
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
  serialized_start=139,
  serialized_end=247,
)


_USEGOLDRES = _descriptor.Descriptor(
  name='UseGoldRes',
  full_name='SanProto.UseGoldRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.UseGoldRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.UseGoldRes.resource', index=1,
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
  serialized_start=249,
  serialized_end=319,
)

_USEGOLDRES.fields_by_name['resource'].message_type = _RESOURCEINFO
DESCRIPTOR.message_types_by_name['ResourceInfo'] = _RESOURCEINFO
DESCRIPTOR.message_types_by_name['UseGoldReq'] = _USEGOLDREQ
DESCRIPTOR.message_types_by_name['UseGoldRes'] = _USEGOLDRES

ResourceInfo = _reflection.GeneratedProtocolMessageType('ResourceInfo', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCEINFO,
  __module__ = 'resource_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ResourceInfo)
  ))
_sym_db.RegisterMessage(ResourceInfo)

UseGoldReq = _reflection.GeneratedProtocolMessageType('UseGoldReq', (_message.Message,), dict(
  DESCRIPTOR = _USEGOLDREQ,
  __module__ = 'resource_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UseGoldReq)
  ))
_sym_db.RegisterMessage(UseGoldReq)

UseGoldRes = _reflection.GeneratedProtocolMessageType('UseGoldRes', (_message.Message,), dict(
  DESCRIPTOR = _USEGOLDRES,
  __module__ = 'resource_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.UseGoldRes)
  ))
_sym_db.RegisterMessage(UseGoldRes)


# @@protoc_insertion_point(module_scope)
