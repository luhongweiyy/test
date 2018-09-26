# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: increase.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import node_pb2
import item_pb2
import resource_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='increase.proto',
  package='SanProto',
  serialized_pb=_b('\n\x0eincrease.proto\x12\x08SanProto\x1a\nnode.proto\x1a\nitem.proto\x1a\x0eresource.proto\"b\n\x0bIncreaseReq\x12\x0f\n\x07user_id\x18\x01 \x02(\x04\x12 \n\x04node\x18\x02 \x02(\x0b\x32\x12.SanProto.NodeInfo\x12 \n\x04item\x18\x03 \x01(\x0b\x32\x12.SanProto.ItemInfo\"G\n\x0bIncreaseRes\x12\x0e\n\x06status\x18\x01 \x02(\x05\x12(\n\x08resource\x18\x02 \x01(\x0b\x32\x16.SanProto.ResourceInfo')
  ,
  dependencies=[node_pb2.DESCRIPTOR,item_pb2.DESCRIPTOR,resource_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INCREASEREQ = _descriptor.Descriptor(
  name='IncreaseReq',
  full_name='SanProto.IncreaseReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='SanProto.IncreaseReq.user_id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node', full_name='SanProto.IncreaseReq.node', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='SanProto.IncreaseReq.item', index=2,
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
  serialized_start=68,
  serialized_end=166,
)


_INCREASERES = _descriptor.Descriptor(
  name='IncreaseRes',
  full_name='SanProto.IncreaseRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.IncreaseRes.status', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resource', full_name='SanProto.IncreaseRes.resource', index=1,
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
  serialized_start=168,
  serialized_end=239,
)

_INCREASEREQ.fields_by_name['node'].message_type = node_pb2._NODEINFO
_INCREASEREQ.fields_by_name['item'].message_type = item_pb2._ITEMINFO
_INCREASERES.fields_by_name['resource'].message_type = resource_pb2._RESOURCEINFO
DESCRIPTOR.message_types_by_name['IncreaseReq'] = _INCREASEREQ
DESCRIPTOR.message_types_by_name['IncreaseRes'] = _INCREASERES

IncreaseReq = _reflection.GeneratedProtocolMessageType('IncreaseReq', (_message.Message,), dict(
  DESCRIPTOR = _INCREASEREQ,
  __module__ = 'increase_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.IncreaseReq)
  ))
_sym_db.RegisterMessage(IncreaseReq)

IncreaseRes = _reflection.GeneratedProtocolMessageType('IncreaseRes', (_message.Message,), dict(
  DESCRIPTOR = _INCREASERES,
  __module__ = 'increase_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.IncreaseRes)
  ))
_sym_db.RegisterMessage(IncreaseRes)


# @@protoc_insertion_point(module_scope)
