# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BaseInformationRecords.proto

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
  name='BaseInformationRecords.proto',
  package='org.campagnelab.dl.varanalysis.protobuf',
  syntax='proto2',
  serialized_pb=_b('\n\x1c\x42\x61seInformationRecords.proto\x12\'org.campagnelab.dl.varanalysis.protobuf\"f\n\x19\x42\x61seInformationCollection\x12I\n\x07records\x18\x01 \x03(\x0b\x32\x38.org.campagnelab.dl.varanalysis.protobuf.BaseInformation\"\xd6\x02\n\x0f\x42\x61seInformation\x12\x17\n\x0freference_index\x18\x01 \x02(\r\x12\x14\n\x0creference_id\x18\n \x01(\t\x12\x10\n\x08position\x18\x02 \x02(\r\x12\x0f\n\x07mutated\x18\x03 \x01(\x08\x12\x13\n\x0bmutatedBase\x18\x04 \x01(\t\x12\x1a\n\x12indexOfMutatedBase\x18\x07 \x01(\r\x12\x1b\n\x13\x66requencyOfMutation\x18\x06 \x01(\x02\x12\x15\n\rreferenceBase\x18\x05 \x01(\t\x12\x44\n\x07samples\x18\x08 \x03(\x0b\x32\x33.org.campagnelab.dl.varanalysis.protobuf.SampleInfo\x12\x14\n\x0ctrueGenotype\x18\t \x01(\t\x12\x10\n\x08trueFrom\x18\x0b \x01(\t\x12\x1e\n\x16genomicSequenceContext\x18\x0f \x01(\t\"\x8d\x01\n\nSampleInfo\x12\x42\n\x06\x63ounts\x18\x01 \x03(\x0b\x32\x32.org.campagnelab.dl.varanalysis.protobuf.CountInfo\x12\x0f\n\x07isTumor\x18\x02 \x01(\x08\x12\x17\n\x0f\x66ormattedCounts\x18\x03 \x01(\t\x12\x11\n\tisVariant\x18\x04 \x01(\x08\"\xc8\r\n\tCountInfo\x12\x18\n\x10matchesReference\x18\x01 \x02(\x08\x12\x14\n\x0c\x66romSequence\x18\x02 \x02(\t\x12\x12\n\ntoSequence\x18\x03 \x02(\t\x12\"\n\x1agenotypeCountForwardStrand\x18\x04 \x02(\r\x12\"\n\x1agenotypeCountReverseStrand\x18\x05 \x02(\r\x12\x0f\n\x07isIndel\x18\x0f \x01(\x08\x12`\n\x1aqualityScoresForwardStrand\x18\x10 \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12`\n\x1aqualityScoresReverseStrand\x18\x11 \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12^\n\x18readIndicesForwardStrand\x18\x12 \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12^\n\x18readIndicesReverseStrand\x18\x13 \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12\x65\n\x1freadMappingQualityForwardStrand\x18\x15 \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12\x65\n\x1freadMappingQualityReverseStrand\x18\x16 \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12Z\n\x14numVariationsInReads\x18\x17 \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12Q\n\x0binsertSizes\x18\x18 \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12Z\n\x14targetAlignedLengths\x18\x19 \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12Y\n\x13queryAlignedLengths\x18\x1a \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12T\n\x0equeryPositions\x18\x1e \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12O\n\tpairFlags\x18\x1b \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12l\n&distancesToReadVariationsForwardStrand\x18\x1c \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12l\n&distancesToReadVariationsReverseStrand\x18\x1d \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12[\n\x15\x64istanceToStartOfRead\x18\x1f \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12Y\n\x13\x64istanceToEndOfRead\x18  \x03(\x0b\x32<.org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency\x12\x10\n\x08isCalled\x18\x14 \x01(\x08\x12\x19\n\x11gobyGenotypeIndex\x18( \x01(\r\"8\n\x13NumberWithFrequency\x12\x0e\n\x06number\x18\x01 \x02(\x05\x12\x11\n\tfrequency\x18\x02 \x02(\rB+\n\'org.campagnelab.dl.varanalysis.protobufH\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BASEINFORMATIONCOLLECTION = _descriptor.Descriptor(
  name='BaseInformationCollection',
  full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformationCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='records', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformationCollection.records', index=0,
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
  serialized_start=73,
  serialized_end=175,
)


