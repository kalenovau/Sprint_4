import pytest as pytest
from selenium import webdriver


@pytest.fixture()
def get_driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture()
def get_user_1():
    user = {
        "Name": "Имя",
        "LastName": "Фамилия",
        "Address": "Адрес",
        "Metro": "Черкизовская",
        "Phone": "77007700770",
        "day": "сутки",
        "comment": "no_comments"
    }
    return user

@pytest.fixture()
def get_user_2():
    user = {
        "Name": "Имядва",
        "LastName": "Фамилиядва",
        "Address": "Адресдва",
        "Metro": "Лубянка",
        "Phone": "77008800880",
        "day": "двое суток",
        "comment": "ноу комментс"
    }
    return user
