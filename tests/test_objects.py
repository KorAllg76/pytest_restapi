#from http.client import responses
from os import path

import requests
import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.put_object import PutObject
from endpoints.delete_object import DelObject

payload = {
    "name": "Apple MacBook Pro 22",
    "data": {
        "year": 2032,
        "price": 1849.99,
        "CPU model": "Intel Core i_11",
        "Hard disk size": "1 TB"
    }
}

def test_creat_object():
    new_object_endpoint = CreateObject()
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_response_is_200()
    new_object_endpoint.check_name(payload['name'])

def test_get_object(obj_id_2):
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id_2)
    get_obj_endpoint.check_response_is_200()
    get_obj_endpoint.check_response_id(obj_id_2)

def test_put_object(obj_id):
    put_obj_endpoint = PutObject()

    put_obj_endpoint.put_by_id(obj_id, payload)
    put_obj_endpoint.check_response_is_200()
    put_obj_endpoint.check_response_name(payload['name'])

def test_del_object(obj_id):
    del_obj_endpoint = DelObject()
    del_obj_endpoint.del_by_id(obj_id)
    del_obj_endpoint.check_response_is_200()

 #   get_obj_endpoint = GetObject()
 #   get_obj_endpoint.get_by_id(obj_id)
 #   get_obj_endpoint.check_response_id(obj_id)




