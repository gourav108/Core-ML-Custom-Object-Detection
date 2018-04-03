# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/optimizer.proto

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
  name='object_detection/protos/optimizer.proto',
  package='protos',
  syntax='proto2',
  serialized_pb=_b('\n\'object_detection/protos/optimizer.proto\x12\x06protos\"\x82\x02\n\tOptimizer\x12\x36\n\x12rms_prop_optimizer\x18\x01 \x01(\x0b\x32\x18.protos.RMSPropOptimizerH\x00\x12\x37\n\x12momentum_optimizer\x18\x02 \x01(\x0b\x32\x19.protos.MomentumOptimizerH\x00\x12/\n\x0e\x61\x64\x61m_optimizer\x18\x03 \x01(\x0b\x32\x15.protos.AdamOptimizerH\x00\x12 \n\x12use_moving_average\x18\x04 \x01(\x08:\x04true\x12$\n\x14moving_average_decay\x18\x05 \x01(\x02:\x06\x30.9999B\x0b\n\toptimizer\"\x8e\x01\n\x10RMSPropOptimizer\x12+\n\rlearning_rate\x18\x01 \x01(\x0b\x32\x14.protos.LearningRate\x12%\n\x18momentum_optimizer_value\x18\x02 \x01(\x02:\x03\x30.9\x12\x12\n\x05\x64\x65\x63\x61y\x18\x03 \x01(\x02:\x03\x30.9\x12\x12\n\x07\x65psilon\x18\x04 \x01(\x02:\x01\x31\"g\n\x11MomentumOptimizer\x12+\n\rlearning_rate\x18\x01 \x01(\x0b\x32\x14.protos.LearningRate\x12%\n\x18momentum_optimizer_value\x18\x02 \x01(\x02:\x03\x30.9\"<\n\rAdamOptimizer\x12+\n\rlearning_rate\x18\x01 \x01(\x0b\x32\x14.protos.LearningRate\"\xbc\x02\n\x0cLearningRate\x12>\n\x16\x63onstant_learning_rate\x18\x01 \x01(\x0b\x32\x1c.protos.ConstantLearningRateH\x00\x12O\n\x1f\x65xponential_decay_learning_rate\x18\x02 \x01(\x0b\x32$.protos.ExponentialDecayLearningRateH\x00\x12\x43\n\x19manual_step_learning_rate\x18\x03 \x01(\x0b\x32\x1e.protos.ManualStepLearningRateH\x00\x12\x45\n\x1a\x63osine_decay_learning_rate\x18\x04 \x01(\x0b\x32\x1f.protos.CosineDecayLearningRateH\x00\x42\x0f\n\rlearning_rate\"4\n\x14\x43onstantLearningRate\x12\x1c\n\rlearning_rate\x18\x01 \x01(\x02:\x05\x30.002\"\x97\x01\n\x1c\x45xponentialDecayLearningRate\x12$\n\x15initial_learning_rate\x18\x01 \x01(\x02:\x05\x30.002\x12\x1c\n\x0b\x64\x65\x63\x61y_steps\x18\x02 \x01(\r:\x07\x34\x30\x30\x30\x30\x30\x30\x12\x1a\n\x0c\x64\x65\x63\x61y_factor\x18\x03 \x01(\x02:\x04\x30.95\x12\x17\n\tstaircase\x18\x04 \x01(\x08:\x04true\"\xe0\x01\n\x16ManualStepLearningRate\x12$\n\x15initial_learning_rate\x18\x01 \x01(\x02:\x05\x30.002\x12\x45\n\x08schedule\x18\x02 \x03(\x0b\x32\x33.protos.ManualStepLearningRate.LearningRateSchedule\x12\x15\n\x06warmup\x18\x03 \x01(\x08:\x05\x66\x61lse\x1a\x42\n\x14LearningRateSchedule\x12\x0c\n\x04step\x18\x01 \x01(\r\x12\x1c\n\rlearning_rate\x18\x02 \x01(\x02:\x05\x30.002\"\xbe\x01\n\x17\x43osineDecayLearningRate\x12!\n\x12learning_rate_base\x18\x01 \x01(\x02:\x05\x30.002\x12\x1c\n\x0btotal_steps\x18\x02 \x01(\r:\x07\x34\x30\x30\x30\x30\x30\x30\x12$\n\x14warmup_learning_rate\x18\x03 \x01(\x02:\x06\x30.0002\x12\x1b\n\x0cwarmup_steps\x18\x04 \x01(\r:\x05\x31\x30\x30\x30\x30\x12\x1f\n\x14hold_base_rate_steps\x18\x05 \x01(\r:\x01\x30')
)




