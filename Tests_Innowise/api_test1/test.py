from vaniffatiy_.Tests_Innowise.api_test1 import Register
from vaniffatiy_.Tests_Innowise.api_test1 import RegisterUser
from vaniffatiy_.Tests_Innowise.api_test1 import valid_schema

URL = "https://stores-tests-api.herokuapp.com"


class TestRegistration:
    def test_registration(self):
        body = RegisterUser.random()
        response = Register(url=URL).register_user(body=body, schema=valid_schema)
        assert response.status == 201
        assert response.response.get('message') == 'User created successfully.'
        assert response.response.get('uuid')
        