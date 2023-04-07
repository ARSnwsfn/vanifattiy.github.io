import pytest
import time


@pytest.fixture
def generate_data():
    login = f"autotest_{time.time()}@hyper.org" # Генерирует логин
    password = "512" # Назначает пароль
    return {"login": login, "password": password} # Возвращает логин и пароль