_OPTIMIZER = _descriptor.Descriptor(
  name='Optimizer',
  full_name='protos.Optimizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rms_prop_optimizer', full_name='protos.Optimizer.rms_prop_optimizer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='momentum_optimizer', full_name='protos.Optimizer.momentum_optimizer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adam_optimizer', full_name='protos.Optimizer.adam_optimizer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_moving_average', full_name='protos.Optimizer.use_moving_average', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moving_average_decay', full_name='protos.Optimizer.moving_average_decay', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.9999),
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
    _descriptor.OneofDescriptor(
      name='optimizer', full_name='protos.Optimizer.optimizer',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=52,
  serialized_end=310,
)


_RMSPROPOPTIMIZER = _descriptor.Descriptor(
  name='RMSPropOptimizer',
  full_name='protos.RMSPropOptimizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='protos.RMSPropOptimizer.learning_rate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='momentum_optimizer_value', full_name='protos.RMSPropOptimizer.momentum_optimizer_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.9),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decay', full_name='protos.RMSPropOptimizer.decay', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.9),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='epsilon', full_name='protos.RMSPropOptimizer.epsilon', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
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
  serialized_start=313,
  serialized_end=455,
)


_MOMENTUMOPTIMIZER = _descriptor.Descriptor(
  name='MomentumOptimizer',
  full_name='protos.MomentumOptimizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='protos.MomentumOptimizer.learning_rate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='momentum_optimizer_value', full_name='protos.MomentumOptimizer.momentum_optimizer_value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.9),
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
  serialized_start=457,
  serialized_end=560,
)


_ADAMOPTIMIZER = _descriptor.Descriptor(
  name='AdamOptimizer',
  full_name='protos.AdamOptimizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='protos.AdamOptimizer.learning_rate', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=562,
  serialized_end=622,
)


_LEARNINGRATE = _descriptor.Descriptor(
  name='LearningRate',
  full_name='protos.LearningRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='constant_learning_rate', full_name='protos.LearningRate.constant_learning_rate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exponential_decay_learning_rate', full_name='protos.LearningRate.exponential_decay_learning_rate', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manual_step_learning_rate', full_name='protos.LearningRate.manual_step_learning_rate', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cosine_decay_learning_rate', full_name='protos.LearningRate.cosine_decay_learning_rate', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='learning_rate', full_name='protos.LearningRate.learning_rate',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=625,
  serialized_end=941,
)


_CONSTANTLEARNINGRATE = _descriptor.Descriptor(
  name='ConstantLearningRate',
  full_name='protos.ConstantLearningRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='protos.ConstantLearningRate.learning_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.002),
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
  serialized_start=943,
  serialized_end=995,
)


_EXPONENTIALDECAYLEARNINGRATE = _descriptor.Descriptor(
  name='ExponentialDecayLearningRate',
  full_name='protos.ExponentialDecayLearningRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='initial_learning_rate', full_name='protos.ExponentialDecayLearningRate.initial_learning_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.002),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decay_steps', full_name='protos.ExponentialDecayLearningRate.decay_steps', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4000000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decay_factor', full_name='protos.ExponentialDecayLearningRate.decay_factor', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.95),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staircase', full_name='protos.ExponentialDecayLearningRate.staircase', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  serialized_start=998,
  serialized_end=1149,
)


_MANUALSTEPLEARNINGRATE_LEARNINGRATESCHEDULE = _descriptor.Descriptor(
  name='LearningRateSchedule',
  full_name='protos.ManualStepLearningRate.LearningRateSchedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='protos.ManualStepLearningRate.LearningRateSchedule.step', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='protos.ManualStepLearningRate.LearningRateSchedule.learning_rate', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.002),
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
  serialized_start=1310,
  serialized_end=1376,
)

_MANUALSTEPLEARNINGRATE = _descriptor.Descriptor(
  name='ManualStepLearningRate',
  full_name='protos.ManualStepLearningRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='initial_learning_rate', full_name='protos.ManualStepLearningRate.initial_learning_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.002),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='schedule', full_name='protos.ManualStepLearningRate.schedule', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='warmup', full_name='protos.ManualStepLearningRate.warmup', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MANUALSTEPLEARNINGRATE_LEARNINGRATESCHEDULE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1152,
  serialized_end=1376,
)


