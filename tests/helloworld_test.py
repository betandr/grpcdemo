from unittest import TestCase
from unittest.mock import patch
from unittest.mock import Mock

import grpc

from concurrent import futures

import app.helloworld_pb2 as helloworld_pb2
import app.helloworld_pb2_grpc as helloworld_pb2_grpc

from app.server import Greeter


class RPCTest(TestCase):

    def setUp(self):
        self._server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), self._server)
        self._server.add_insecure_port('[::]:50051')
        self._server.start()

        self._channel = grpc.insecure_channel('localhost:50051')
        self._stub = helloworld_pb2_grpc.GreeterStub(self._channel)

        self._context = Mock()
        self._greeter = Greeter()

    def tearDown(self):
        self._server.stop(None)

    def test_greet_with_server(self):
        response = self._stub.Greet(helloworld_pb2.GreetRequest(name='Test'))
        assert(response.message == "Hello, Test!")

    def test_greet_with_mock(self):
        response = self._greeter.Greet(request=helloworld_pb2.GreetRequest(name='Test'), context=self._context)
        assert (response.message == "Hello, Test!")


