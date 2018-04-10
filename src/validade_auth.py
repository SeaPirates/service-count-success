import requests
from flask import json

class ValidadeAuth:

    def __init__(self):
        self.headers = {"Host": "metrics.auth.validate"}
        self.url = "http://metrics.service"

    def validar(self, auth):
        payload = {"auth": auth}
        response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
        return response.json()