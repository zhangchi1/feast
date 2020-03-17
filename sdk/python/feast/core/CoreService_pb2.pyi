# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from typing import Iterable as typing___Iterable
from typing import List as typing___List
from typing import Optional as typing___Optional
from typing import Text as typing___Text
from typing import Tuple as typing___Tuple
from typing import Union as typing___Union
from typing import cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from feast.core.FeatureSet_pb2 import (
    FeatureSet as feast___core___FeatureSet_pb2___FeatureSet,
)
from feast.core.Store_pb2 import Store as feast___core___Store_pb2___Store

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class GetFeatureSetRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    project = ...  # type: typing___Text
    name = ...  # type: typing___Text
    version = ...  # type: builtin___int
    def __init__(
        self,
        *,
        project: typing___Optional[typing___Text] = None,
        name: typing___Optional[typing___Text] = None,
        version: typing___Optional[builtin___int] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetFeatureSetRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> GetFeatureSetRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "name", b"name", "project", b"project", "version", b"version"
        ],
    ) -> None: ...

class GetFeatureSetResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def feature_set(self) -> feast___core___FeatureSet_pb2___FeatureSet: ...
    def __init__(
        self,
        *,
        feature_set: typing___Optional[
            feast___core___FeatureSet_pb2___FeatureSet
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetFeatureSetResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> GetFeatureSetResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["feature_set", b"feature_set"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["feature_set", b"feature_set"]
    ) -> None: ...

class ListFeatureSetsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Filter(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        project = ...  # type: typing___Text
        feature_set_name = ...  # type: typing___Text
        feature_set_version = ...  # type: typing___Text
        def __init__(
            self,
            *,
            project: typing___Optional[typing___Text] = None,
            feature_set_name: typing___Optional[typing___Text] = None,
            feature_set_version: typing___Optional[typing___Text] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> ListFeatureSetsRequest.Filter: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> ListFeatureSetsRequest.Filter: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "feature_set_name",
                b"feature_set_name",
                "feature_set_version",
                b"feature_set_version",
                "project",
                b"project",
            ],
        ) -> None: ...
    @property
    def filter(self) -> ListFeatureSetsRequest.Filter: ...
    def __init__(
        self, *, filter: typing___Optional[ListFeatureSetsRequest.Filter] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListFeatureSetsRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ListFeatureSetsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["filter", b"filter"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["filter", b"filter"]
    ) -> None: ...

class ListFeatureSetsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def feature_sets(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        feast___core___FeatureSet_pb2___FeatureSet
    ]: ...
    def __init__(
        self,
        *,
        feature_sets: typing___Optional[
            typing___Iterable[feast___core___FeatureSet_pb2___FeatureSet]
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListFeatureSetsResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ListFeatureSetsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["feature_sets", b"feature_sets"]
    ) -> None: ...

class ListStoresRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Filter(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ...  # type: typing___Text
        def __init__(
            self, *, name: typing___Optional[typing___Text] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ListStoresRequest.Filter: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> ListStoresRequest.Filter: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions___Literal["name", b"name"]
        ) -> None: ...
    @property
    def filter(self) -> ListStoresRequest.Filter: ...
    def __init__(
        self, *, filter: typing___Optional[ListStoresRequest.Filter] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListStoresRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ListStoresRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["filter", b"filter"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["filter", b"filter"]
    ) -> None: ...

class ListStoresResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def store(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        feast___core___Store_pb2___Store
    ]: ...
    def __init__(
        self,
        *,
        store: typing___Optional[
            typing___Iterable[feast___core___Store_pb2___Store]
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListStoresResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ListStoresResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["store", b"store"]
    ) -> None: ...

class ApplyFeatureSetRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def feature_set(self) -> feast___core___FeatureSet_pb2___FeatureSet: ...
    def __init__(
        self,
        *,
        feature_set: typing___Optional[
            feast___core___FeatureSet_pb2___FeatureSet
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ApplyFeatureSetRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ApplyFeatureSetRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["feature_set", b"feature_set"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["feature_set", b"feature_set"]
    ) -> None: ...

class ApplyFeatureSetResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Status(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> "ApplyFeatureSetResponse.Status": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["ApplyFeatureSetResponse.Status"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "ApplyFeatureSetResponse.Status"]
        ]: ...
        NO_CHANGE = typing___cast("ApplyFeatureSetResponse.Status", 0)
        CREATED = typing___cast("ApplyFeatureSetResponse.Status", 1)
        ERROR = typing___cast("ApplyFeatureSetResponse.Status", 2)
    NO_CHANGE = typing___cast("ApplyFeatureSetResponse.Status", 0)
    CREATED = typing___cast("ApplyFeatureSetResponse.Status", 1)
    ERROR = typing___cast("ApplyFeatureSetResponse.Status", 2)

    status = ...  # type: ApplyFeatureSetResponse.Status
    @property
    def feature_set(self) -> feast___core___FeatureSet_pb2___FeatureSet: ...
    def __init__(
        self,
        *,
        feature_set: typing___Optional[
            feast___core___FeatureSet_pb2___FeatureSet
        ] = None,
        status: typing___Optional[ApplyFeatureSetResponse.Status] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ApplyFeatureSetResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ApplyFeatureSetResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["feature_set", b"feature_set"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "feature_set", b"feature_set", "status", b"status"
        ],
    ) -> None: ...

class GetFeastCoreVersionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetFeastCoreVersionRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> GetFeastCoreVersionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class GetFeastCoreVersionResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    version = ...  # type: typing___Text
    def __init__(
        self, *, version: typing___Optional[typing___Text] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetFeastCoreVersionResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> GetFeastCoreVersionResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["version", b"version"]
    ) -> None: ...

class UpdateStoreRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def store(self) -> feast___core___Store_pb2___Store: ...
    def __init__(
        self, *, store: typing___Optional[feast___core___Store_pb2___Store] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateStoreRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> UpdateStoreRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["store", b"store"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["store", b"store"]
    ) -> None: ...

class UpdateStoreResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Status(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> "UpdateStoreResponse.Status": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["UpdateStoreResponse.Status"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "UpdateStoreResponse.Status"]
        ]: ...
        NO_CHANGE = typing___cast("UpdateStoreResponse.Status", 0)
        UPDATED = typing___cast("UpdateStoreResponse.Status", 1)
    NO_CHANGE = typing___cast("UpdateStoreResponse.Status", 0)
    UPDATED = typing___cast("UpdateStoreResponse.Status", 1)

    status = ...  # type: UpdateStoreResponse.Status
    @property
    def store(self) -> feast___core___Store_pb2___Store: ...
    def __init__(
        self,
        *,
        store: typing___Optional[feast___core___Store_pb2___Store] = None,
        status: typing___Optional[UpdateStoreResponse.Status] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateStoreResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> UpdateStoreResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["store", b"store"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["status", b"status", "store", b"store"],
    ) -> None: ...

class CreateProjectRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ...  # type: typing___Text
    def __init__(self, *, name: typing___Optional[typing___Text] = None,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateProjectRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> CreateProjectRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["name", b"name"]
    ) -> None: ...

class CreateProjectResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateProjectResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> CreateProjectResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class ArchiveProjectRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ...  # type: typing___Text
    def __init__(self, *, name: typing___Optional[typing___Text] = None,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ArchiveProjectRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ArchiveProjectRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["name", b"name"]
    ) -> None: ...

class ArchiveProjectResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ArchiveProjectResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ArchiveProjectResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class ListProjectsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListProjectsRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ListProjectsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class ListProjectsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    projects = (
        ...
    )  # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    def __init__(
        self, *, projects: typing___Optional[typing___Iterable[typing___Text]] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListProjectsResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ListProjectsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["projects", b"projects"]
    ) -> None: ...
