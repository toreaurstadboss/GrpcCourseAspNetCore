# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MeterReader.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import enums_pb2 as enums__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='MeterReader.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\252\002\027MeterReaderWeb.Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11MeterReader.proto\x1a\x0b\x65nums.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"e\n\rReadingPacket\x12!\n\x08readings\x18\x01 \x03(\x0b\x32\x0f.ReadingMessage\x12\r\n\x05notes\x18\x02 \x01(\t\x12\"\n\nsuccessful\x18\x03 \x01(\x0e\x32\x0e.ReadingStatus\"\x83\x01\n\x0eReadingMessage\x12\x12\n\ncustomerId\x18\x01 \x01(\x05\x12\x14\n\x0creadingValue\x18\x02 \x01(\x05\x12/\n\x0breadingTime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampJ\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05R\nsuccessful\"D\n\rStatusMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\"\n\nsuccessful\x18\x02 \x01(\x0e\x32\x0e.ReadingStatus2C\n\x13MeterReadingService\x12,\n\nAddReading\x12\x0e.ReadingPacket\x1a\x0e.StatusMessageB\x1a\xaa\x02\x17MeterReaderWeb.Servicesb\x06proto3'
  ,
  dependencies=[enums__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_READINGPACKET = _descriptor.Descriptor(
  name='ReadingPacket',
  full_name='ReadingPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='readings', full_name='ReadingPacket.readings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notes', full_name='ReadingPacket.notes', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='successful', full_name='ReadingPacket.successful', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=168,
)


_READINGMESSAGE = _descriptor.Descriptor(
  name='ReadingMessage',
  full_name='ReadingMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customerId', full_name='ReadingMessage.customerId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='readingValue', full_name='ReadingMessage.readingValue', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='readingTime', full_name='ReadingMessage.readingTime', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=171,
  serialized_end=302,
)


_STATUSMESSAGE = _descriptor.Descriptor(
  name='StatusMessage',
  full_name='StatusMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='StatusMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='successful', full_name='StatusMessage.successful', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=372,
)

_READINGPACKET.fields_by_name['readings'].message_type = _READINGMESSAGE
_READINGPACKET.fields_by_name['successful'].enum_type = enums__pb2._READINGSTATUS
_READINGMESSAGE.fields_by_name['readingTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STATUSMESSAGE.fields_by_name['successful'].enum_type = enums__pb2._READINGSTATUS
DESCRIPTOR.message_types_by_name['ReadingPacket'] = _READINGPACKET
DESCRIPTOR.message_types_by_name['ReadingMessage'] = _READINGMESSAGE
DESCRIPTOR.message_types_by_name['StatusMessage'] = _STATUSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReadingPacket = _reflection.GeneratedProtocolMessageType('ReadingPacket', (_message.Message,), {
  'DESCRIPTOR' : _READINGPACKET,
  '__module__' : 'MeterReader_pb2'
  # @@protoc_insertion_point(class_scope:ReadingPacket)
  })
_sym_db.RegisterMessage(ReadingPacket)

ReadingMessage = _reflection.GeneratedProtocolMessageType('ReadingMessage', (_message.Message,), {
  'DESCRIPTOR' : _READINGMESSAGE,
  '__module__' : 'MeterReader_pb2'
  # @@protoc_insertion_point(class_scope:ReadingMessage)
  })
_sym_db.RegisterMessage(ReadingMessage)

StatusMessage = _reflection.GeneratedProtocolMessageType('StatusMessage', (_message.Message,), {
  'DESCRIPTOR' : _STATUSMESSAGE,
  '__module__' : 'MeterReader_pb2'
  # @@protoc_insertion_point(class_scope:StatusMessage)
  })
_sym_db.RegisterMessage(StatusMessage)


DESCRIPTOR._options = None

_METERREADINGSERVICE = _descriptor.ServiceDescriptor(
  name='MeterReadingService',
  full_name='MeterReadingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=374,
  serialized_end=441,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddReading',
    full_name='MeterReadingService.AddReading',
    index=0,
    containing_service=None,
    input_type=_READINGPACKET,
    output_type=_STATUSMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_METERREADINGSERVICE)

DESCRIPTOR.services_by_name['MeterReadingService'] = _METERREADINGSERVICE

# @@protoc_insertion_point(module_scope)