_COSINEDECAYLEARNINGRATE = _descriptor.Descriptor(
  name='CosineDecayLearningRate',
  full_name='protos.CosineDecayLearningRate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='learning_rate_base', full_name='protos.CosineDecayLearningRate.learning_rate_base', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.002),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_steps', full_name='protos.CosineDecayLearningRate.total_steps', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4000000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='warmup_learning_rate', full_name='protos.CosineDecayLearningRate.warmup_learning_rate', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.0002),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='warmup_steps', full_name='protos.CosineDecayLearningRate.warmup_steps', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=10000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hold_base_rate_steps', full_name='protos.CosineDecayLearningRate.hold_base_rate_steps', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=1379,
  serialized_end=1569,
)

_OPTIMIZER.fields_by_name['rms_prop_optimizer'].message_type = _RMSPROPOPTIMIZER
_OPTIMIZER.fields_by_name['momentum_optimizer'].message_type = _MOMENTUMOPTIMIZER
_OPTIMIZER.fields_by_name['adam_optimizer'].message_type = _ADAMOPTIMIZER
_OPTIMIZER.oneofs_by_name['optimizer'].fields.append(
  _OPTIMIZER.fields_by_name['rms_prop_optimizer'])
_OPTIMIZER.fields_by_name['rms_prop_optimizer'].containing_oneof = _OPTIMIZER.oneofs_by_name['optimizer']
_OPTIMIZER.oneofs_by_name['optimizer'].fields.append(
  _OPTIMIZER.fields_by_name['momentum_optimizer'])
_OPTIMIZER.fields_by_name['momentum_optimizer'].containing_oneof = _OPTIMIZER.oneofs_by_name['optimizer']
_OPTIMIZER.oneofs_by_name['optimizer'].fields.append(
  _OPTIMIZER.fields_by_name['adam_optimizer'])
_OPTIMIZER.fields_by_name['adam_optimizer'].containing_oneof = _OPTIMIZER.oneofs_by_name['optimizer']
_RMSPROPOPTIMIZER.fields_by_name['learning_rate'].message_type = _LEARNINGRATE
_MOMENTUMOPTIMIZER.fields_by_name['learning_rate'].message_type = _LEARNINGRATE
_ADAMOPTIMIZER.fields_by_name['learning_rate'].message_type = _LEARNINGRATE
_LEARNINGRATE.fields_by_name['constant_learning_rate'].message_type = _CONSTANTLEARNINGRATE
_LEARNINGRATE.fields_by_name['exponential_decay_learning_rate'].message_type = _EXPONENTIALDECAYLEARNINGRATE
_LEARNINGRATE.fields_by_name['manual_step_learning_rate'].message_type = _MANUALSTEPLEARNINGRATE
_LEARNINGRATE.fields_by_name['cosine_decay_learning_rate'].message_type = _COSINEDECAYLEARNINGRATE
_LEARNINGRATE.oneofs_by_name['learning_rate'].fields.append(
  _LEARNINGRATE.fields_by_name['constant_learning_rate'])
_LEARNINGRATE.fields_by_name['constant_learning_rate'].containing_oneof = _LEARNINGRATE.oneofs_by_name['learning_rate']
_LEARNINGRATE.oneofs_by_name['learning_rate'].fields.append(
  _LEARNINGRATE.fields_by_name['exponential_decay_learning_rate'])
_LEARNINGRATE.fields_by_name['exponential_decay_learning_rate'].containing_oneof = _LEARNINGRATE.oneofs_by_name['learning_rate']
_LEARNINGRATE.oneofs_by_name['learning_rate'].fields.append(
  _LEARNINGRATE.fields_by_name['manual_step_learning_rate'])
_LEARNINGRATE.fields_by_name['manual_step_learning_rate'].containing_oneof = _LEARNINGRATE.oneofs_by_name['learning_rate']
_LEARNINGRATE.oneofs_by_name['learning_rate'].fields.append(
  _LEARNINGRATE.fields_by_name['cosine_decay_learning_rate'])
