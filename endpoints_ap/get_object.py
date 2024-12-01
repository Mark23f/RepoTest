import requests
from endpoints_ap.base_endpoint import Endpoint


class GetObject(Endpoint):

    def get_by_id(self, obj_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
        self.response_json = self.response.json()

    def check_response_id(self, obj_id):
        assert self.response_json['id'] == obj_id

    def check_response_400(self):
        assert self.response.status_code == 400 or 401 or 403
