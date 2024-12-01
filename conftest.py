import pytest
import requests
from endpoints_ap.create_object import CreateObject
from endpoints_ap.delete_object import DeleteObject


@pytest.fixture()
def obj_id():
    create_object = CreateObject()
    payload = {
        "name": "Apple Mackbook Pro",
        "data": {
            "year": 2019,
            "price": 1849.00,
            "CPU model": "Intel Core I9",
            "Hard disk size": "1 TB"

        }
    }
    create_object.new_object(payload)
    #responce = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    #Возвращает значение в obj_id
    #return responce['id']
    #yield responce['id']   #- это как постусловие
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_object(create_object.response_json['id'])
    #requests.delete(f"https://api.restful-api.dev/objects/{responce['id']}")
    #-после того,как будет выполнена obj_id до request.delete возвратится в def функцию какую-либо ниже
    # и после ее завершения еще и выполнит request.delete( удалит этот id, который передал ранее - это постусловие

