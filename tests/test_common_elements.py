from time import sleep
import allure
from pages.main_page import MainPage
from pages.common_elements import CommonElements


@allure.title("Проверка перехода на главную страницу")
def test_click_logo_scooter_open_main_page(get_driver):
    driver = get_driver
    common_elements = CommonElements(driver)
    main_page = MainPage(driver)
    driver.get("https://qa-scooter.praktikum-services.ru/order")
    common_elements.click_scooter_logo()
    main_page.check_load_page()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

@allure.title("Проверка перехода на dzen")
def test_click_logo_yandex_open_dzen(get_driver):
    driver = get_driver
    common_elements = CommonElements(driver)
    main_page = MainPage(driver)
    common_elements.click_logo_yandex()
    sleep(5)
    driver.switch_to.window(driver.window_handles[-1])
    assert main_page.check_current_url(driver.current_url, "https://dzen.ru")
