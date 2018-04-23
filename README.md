# gRPC Python Demo

Python client-server demo using [gRPC](https://grpc.io/) and
[protocol buffers](https://developers.google.com/protocol-buffers/docs/overview)

- Service defined in a [helloworld.proto](helloworld.proto) file.
- Server and client code generated with the protocol buffer compiler.
- Simple [client](client.py) and [server](server.py) implemented with Python gRPC API.

## Install dependencies
```
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

## Generate code from the service definition
```
python -m grpc_tools.protoc \
  -I. \
  --python_out=. \
  --grpc_python_out=. \
  ./helloworld.proto
```

## Start the server
```
python3 app/server.py
```

## Run the client
```
python3 app/client.py
```

## Run tests
```
pip install -r requirements_text.txt
py.test tests/
```
