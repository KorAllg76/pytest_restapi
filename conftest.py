import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DelObject

@pytest.fixture()
def obj_id():
    create_object = CreateObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2048,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_object.new_object(payload)
    yield create_object.response_json['id']
    delete_object = DelObject()
    delete_object.del_by_id(create_object.response_json['id'])

@pytest.fixture()
def obj_id_2():
    create_object = CreateObject()
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2048,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_object.new_object(payload)
    yield create_object.response_json['id']
    delete_object = DelObject()
    delete_object.del_by_id(create_object.response_json['id'])