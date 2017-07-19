# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Reads.proto

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
  name='Reads.proto',
  package='goby',
  syntax='proto2',
  serialized_pb=_b('\n\x0bReads.proto\x12\x04goby\"0\n\x0eReadCollection\x12\x1e\n\x05reads\x18\x01 \x03(\x0b\x32\x0f.goby.ReadEntry\"\xad\x02\n\tReadEntry\x12\x12\n\nread_index\x18\x01 \x02(\r\x12\x15\n\rbarcode_index\x18\n \x01(\r\x12\x17\n\x0fread_identifier\x18\x17 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x16 \x01(\t\x12\x13\n\x0bread_length\x18\x02 \x02(\r\x12\x10\n\x08sequence\x18\x03 \x01(\x0c\x12\x15\n\rsequence_pair\x18\x05 \x01(\x0c\x12\x18\n\x10read_length_pair\x18\x06 \x01(\r\x12\x16\n\x0equality_scores\x18\x04 \x01(\x0c\x12\x1b\n\x13quality_scores_pair\x18\x07 \x01(\x0c\x12\x17\n\x0f\x63ompressed_data\x18\x08 \x01(\x0c\x12!\n\tmeta_data\x18\x19 \x03(\x0b\x32\x0e.goby.MetaData\"&\n\x08MetaData\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\tB\x1e\n\x1aorg.campagnelab.goby.readsH\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_READCOLLECTION = _descriptor.Descriptor(
  name='ReadCollection',
  full_name='goby.ReadCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reads', full_name='goby.ReadCollection.reads', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=69,
)


_READENTRY = _descriptor.Descriptor(
  name='ReadEntry',
  full_name='goby.ReadEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='read_index', full_name='goby.ReadEntry.read_index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='barcode_index', full_name='goby.ReadEntry.barcode_index', index=1,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_identifier', full_name='goby.ReadEntry.read_identifier', index=2,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='goby.ReadEntry.description', index=3,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_length', full_name='goby.ReadEntry.read_length', index=4,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='goby.ReadEntry.sequence', index=5,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequence_pair', full_name='goby.ReadEntry.sequence_pair', index=6,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_length_pair', full_name='goby.ReadEntry.read_length_pair', index=7,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quality_scores', full_name='goby.ReadEntry.quality_scores', index=8,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quality_scores_pair', full_name='goby.ReadEntry.quality_scores_pair', index=9,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compressed_data', full_name='goby.ReadEntry.compressed_data', index=10,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='meta_data', full_name='goby.ReadEntry.meta_data', index=11,
      number=25, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=373,
)


_METADATA = _descriptor.Descriptor(
  name='MetaData',
  full_name='goby.MetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='goby.MetaData.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='goby.MetaData.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=413,
)

_READCOLLECTION.fields_by_name['reads'].message_type = _READENTRY
_READENTRY.fields_by_name['meta_data'].message_type = _METADATA
DESCRIPTOR.message_types_by_name['ReadCollection'] = _READCOLLECTION
DESCRIPTOR.message_types_by_name['ReadEntry'] = _READENTRY
DESCRIPTOR.message_types_by_name['MetaData'] = _METADATA

ReadCollection = _reflection.GeneratedProtocolMessageType('ReadCollection', (_message.Message,), dict(
  DESCRIPTOR = _READCOLLECTION,
  __module__ = 'Reads_pb2'
  # @@protoc_insertion_point(class_scope:goby.ReadCollection)
  ))
_sym_db.RegisterMessage(ReadCollection)

ReadEntry = _reflection.GeneratedProtocolMessageType('ReadEntry', (_message.Message,), dict(
  DESCRIPTOR = _READENTRY,
  __module__ = 'Reads_pb2'
  # @@protoc_insertion_point(class_scope:goby.ReadEntry)
  ))
_sym_db.RegisterMessage(ReadEntry)

MetaData = _reflection.GeneratedProtocolMessageType('MetaData', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'Reads_pb2'
  # @@protoc_insertion_point(class_scope:goby.MetaData)
  ))
_sym_db.RegisterMessage(MetaData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032org.campagnelab.goby.readsH\001'))
# @@protoc_insertion_point(module_scope)
