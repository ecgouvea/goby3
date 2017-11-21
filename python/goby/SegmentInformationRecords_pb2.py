# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SegmentInformationRecords.proto

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
  name='SegmentInformationRecords.proto',
  package='org.campagnelab.dl.varanalysis.protobuf',
  syntax='proto2',
  serialized_pb=_b('\n\x1fSegmentInformationRecords.proto\x12\'org.campagnelab.dl.varanalysis.protobuf\"l\n\x1cSegmentInformationCollection\x12L\n\x07records\x18\x01 \x03(\x0b\x32;.org.campagnelab.dl.varanalysis.protobuf.SegmentInformation\"\x8b\x02\n\x12SegmentInformation\x12R\n\x0estart_position\x18\x01 \x01(\x0b\x32:.org.campagnelab.dl.varanalysis.protobuf.ReferencePosition\x12P\n\x0c\x65nd_position\x18\x02 \x01(\x0b\x32:.org.campagnelab.dl.varanalysis.protobuf.ReferencePosition\x12\x0e\n\x06length\x18\x05 \x01(\r\x12?\n\x06sample\x18\x04 \x03(\x0b\x32/.org.campagnelab.dl.varanalysis.protobuf.Sample\"E\n\x06Sample\x12;\n\x04\x62\x61se\x18\x01 \x03(\x0b\x32-.org.campagnelab.dl.varanalysis.protobuf.Base\"\xc0\x02\n\x04\x42\x61se\x12\x10\n\x08\x66\x65\x61tures\x18\x01 \x03(\x02\x12\x0e\n\x06labels\x18\x02 \x03(\x02\x12\r\n\x05\x63olor\x18\x06 \x03(\r\x12\x11\n\ttrueLabel\x18\x03 \x03(\t\x12!\n\x19prePostProcessingGenotype\x18\n \x01(\t\x12\x0e\n\x06offset\x18\x0b \x01(\r\x12\x19\n\x11hasCandidateIndel\x18\x04 \x01(\x08\x12\x14\n\x0chasTrueIndel\x18\x05 \x01(\x08\x12\x11\n\tisVariant\x18\x07 \x01(\x08\x12\x17\n\x0freferenceAllele\x18\x08 \x01(\t\x12\x17\n\x0f\x66ormattedCounts\x18\t \x01(\t\x12K\n\x07postion\x18\x0c \x01(\x0b\x32:.org.campagnelab.dl.varanalysis.protobuf.ReferencePosition\"T\n\x11ReferencePosition\x12\x17\n\x0freference_index\x18\x02 \x01(\r\x12\x14\n\x0creference_id\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x01 \x01(\rB+\n\'org.campagnelab.dl.varanalysis.protobufH\x01')
)




_SEGMENTINFORMATIONCOLLECTION = _descriptor.Descriptor(
  name='SegmentInformationCollection',
  full_name='org.campagnelab.dl.varanalysis.protobuf.SegmentInformationCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='records', full_name='org.campagnelab.dl.varanalysis.protobuf.SegmentInformationCollection.records', index=0,
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
  serialized_start=76,
  serialized_end=184,
)


_SEGMENTINFORMATION = _descriptor.Descriptor(
  name='SegmentInformation',
  full_name='org.campagnelab.dl.varanalysis.protobuf.SegmentInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_position', full_name='org.campagnelab.dl.varanalysis.protobuf.SegmentInformation.start_position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_position', full_name='org.campagnelab.dl.varanalysis.protobuf.SegmentInformation.end_position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='org.campagnelab.dl.varanalysis.protobuf.SegmentInformation.length', index=2,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sample', full_name='org.campagnelab.dl.varanalysis.protobuf.SegmentInformation.sample', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=187,
  serialized_end=454,
)


_SAMPLE = _descriptor.Descriptor(
  name='Sample',
  full_name='org.campagnelab.dl.varanalysis.protobuf.Sample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base', full_name='org.campagnelab.dl.varanalysis.protobuf.Sample.base', index=0,
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
  serialized_start=456,
  serialized_end=525,
)


