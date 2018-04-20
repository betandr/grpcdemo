from __future__ import print_function

import grpc

import app.helloworld_pb2 as helloworld_pb2
import app.helloworld_pb2_grpc as helloworld_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)

    response = stub.Greet(helloworld_pb2.GreetRequest(name='World'))
    print("Received: " + response.message)


if __name__ == '__main__':
    run()