_BASEINFORMATION = _descriptor.Descriptor(
  name='BaseInformation',
  full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference_index', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.reference_index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_id', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.reference_id', index=1,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.position', index=2,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mutated', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.mutated', index=3,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mutatedBase', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.mutatedBase', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indexOfMutatedBase', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.indexOfMutatedBase', index=5,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frequencyOfMutation', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.frequencyOfMutation', index=6,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='referenceBase', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.referenceBase', index=7,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='samples', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.samples', index=8,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trueGenotype', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.trueGenotype', index=9,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trueFrom', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.trueFrom', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genomicSequenceContext', full_name='org.campagnelab.dl.varanalysis.protobuf.BaseInformation.genomicSequenceContext', index=11,
      number=15, type=9, cpp_type=9, label=1,
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
  serialized_start=178,
  serialized_end=520,
)


_SAMPLEINFO = _descriptor.Descriptor(
  name='SampleInfo',
  full_name='org.campagnelab.dl.varanalysis.protobuf.SampleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='counts', full_name='org.campagnelab.dl.varanalysis.protobuf.SampleInfo.counts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isTumor', full_name='org.campagnelab.dl.varanalysis.protobuf.SampleInfo.isTumor', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='formattedCounts', full_name='org.campagnelab.dl.varanalysis.protobuf.SampleInfo.formattedCounts', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isVariant', full_name='org.campagnelab.dl.varanalysis.protobuf.SampleInfo.isVariant', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=523,
  serialized_end=664,
)


_COUNTINFO = _descriptor.Descriptor(
  name='CountInfo',
  full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='matchesReference', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.matchesReference', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fromSequence', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.fromSequence', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='toSequence', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.toSequence', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genotypeCountForwardStrand', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.genotypeCountForwardStrand', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genotypeCountReverseStrand', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.genotypeCountReverseStrand', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isIndel', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.isIndel', index=5,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qualityScoresForwardStrand', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.qualityScoresForwardStrand', index=6,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qualityScoresReverseStrand', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.qualityScoresReverseStrand', index=7,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readIndicesForwardStrand', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.readIndicesForwardStrand', index=8,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readIndicesReverseStrand', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.readIndicesReverseStrand', index=9,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readMappingQualityForwardStrand', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.readMappingQualityForwardStrand', index=10,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readMappingQualityReverseStrand', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.readMappingQualityReverseStrand', index=11,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numVariationsInReads', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.numVariationsInReads', index=12,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='insertSizes', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.insertSizes', index=13,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='targetAlignedLengths', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.targetAlignedLengths', index=14,
      number=25, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='queryAlignedLengths', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.queryAlignedLengths', index=15,
      number=26, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='queryPositions', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.queryPositions', index=16,
      number=30, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pairFlags', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.pairFlags', index=17,
      number=27, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distancesToReadVariationsForwardStrand', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.distancesToReadVariationsForwardStrand', index=18,
      number=28, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distancesToReadVariationsReverseStrand', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.distancesToReadVariationsReverseStrand', index=19,
      number=29, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distanceToStartOfRead', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.distanceToStartOfRead', index=20,
      number=31, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distanceToEndOfRead', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.distanceToEndOfRead', index=21,
      number=32, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isCalled', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.isCalled', index=22,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gobyGenotypeIndex', full_name='org.campagnelab.dl.varanalysis.protobuf.CountInfo.gobyGenotypeIndex', index=23,
      number=40, type=13, cpp_type=3, label=1,
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
  serialized_start=667,
  serialized_end=2403,
)


