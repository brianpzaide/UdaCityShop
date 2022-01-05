#!/usr/bin/python

import os
import random
import time
import random
import traceback
from concurrent import futures

import grpc

from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc

import demo_pb2
import demo_pb2_grpc

from logger import getJSONLogger
logger = getJSONLogger('adservice-v2-server')


class AdServiceV2(demo_pb2_grpc.AdserviceV2Servicer, health_pb2_grpc.HealthServicer):
    # Implemet the Ad service business logic
    
    def GetAdsV2(self, request, context):
        channel = grpc.insecure_channel("productcatalogservice:3550")
        client = demo_pb2_grpc.ProductCatalogServiceStub(channel)
        response = stub.ListProducts(demo_pb2.Empty())
        random_products = random.sample(response.products, k=random.randint(1,5))
        random_ads = [demo_pb2.Ad(redirect_url=f'/product/{p.id}', text=f"AdV2 - Items with {5*random.randint(1,10)}% Discount!") for p in random_products]
        return demo_pb2.AdResponse(ads=random_ads)
        
    
    # Note: These are needed for the liveness and readiness probes
    def Check(self, request, context):
        return health_pb2.HealthCheckResponse(status=health_pb2.HealthCheckResponse.SERVING)
    def Watch(self, request, context):
        return health_pb2.HealthCheckResponse(status=health_pb2.HealthCheckResponse.UNIMPLEMENTED)


if __name__ == "__main__":
    logger.info("initializing adservice-v2")
    
    # create gRPC server, add the Ad-v2 service and start it
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    demo_pb2_grpc.add_AdServiceV2Servicer_to_server(AdServiceV2(), server)
    
    health_pb2_grpc.add_HealthServicer_to_server(service, server)

    server.add_insecure_port("[::]:9556")
    server.start()
    server.wait_for_termination()
