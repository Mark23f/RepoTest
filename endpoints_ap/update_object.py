import requests
from endpoints_ap.base_endpoint import Endpoint


class UpdateObject(Endpoint):

    def update_object(self, obj_id, payload):
        self.response = requests.put(
            f'https://api.restful-api.dev/objects/{obj_id}',
            json=payload
        )
        self.response_json = self.response.json()

    def check_response_name(self, name):
        assert self.response_json['name'] == name
