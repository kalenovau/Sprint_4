import pytest as pytest
from selenium import webdriver


@pytest.fixture()
def get_driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture()
def get_user():
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
