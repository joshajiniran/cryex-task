COMPOSE = docker-compose -f docker-compose.yml

SERVICE = script

build:
	$(COMPOSE) up --build

run:
	locust -f scripts/locustfile.py

gen:
	python -m grpc_tools.protoc --proto_path=protos --python_out=protobufs --grpc_python_out=protobufs  protos/*.proto

clean:
	rm protobufs/*.py && touch protobufs/__init__.py