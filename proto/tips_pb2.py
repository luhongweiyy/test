# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tips.proto

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
  name='tips.proto',
  package='SanProto',
  serialized_pb=_b('\n\ntips.proto\x12\x08SanProto\"\x84\x02\n\nButtonTips\x12)\n\x05index\x18\x01 \x02(\x0e\x32\x1a.SanProto.ButtonTips.INDEX\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x10\n\x08redpoint\x18\x03 \x01(\x05\"\xa8\x01\n\x05INDEX\x12\x16\n\x12\x41\x43TIVITY_SEVEN_DAY\x10\x01\x12\x16\n\x12\x41\x43TIVITY_FIRST_PAY\x10\x02\x12\x12\n\x0e\x41\x43TIVITY_DAILY\x10\x03\x12\x11\n\rACTIVITY_SHOP\x10\x04\x12\x13\n\x0f\x41\x43TIVITY_NORMAL\x10\x05\x12\x15\n\x11\x41\x43TIVITY_FESTIVAL\x10\x06\x12\x10\n\x0cUNION_BATTLE\x10\x07\x12\n\n\x06\x41SSESS\x10\x08')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BUTTONTIPS_INDEX = _descriptor.EnumDescriptor(
  name='INDEX',
  full_name='SanProto.ButtonTips.INDEX',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTIVITY_SEVEN_DAY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVITY_FIRST_PAY', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVITY_DAILY', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVITY_SHOP', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVITY_NORMAL', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVITY_FESTIVAL', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNION_BATTLE', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASSESS', index=7, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=117,
  serialized_end=285,
)
_sym_db.RegisterEnumDescriptor(_BUTTONTIPS_INDEX)


_BUTTONTIPS = _descriptor.Descriptor(
  name='ButtonTips',
  full_name='SanProto.ButtonTips',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='SanProto.ButtonTips.index', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='SanProto.ButtonTips.status', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='redpoint', full_name='SanProto.ButtonTips.redpoint', index=2,
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
    _BUTTONTIPS_INDEX,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=285,
)

_BUTTONTIPS.fields_by_name['index'].enum_type = _BUTTONTIPS_INDEX
_BUTTONTIPS_INDEX.containing_type = _BUTTONTIPS
DESCRIPTOR.message_types_by_name['ButtonTips'] = _BUTTONTIPS

ButtonTips = _reflection.GeneratedProtocolMessageType('ButtonTips', (_message.Message,), dict(
  DESCRIPTOR = _BUTTONTIPS,
  __module__ = 'tips_pb2'
  # @@protoc_insertion_point(class_scope:SanProto.ButtonTips)
  ))
_sym_db.RegisterMessage(ButtonTips)


# @@protoc_insertion_point(module_scope)
