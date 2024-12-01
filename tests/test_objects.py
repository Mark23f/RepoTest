from endpoints_ap.get_object import GetObject
from endpoints_ap.update_object import UpdateObject
from endpoints_ap.delete_object import DeleteObject
from endpoints_ap.create_object import CreateObject
import allure

# в терминале создаю папку для файлов результатов pytest -v -s --alluredir results
# далее формирую файлы с результатами в этой папке - allure serve results
# если надо отдельным файлом сгенерить, то allure generate results => переход Report successfully generated
#  to allure-report


# @pytest.fixture()
# def obj_id():
#     payload = {
#         "name": "Apple Mackbook Pro",
#         "data": {
#             "year": 2019,
#             "price": 1849.00,
#             "CPU model": "Intel Core I9",
#             "Hard disk size": "1 TB"
#
#         }
#     }
#     response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
#     #Возвращает значение в obj_id
#     #return responce['id']
#     yield response['id']   #- это как постусловие
#     requests.delete(f"https://api.restful-api.dev/objects/{response['id']}")
#     #-после того,как будет выполнена obj_id до request.delete возвратится в def функцию какую-либо ниже
#     # и после ее завершения еще и выполнит request.delete( удалит этот id, который передал ранее - это постусловие
#

# Создание объекта
@allure.feature('Create USER')
@allure.story('creatable')
def test_create_object():
    new_object_endpoint = CreateObject()
    payload = {
        "name": "Apple Mackbook Pro",
        "data": {
            "year": 2019,
            "price": 1849.00,
            "CPU model": "Intel Core I9",
            "Hard disk size": "1 TB"

        }
    }
    with allure.step('Crete new object'):
        new_object_endpoint.new_object(payload=payload)
    with allure.step('Check that status is 200'):
        new_object_endpoint.check_response_is_200()
    with allure.step('Check that name is correct'):
        new_object_endpoint.check_name(payload['name'])


# Получение статуса
@allure.feature('Get USER')
@allure.story('getable')
def test_get_object(obj_id):
    get_obj_endpoint = GetObject()

    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_response_is_200()
    get_obj_endpoint.check_response_id(obj_id)


# Изменение статуса

def test_update_object(obj_id):
    update_obj_endpoint = UpdateObject()
    payload = {
        "name": "Apple Mackbook Pro 15",
        "data": {
            "year": 2023,
            "price": 2000.00,
            "CPU model": "Intel Core I3",
            "Hard disk size": "5 TB"

        }
    }
    update_obj_endpoint.update_object(obj_id=obj_id, payload=payload)
    update_obj_endpoint.check_response_is_200()
    update_obj_endpoint.check_response_name(payload['name'])


def test_delete_object(obj_id):
    # Идет удаление запроса на удаление, а после проверка на get,что после get нет такого объекта =404
    # obj_id= create_object()
    delete_object_endpoint = DeleteObject()
    delete_object_endpoint.delete_object(obj_id)
    delete_object_endpoint.check_response_is_200()
    get_object_endpoint = GetObject()
    get_object_endpoint.get_by_id(obj_id)
    get_object_endpoint.check_response_400()
