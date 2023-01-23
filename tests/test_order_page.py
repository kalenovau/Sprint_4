import time

import allure
import pytest
from selenium import webdriver
from pages.order_page import OrderPage
from pages.main_page import MainPage


class TestOrder:
    driver = None

    @allure.description("Открытие браузера")
    def setup_class_1 (cls1):
        cls1.driver = webdriver.Firefox()
        cls1.driver.get("https://qa-scooter.praktikum-services.ru/")

    @allure.description("Проверка верхней кнопки Оформить заказ")
    def test_click_on_the_order_button_up_open_order_page(cls1, get_driver):
        driver = get_driver
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_order_button_up()
        order_page.wait_order_page()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

    @allure.description("Проверка нижней кнопки Оформить заказ")
    def test_click_on_the_order_button_down_open_order_page(cls1, get_driver):
        driver = get_driver
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.scroll_to_order_button_down()
        main_page.click_order_button_down()
        order_page.wait_order_page()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"

    @allure.description("Проверка сценария оформления заказа через верхнюю кнопку")
    def test_order_success(cls1, get_driver, get_user_1):
        driver = get_driver
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_order_button_up()
        order_page.fill_order_full_1(get_user_1)
        assert order_page.check_confirm_order()

    @allure.description("Проверка сценария оформления заказа через нижнюю кнопку")
    def test_order_success_2(cls1, get_driver, get_user_2):
        driver = get_driver
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.scroll_to_order_button_down()
        main_page.click_order_button_down()
        order_page.fill_order_full_2(get_user_2)
        assert order_page.check_confirm_order()
