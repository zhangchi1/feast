# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from feast.serving import (
    ServingService_pb2 as feast_dot_serving_dot_ServingService__pb2,
)


class ServingServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.GetFeastServingInfo = channel.unary_unary(
            "/feast.serving.ServingService/GetFeastServingInfo",
            request_serializer=feast_dot_serving_dot_ServingService__pb2.GetFeastServingInfoRequest.SerializeToString,
            response_deserializer=feast_dot_serving_dot_ServingService__pb2.GetFeastServingInfoResponse.FromString,
        )
        self.GetOnlineFeatures = channel.unary_unary(
            "/feast.serving.ServingService/GetOnlineFeatures",
            request_serializer=feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesRequest.SerializeToString,
            response_deserializer=feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesResponse.FromString,
        )
        self.GetBatchFeatures = channel.unary_unary(
            "/feast.serving.ServingService/GetBatchFeatures",
            request_serializer=feast_dot_serving_dot_ServingService__pb2.GetBatchFeaturesRequest.SerializeToString,
            response_deserializer=feast_dot_serving_dot_ServingService__pb2.GetBatchFeaturesResponse.FromString,
        )
        self.GetJob = channel.unary_unary(
            "/feast.serving.ServingService/GetJob",
            request_serializer=feast_dot_serving_dot_ServingService__pb2.GetJobRequest.SerializeToString,
            response_deserializer=feast_dot_serving_dot_ServingService__pb2.GetJobResponse.FromString,
        )


class ServingServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def GetFeastServingInfo(self, request, context):
        """Get information about this Feast serving.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetOnlineFeatures(self, request, context):
        """Get online features synchronously.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetBatchFeatures(self, request, context):
        """Get batch features asynchronously.

    The client should check the status of the returned job periodically by
    calling ReloadJob to determine if the job has completed successfully
    or with an error. If the job completes successfully i.e.
    status = JOB_STATUS_DONE with no error, then the client can check
    the file_uris for the location to download feature values data.
    The client is assumed to have access to these file URIs.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetJob(self, request, context):
        """Get the latest job status for batch feature retrieval.
    """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ServingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetFeastServingInfo": grpc.unary_unary_rpc_method_handler(
            servicer.GetFeastServingInfo,
            request_deserializer=feast_dot_serving_dot_ServingService__pb2.GetFeastServingInfoRequest.FromString,
            response_serializer=feast_dot_serving_dot_ServingService__pb2.GetFeastServingInfoResponse.SerializeToString,
        ),
        "GetOnlineFeatures": grpc.unary_unary_rpc_method_handler(
            servicer.GetOnlineFeatures,
            request_deserializer=feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesRequest.FromString,
            response_serializer=feast_dot_serving_dot_ServingService__pb2.GetOnlineFeaturesResponse.SerializeToString,
        ),
        "GetBatchFeatures": grpc.unary_unary_rpc_method_handler(
            servicer.GetBatchFeatures,
            request_deserializer=feast_dot_serving_dot_ServingService__pb2.GetBatchFeaturesRequest.FromString,
            response_serializer=feast_dot_serving_dot_ServingService__pb2.GetBatchFeaturesResponse.SerializeToString,
        ),
        "GetJob": grpc.unary_unary_rpc_method_handler(
            servicer.GetJob,
            request_deserializer=feast_dot_serving_dot_ServingService__pb2.GetJobRequest.FromString,
            response_serializer=feast_dot_serving_dot_ServingService__pb2.GetJobResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "feast.serving.ServingService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
