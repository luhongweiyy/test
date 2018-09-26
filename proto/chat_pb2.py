# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto

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
  name='chat.proto',
  package='SanProto',
  serialized_pb=_b('\n\nchat.proto\x12\x08SanProto\"i\n\x0cStartChatReq\x12)\n\x04type\x18\x01 \x02(\x0e\x32\x1b.SanProto.StartChatReq.TYPE\x12\x10\n\x08union_id\x18\x02 \x01(\x05\"\x1c\n\x04TYPE\x12\t\n\x05WORLD\x10\x01\x12\t\n\x05UNION\x10\x02\"u\n\x0cStartChatRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12\x11\n\tavailable\x18\x02 \x01(\x08\x12\x10\n\x08hostname\x18\x03 \x01(\x0c\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\x10\n\x08roomname\x18\x05 \x01(\x0c\x12\x10\n\x08password\x18\x06 \x01(\x0c\"I\n\rManageChatReq\x12\x16\n\x0etarget_user_id\x18\x01 \x02(\x04\x12\x0e\n\x06\x65nable\x18\x02 \x02(\x08\x12\x10\n\x08lock_min\x18\x03 \x01(\x05\"\x1f\n\rManageChatRes\x12\x0e\n\x06status\x18\x01 \x02(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STARTCHATREQ_TYPE = _descriptor.EnumDescriptor(
  name='TYPE',
  full_name='SanProto.StartChatReq.TYPE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WORLD', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNION', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=101,
  serialized_end=129,
)
_sym_db.RegisterEnumDescriptor(_STARTCHATREQ_TYPE)


_STARTCHATREQ = _descriptor.Descriptor(
  name='StartChatReq',
  full_name='SanProto.StartChatReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='SanProto.StartChatReq.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='union_id', full_name='SanProto.StartChatReq.union_id', index=1,
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
    _STARTCHATREQ_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=129,
)


_STARTCHATRES = _descriptor.Descriptor(
  name='StartChatRes',
  full_name='SanProto.StartChatRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.StartChatRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='available', full_name='SanProto.StartChatRes.available', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='SanProto.StartChatRes.hostname', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='SanProto.StartChatRes.port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roomname', full_name='SanProto.StartChatRes.roomname', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='SanProto.StartChatRes.password', index=5,
      number=6, type=12, cpp_type=9, label=1,
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
  serialized_start=131,
  serialized_end=248,
)


_MANAGECHATREQ = _descriptor.Descriptor(
  name='ManageChatReq',
  full_name='SanProto.ManageChatReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_user_id', full_name='SanProto.ManageChatReq.target_user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enable', full_name='SanProto.ManageChatReq.enable', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lock_min', full_name='SanProto.ManageChatReq.lock_min', index=2,
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
  serialized_start=250,
  serialized_end=323,
)


_MANAGECHATRES = _descriptor.Descriptor(
  name='ManageChatRes',
  full_name='SanProto.ManageChatRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.ManageChatRes.status', index=0,
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
  serialized_start=325,
  serialized_end=356,
)

_STARTCHATREQ.fields_by_name['type'].enum_type = _STARTCHATREQ_TYPE
_STARTCHATREQ_TYPE.containing_type = _STARTCHATREQ
DESCRIPTOR.message_types_by_name['StartChatReq'] = _STARTCHATREQ
DESCRIPTOR.message_types_by_name['StartChatRes'] = _STARTCHATRES
DESCRIPTOR.message_types_by_name['ManageChatReq'] = _MANAGECHATREQ
DESCRIPTOR.message_types_by_name['ManageChatRes'] = _MANAGECHATRES

StartChatReq = _reflection.GeneratedProtocolMessageType('StartChatReq', (_message.Message,), dict(
  DESCRIPTOR = _STARTCHATREQ,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.StartChatReq)
  ))
_sym_db.RegisterMessage(StartChatReq)

StartChatRes = _reflection.GeneratedProtocolMessageType('StartChatRes', (_message.Message,), dict(
  DESCRIPTOR = _STARTCHATRES,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.StartChatRes)
  ))
_sym_db.RegisterMessage(StartChatRes)

ManageChatReq = _reflection.GeneratedProtocolMessageType('ManageChatReq', (_message.Message,), dict(
  DESCRIPTOR = _MANAGECHATREQ,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ManageChatReq)
  ))
_sym_db.RegisterMessage(ManageChatReq)

ManageChatRes = _reflection.GeneratedProtocolMessageType('ManageChatRes', (_message.Message,), dict(
  DESCRIPTOR = _MANAGECHATRES,
  __module__ = 'chat_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ManageChatRes)
  ))
_sym_db.RegisterMessage(ManageChatRes)


# @@protoc_insertion_point(module_scope)
