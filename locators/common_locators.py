from selenium.webdriver.common.by import By

# Лого Самокат
scooter_logo = [By.XPATH, "//*[@alt='Scooter']"]

# Лого Яндекс
yandex_logo = [By.XPATH, "//*[@alt='Yandex']"]

# Поле Введите номер заказа
field_order_number = [By.XPATH, "//input[@type='text' and @placeholder='Введите номер заказа']"]

# Кнопка Go
button_go = [By.XPATH, "//button[text()='Go!']"]



# попробовать сократить икспас Кнопка Статус заказа
button_order_status = [By.XPATH, "//div[contains(@class,'Header')]/button[text()='Статус заказа']"]



