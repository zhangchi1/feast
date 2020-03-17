# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from typing import Iterable as typing___Iterable
from typing import Optional as typing___Optional
from typing import Text as typing___Text
from typing import Union as typing___Union

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.timestamp_pb2 import (
    Timestamp as google___protobuf___timestamp_pb2___Timestamp,
)
from typing_extensions import Literal as typing_extensions___Literal

from feast.types.Field_pb2 import Field as feast___types___Field_pb2___Field

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class FeatureRow(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    feature_set = ...  # type: typing___Text
    @property
    def fields(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        feast___types___Field_pb2___Field
    ]: ...
    @property
    def event_timestamp(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
    def __init__(
        self,
        *,
        fields: typing___Optional[
            typing___Iterable[feast___types___Field_pb2___Field]
        ] = None,
        event_timestamp: typing___Optional[
            google___protobuf___timestamp_pb2___Timestamp
        ] = None,
        feature_set: typing___Optional[typing___Text] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FeatureRow: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> FeatureRow: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal["event_timestamp", b"event_timestamp"],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "event_timestamp",
            b"event_timestamp",
            "feature_set",
            b"feature_set",
            "fields",
            b"fields",
        ],
    ) -> None: ...
