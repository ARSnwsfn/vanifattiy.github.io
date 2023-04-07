import pytest


class TestExample:

    def test_1(self, generate_data): # Прокидываем фикстуру в тест и она выполнится перед тестом
        login = generate_data["login"] # Записываем в переменную сгенерированный логин
        password = generate_data["password"] # Записываем в переменную полученный логин