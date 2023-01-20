import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage


# @allure.feature("Кнопка заказа на главной")
# @allure.suite("проверка кнопки заказа")
# @allure.title("тест на проверку кнопки заказа в шапке")
@allure.description("Проверка верхней кнопки Оформить заказ")
def test_click_on_the_order_button_up_open_order_page(get_driver):
    driver = get_driver
    main_page = MainPage(driver)
    order_page = OrderPage(driver)
    main_page.click_order_button_up()
    order_page.wait_order_page()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

# @allure.feature("Кнопка заказа на главной")
# @allure.suite("проверка кнопки заказа")
# @allure.title("тест на проверку кнопки заказа в теле страницы")
@allure.description("Проверка нижней кнопки Оформить заказ")
def test_click_on_the_order_button_down_open_order_page(get_driver):
    driver = get_driver
    order_page = OrderPage(driver)
    main_page = MainPage(driver)
    main_page.scroll_to_order_button_down()
    main_page.click_order_button_down()
    order_page.wait_order_page()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

# @allure.feature("Оформление заказа")
# @allure.suite("полный заказ")
# @allure.title("полный тест на проверку создания заказа")
@allure.description("Проверка сценария оформления заказа")
def test_order_success(get_driver, get_user):
    driver = get_driver
    order_page = OrderPage(driver)
    driver.get("https://qa-scooter.praktikum-services.ru/order")
    order_page.fill_order_full(get_user)
    assert order_page.check_confirm_order()
