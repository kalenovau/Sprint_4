import allure
#import locators.header_locators as header
import locators.common_locators as common


class CommonElements:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажатие лого Самокат")
    def click_scooter_logo(self):
        self.driver.find_element(*common.scooter_logo).click()

    @allure.step("Нажатие лого Яндекс")
    def click_logo_yandex(self):
        self.driver.find_element(*common.yandex_logo).click()