_LEARNINGRATE.fields_by_name['cosine_decay_learning_rate'].containing_oneof = _LEARNINGRATE.oneofs_by_name['learning_rate']
_MANUALSTEPLEARNINGRATE_LEARNINGRATESCHEDULE.containing_type = _MANUALSTEPLEARNINGRATE
_MANUALSTEPLEARNINGRATE.fields_by_name['schedule'].message_type = _MANUALSTEPLEARNINGRATE_LEARNINGRATESCHEDULE
DESCRIPTOR.message_types_by_name['Optimizer'] = _OPTIMIZER
DESCRIPTOR.message_types_by_name['RMSPropOptimizer'] = _RMSPROPOPTIMIZER
DESCRIPTOR.message_types_by_name['MomentumOptimizer'] = _MOMENTUMOPTIMIZER
DESCRIPTOR.message_types_by_name['AdamOptimizer'] = _ADAMOPTIMIZER
DESCRIPTOR.message_types_by_name['LearningRate'] = _LEARNINGRATE
DESCRIPTOR.message_types_by_name['ConstantLearningRate'] = _CONSTANTLEARNINGRATE
DESCRIPTOR.message_types_by_name['ExponentialDecayLearningRate'] = _EXPONENTIALDECAYLEARNINGRATE
DESCRIPTOR.message_types_by_name['ManualStepLearningRate'] = _MANUALSTEPLEARNINGRATE
DESCRIPTOR.message_types_by_name['CosineDecayLearningRate'] = _COSINEDECAYLEARNINGRATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Optimizer = _reflection.GeneratedProtocolMessageType('Optimizer', (_message.Message,), dict(
  DESCRIPTOR = _OPTIMIZER,
  __module__ = 'protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.Optimizer)
  ))
_sym_db.RegisterMessage(Optimizer)

RMSPropOptimizer = _reflection.GeneratedProtocolMessageType('RMSPropOptimizer', (_message.Message,), dict(
  DESCRIPTOR = _RMSPROPOPTIMIZER,
  __module__ = 'protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.RMSPropOptimizer)
  ))
_sym_db.RegisterMessage(RMSPropOptimizer)

MomentumOptimizer = _reflection.GeneratedProtocolMessageType('MomentumOptimizer', (_message.Message,), dict(
  DESCRIPTOR = _MOMENTUMOPTIMIZER,
  __module__ = 'protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.MomentumOptimizer)
  ))
_sym_db.RegisterMessage(MomentumOptimizer)

AdamOptimizer = _reflection.GeneratedProtocolMessageType('AdamOptimizer', (_message.Message,), dict(
  DESCRIPTOR = _ADAMOPTIMIZER,
  __module__ = 'protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.AdamOptimizer)
  ))
_sym_db.RegisterMessage(AdamOptimizer)

LearningRate = _reflection.GeneratedProtocolMessageType('LearningRate', (_message.Message,), dict(
  DESCRIPTOR = _LEARNINGRATE,
  __module__ = 'protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.LearningRate)
  ))
_sym_db.RegisterMessage(LearningRate)

ConstantLearningRate = _reflection.GeneratedProtocolMessageType('ConstantLearningRate', (_message.Message,), dict(
  DESCRIPTOR = _CONSTANTLEARNINGRATE,
  __module__ = 'protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.ConstantLearningRate)
  ))
_sym_db.RegisterMessage(ConstantLearningRate)

ExponentialDecayLearningRate = _reflection.GeneratedProtocolMessageType('ExponentialDecayLearningRate', (_message.Message,), dict(
  DESCRIPTOR = _EXPONENTIALDECAYLEARNINGRATE,
  __module__ = 'protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.ExponentialDecayLearningRate)
  ))
_sym_db.RegisterMessage(ExponentialDecayLearningRate)

ManualStepLearningRate = _reflection.GeneratedProtocolMessageType('ManualStepLearningRate', (_message.Message,), dict(

  LearningRateSchedule = _reflection.GeneratedProtocolMessageType('LearningRateSchedule', (_message.Message,), dict(
    DESCRIPTOR = _MANUALSTEPLEARNINGRATE_LEARNINGRATESCHEDULE,
    __module__ = 'protos.optimizer_pb2'
    # @@protoc_insertion_point(class_scope:protos.ManualStepLearningRate.LearningRateSchedule)
    ))
  ,
  DESCRIPTOR = _MANUALSTEPLEARNINGRATE,
  __module__ = 'protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.ManualStepLearningRate)
  ))
_sym_db.RegisterMessage(ManualStepLearningRate)
_sym_db.RegisterMessage(ManualStepLearningRate.LearningRateSchedule)

CosineDecayLearningRate = _reflection.GeneratedProtocolMessageType('CosineDecayLearningRate', (_message.Message,), dict(
  DESCRIPTOR = _COSINEDECAYLEARNINGRATE,
  __module__ = 'protos.optimizer_pb2'
  # @@protoc_insertion_point(class_scope:protos.CosineDecayLearningRate)
  ))
_sym_db.RegisterMessage(CosineDecayLearningRate)


# @@protoc_insertion_point(module_scope)
