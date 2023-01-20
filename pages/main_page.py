from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.main_page_locators as main_page
import allure


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Скроллинг к разделу Вопросы о важном")
    def scroll_to_questions(self):
        element = self.driver.find_element(*main_page.questions_header)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("прокручиваем страницу до кнопки Заказа в теле страницы")
    def scroll_to_order_button_down(self):
        element = self.driver.find_element(*main_page.order_button_down)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("кликаем по названию в списке: {name_list}")
    def click_accordion_name_by_text(self, name_list):
        elem = self.driver.find_element(By.XPATH, f"//div[text()='{name_list}']")
        elem.click()

    @allure.step("проверяем доступность элемента: {text_accordion_panel}")
    def get_len_elem_by_text(self, text_accordion_panel):
        elems = self.driver.find_elements(By.XPATH, f"//div[not (@hidden)]/p[text()='{text_accordion_panel}']")
        return len(elems) == 1

    @allure.step("клик по верхней кнопке заказать")
    def click_order_button_up(self):
        self.driver.find_element(*main_page.order_button_up).click()

    @allure.step("клик по нижней кнопке заказать")
    def click_order_button_down(self):
        self.driver.find_element(*main_page.order_button_down).click()

    @allure.step("проверка содержания {expect_url} в {current_url}")
    def check_current_url(self, current_url, expect_url):
        return expect_url in current_url

    @allure.step("Проверка загрузки страницы")
    def check_load_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(main_page.order_button_down))
