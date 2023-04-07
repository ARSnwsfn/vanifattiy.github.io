import pytest
import requests
import json

# тест на создание пользователя и проверку успешного создания
def test create_user():
    user = {"name": "Fred”, "age": 25, "mail":"fr@mal.com", "password": "134513"}
    url = "http://localhost/users/”
    r = requests.post(url, data=user)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('ERROR: %s' % e)
    assert r.text == "Ok"

import requests


