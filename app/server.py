from concurrent import futures
import time

import grpc

import app.helloworld_pb2 as helloworld_pb2
import app.helloworld_pb2_grpc as helloworld_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def Greet(self, request, context):
        print('Saying `hello` to %s' % request.name)
        return helloworld_pb2.GreetResponse(message='Hello, {}!'.format(request.name))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
