#!/usr/bin/python

import sys
import grpc

import demo_pb2
import demo_pb2_grpc

from logger import getJSONLogger
logger = getJSONLogger('adservice-v2-server')

if __name__ == "__main__":
    # set up server stub
    channel = grpc.insecure_channel("localhost:9556")
    client = demo_pb2_grpc.AdServiceV2Stub(channel)
     
    # form a request with the required input
    req = demo_pb2.AdRequest(context_keys=["test"])
    
    # make a call to server and return a response
    res = client.GetAdsV2(req)
    
    logger.info(res)