_NUMBERWITHFREQUENCY = _descriptor.Descriptor(
  name='NumberWithFrequency',
  full_name='org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency.number', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency.frequency', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=2405,
  serialized_end=2461,
)

_BASEINFORMATIONCOLLECTION.fields_by_name['records'].message_type = _BASEINFORMATION
_BASEINFORMATION.fields_by_name['samples'].message_type = _SAMPLEINFO
_SAMPLEINFO.fields_by_name['counts'].message_type = _COUNTINFO
_COUNTINFO.fields_by_name['qualityScoresForwardStrand'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['qualityScoresReverseStrand'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['readIndicesForwardStrand'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['readIndicesReverseStrand'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['readMappingQualityForwardStrand'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['readMappingQualityReverseStrand'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['numVariationsInReads'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['insertSizes'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['targetAlignedLengths'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['queryAlignedLengths'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['queryPositions'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['pairFlags'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['distancesToReadVariationsForwardStrand'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['distancesToReadVariationsReverseStrand'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['distanceToStartOfRead'].message_type = _NUMBERWITHFREQUENCY
_COUNTINFO.fields_by_name['distanceToEndOfRead'].message_type = _NUMBERWITHFREQUENCY
DESCRIPTOR.message_types_by_name['BaseInformationCollection'] = _BASEINFORMATIONCOLLECTION
DESCRIPTOR.message_types_by_name['BaseInformation'] = _BASEINFORMATION
DESCRIPTOR.message_types_by_name['SampleInfo'] = _SAMPLEINFO
DESCRIPTOR.message_types_by_name['CountInfo'] = _COUNTINFO
DESCRIPTOR.message_types_by_name['NumberWithFrequency'] = _NUMBERWITHFREQUENCY

BaseInformationCollection = _reflection.GeneratedProtocolMessageType('BaseInformationCollection', (_message.Message,), dict(
  DESCRIPTOR = _BASEINFORMATIONCOLLECTION,
  __module__ = 'BaseInformationRecords_pb2'
  # @@protoc_insertion_point(class_scope:org.campagnelab.dl.varanalysis.protobuf.BaseInformationCollection)
  ))
_sym_db.RegisterMessage(BaseInformationCollection)

BaseInformation = _reflection.GeneratedProtocolMessageType('BaseInformation', (_message.Message,), dict(
  DESCRIPTOR = _BASEINFORMATION,
  __module__ = 'BaseInformationRecords_pb2'
  # @@protoc_insertion_point(class_scope:org.campagnelab.dl.varanalysis.protobuf.BaseInformation)
  ))
_sym_db.RegisterMessage(BaseInformation)

SampleInfo = _reflection.GeneratedProtocolMessageType('SampleInfo', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLEINFO,
  __module__ = 'BaseInformationRecords_pb2'
  # @@protoc_insertion_point(class_scope:org.campagnelab.dl.varanalysis.protobuf.SampleInfo)
  ))
_sym_db.RegisterMessage(SampleInfo)

CountInfo = _reflection.GeneratedProtocolMessageType('CountInfo', (_message.Message,), dict(
  DESCRIPTOR = _COUNTINFO,
  __module__ = 'BaseInformationRecords_pb2'
  # @@protoc_insertion_point(class_scope:org.campagnelab.dl.varanalysis.protobuf.CountInfo)
  ))
_sym_db.RegisterMessage(CountInfo)

NumberWithFrequency = _reflection.GeneratedProtocolMessageType('NumberWithFrequency', (_message.Message,), dict(
  DESCRIPTOR = _NUMBERWITHFREQUENCY,
  __module__ = 'BaseInformationRecords_pb2'
  # @@protoc_insertion_point(class_scope:org.campagnelab.dl.varanalysis.protobuf.NumberWithFrequency)
  ))
_sym_db.RegisterMessage(NumberWithFrequency)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\'org.campagnelab.dl.varanalysis.protobufH\001'))
# @@protoc_insertion_point(module_scope)
