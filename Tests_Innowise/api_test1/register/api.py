# import requests
#
#
# class Register:
#     def __init__(self, url):
#         self.url = url
#
#     POST_REGISTER_USER = '/register'
#
#     def register_user(self, body: dict, schema: dict):
#         """
#               https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser
#               """
#         response = requests.post(f"{self.url}{self.POST_REGISTER_USER}", json=body)
#         validate(instance=response.json(), schema=schema)
#         return response
import logging
from jsonschema import validate

from vanifattiy_.Tests_Innowise.api_test1.custom_requests import Client
from vanifattiy_.Tests_Innowise.api_test1.register.models import ResponseModel

logger = logging.getLogger("api")

class Register:
    def __init__(self, url):
        self.url = url
        self.client=Client()

    POST_REGISTER_USER = '/register'

    def register_user(self, body: dict, schema: dict):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser
        """
        response = self.client.custom_request("POST", f"{self.url}{self.POST_REGISTER_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())
