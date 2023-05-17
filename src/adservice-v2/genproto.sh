#!/bin/bash -eu

set -e

# TODO: Add the commands to generate the gRPC files
python -m grpc_tools.protoc -I ./proto --python_out=. --grpc_python_out=. ./proto/demo.proto