_BASE = _descriptor.Descriptor(
  name='Base',
  full_name='org.campagnelab.dl.varanalysis.protobuf.Base',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.features', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.labels', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='color', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.color', index=2,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trueLabel', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.trueLabel', index=3,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prePostProcessingGenotype', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.prePostProcessingGenotype', index=4,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.offset', index=5,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hasCandidateIndel', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.hasCandidateIndel', index=6,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hasTrueIndel', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.hasTrueIndel', index=7,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isVariant', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.isVariant', index=8,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='referenceAllele', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.referenceAllele', index=9,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='formattedCounts', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.formattedCounts', index=10,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='postion', full_name='org.campagnelab.dl.varanalysis.protobuf.Base.postion', index=11,
      number=12, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=528,
  serialized_end=848,
)


_REFERENCEPOSITION = _descriptor.Descriptor(
  name='ReferencePosition',
  full_name='org.campagnelab.dl.varanalysis.protobuf.ReferencePosition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_index', full_name='org.campagnelab.dl.varanalysis.protobuf.ReferencePosition.reference_index', index=0,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_id', full_name='org.campagnelab.dl.varanalysis.protobuf.ReferencePosition.reference_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='org.campagnelab.dl.varanalysis.protobuf.ReferencePosition.location', index=2,
      number=1, type=13, cpp_type=3, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=850,
  serialized_end=934,
)

_SEGMENTINFORMATIONCOLLECTION.fields_by_name['records'].message_type = _SEGMENTINFORMATION
_SEGMENTINFORMATION.fields_by_name['start_position'].message_type = _REFERENCEPOSITION
_SEGMENTINFORMATION.fields_by_name['end_position'].message_type = _REFERENCEPOSITION
_SEGMENTINFORMATION.fields_by_name['sample'].message_type = _SAMPLE
_SAMPLE.fields_by_name['base'].message_type = _BASE
_BASE.fields_by_name['postion'].message_type = _REFERENCEPOSITION
DESCRIPTOR.message_types_by_name['SegmentInformationCollection'] = _SEGMENTINFORMATIONCOLLECTION
DESCRIPTOR.message_types_by_name['SegmentInformation'] = _SEGMENTINFORMATION
DESCRIPTOR.message_types_by_name['Sample'] = _SAMPLE
DESCRIPTOR.message_types_by_name['Base'] = _BASE
DESCRIPTOR.message_types_by_name['ReferencePosition'] = _REFERENCEPOSITION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SegmentInformationCollection = _reflection.GeneratedProtocolMessageType('SegmentInformationCollection', (_message.Message,), dict(
  DESCRIPTOR = _SEGMENTINFORMATIONCOLLECTION,
  __module__ = 'SegmentInformationRecords_pb2'
  # @@protoc_insertion_point(class_scope:org.campagnelab.dl.varanalysis.protobuf.SegmentInformationCollection)
  ))
_sym_db.RegisterMessage(SegmentInformationCollection)

SegmentInformation = _reflection.GeneratedProtocolMessageType('SegmentInformation', (_message.Message,), dict(
  DESCRIPTOR = _SEGMENTINFORMATION,
  __module__ = 'SegmentInformationRecords_pb2'
  # @@protoc_insertion_point(class_scope:org.campagnelab.dl.varanalysis.protobuf.SegmentInformation)
  ))
_sym_db.RegisterMessage(SegmentInformation)

Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLE,
  __module__ = 'SegmentInformationRecords_pb2'
  # @@protoc_insertion_point(class_scope:org.campagnelab.dl.varanalysis.protobuf.Sample)
  ))
_sym_db.RegisterMessage(Sample)

Base = _reflection.GeneratedProtocolMessageType('Base', (_message.Message,), dict(
  DESCRIPTOR = _BASE,
  __module__ = 'SegmentInformationRecords_pb2'
  # @@protoc_insertion_point(class_scope:org.campagnelab.dl.varanalysis.protobuf.Base)
  ))
_sym_db.RegisterMessage(Base)

ReferencePosition = _reflection.GeneratedProtocolMessageType('ReferencePosition', (_message.Message,), dict(
  DESCRIPTOR = _REFERENCEPOSITION,
  __module__ = 'SegmentInformationRecords_pb2'
  # @@protoc_insertion_point(class_scope:org.campagnelab.dl.varanalysis.protobuf.ReferencePosition)
  ))
_sym_db.RegisterMessage(ReferencePosition)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\'org.campagnelab.dl.varanalysis.protobufH\001'))
# @@protoc_insertion_point(module_scope)
