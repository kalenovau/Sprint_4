import datetime
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.order_page_locators as order_page


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание локатора: {elem}")
    def wait_element_visible(self, elem):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(elem))

    @allure.step("Ввод имени: {name}")
    def input_name_field(self, name):
        self.driver.find_element(*order_page.name_field).send_keys(name)

    @allure.step("Ввод фамилии: {second_name}")
    def input_second_name(self, second_name):
        self.driver.find_element(*order_page.second_name_field).send_keys(second_name)

    @allure.step("Нажатие на поле выбора станций метро")
    def click_subway_field(self):
        self.driver.find_element(*order_page.subway_station).click()

    # ввод номера телефона
    @allure.step("Ввод номера телефона: {phone}")
    def input_phone_number(self, phone):
        self.driver.find_element(*order_page.phone_number_field).send_keys(phone)

    @allure.step("Ввод адреса: {address}")
    def input_address(self, address):
        self.driver.find_element(*order_page.address_field).send_keys(address)

    @allure.step("Ввод названия станции метро: {name_subway}")
    def input_subway_name(self, name_subway):
        self.driver.find_element(*order_page.subway_station).send_keys(name_subway)

    # выбор станции метро
    @allure.step("Выбор по станции метро по названию: {name_subway}")
    def select_subway(self, name_subway):
        self.driver.find_element(By.XPATH, f"//li[@class='select-search__row']//div[contains(text(),'{name_subway}')]").click()

    @allure.step("Нажатие кнопки Далее")
    def click_on_next_button(self):
        self.driver.find_element(*order_page.next_button).click()

    @allure.step("Проверка перехода на вторую страницу оформдения заказа")
    def check_second_page_order(self):
        return len(self.driver.find_elements(*order_page.order_header_second)) == 1

    @allure.step("Выбор даты")
    def select_current_day(self):
        self.driver.find_element(*order_page.field_date).click()
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='react-datepicker__tab-loop']")))
        self.driver.find_element(By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{datetime.datetime.today().day}']").click()

    @allure.step("Выбор времени аренды")
    def select_rent_ours(self, ours):
        self.driver.find_element(*order_page.rent_time).click()
        self.driver.find_element(By.XPATH, f"//div[@class = 'Dropdown-option' and text()='{ours}']").click()

    @allure.step("Выбор серого цвета")
    def select_black_color(self):
        self.driver.find_element(*order_page.checkbox_color_black).click()

    @allure.step("Выбор серого цвета")
    def select_gray_color(self):
        self.driver.find_element(*order_page.checkbox_color_gray).click()

    @allure.step("Ввод комментария для курьера")
    def input_comment_for_courier(self, comment):
        self.driver.find_element(*order_page.field_comment).send_keys(comment)

    @allure.step("Подтверждение заказа")
    def press_button_order(self):
        self.driver.find_element(*order_page.order_button).click()

    @allure.step("Нажатие кнопки Да")
    def press_button_yes(self):
        self.driver.find_element(*order_page.yes_button).click()

    # метод для заполнения полей для заказа пользователя 1
    def fill_order_full_1(self, get_user_1):
        self.wait_element_visible(order_page.name_field)
        self.input_name_field(get_user_1["Name"])
        self.input_second_name(get_user_1["LastName"])
        self.input_address(get_user_1["Address"])
        self.input_phone_number(get_user_1["Phone"])
        self.input_subway_name(get_user_1["Metro"])
        self.select_subway(get_user_1["Metro"])
        self.click_on_next_button()
        self.select_current_day()
        self.select_rent_ours(get_user_1["day"])
        self.select_gray_color()
        self.input_comment_for_courier(get_user_1["comment"])
        self.press_button_order()
        self.press_button_yes()

    # метод для заполнения полей для заказа пользователя 2
    def fill_order_full_2(self, get_user_2):
        self.wait_element_visible(order_page.name_field)
        self.input_name_field(get_user_2["Name"])
        self.input_second_name(get_user_2["LastName"])
        self.input_address(get_user_2["Address"])
        self.input_phone_number(get_user_2["Phone"])
        self.input_subway_name(get_user_2["Metro"])
        self.select_subway(get_user_2["Metro"])
        self.click_on_next_button()
        self.select_current_day()
        self.select_rent_ours(get_user_2["day"])
        self.select_black_color()
        self.input_comment_for_courier(get_user_2["comment"])
        self.press_button_order()
        self.press_button_yes()

    @allure.step("Проверка завершения оформления заказа")
    def check_confirm_order(self):
        return len(self.driver.find_elements(*order_page.header_order_confirmed)) == 1

    @allure.step("Проверка загрузки страницы с итогом заказа")
    def wait_order_page(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(order_page.order_header))
