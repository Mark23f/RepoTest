import requests
from endpoints_ap.base_endpoint import Endpoint
import allure


class CreateObject(Endpoint):

    # Для примера новый метод, который будет как подметод в аллюре

    @allure.step('read JSON')
    def read_json(self, response):
        return response.json()

    def new_object(self, payload):
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
       # Вернуть, если убрать функцию read_json
       #self.response_json = self.response.json()
        self.response = self.read_json(self.response)




    def check_name(self, name):
        assert self.response_json['name'] == name
