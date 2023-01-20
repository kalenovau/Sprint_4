from selenium.webdriver.common.by import By

# Заголовок Вопросы о важном
questions_header = [By.XPATH, "//div[text()='Вопросы о важном']"]

# Кнопка Заказать вверху страницы
order_button_up = [By.XPATH, "//div[contains(@class,'Header')]/button[text()='Заказать']"]

# Кнопка Заказать внизу страницы
order_button_down = [By.XPATH, "//button[contains(@class,'Middle') and text()='Заказать']"]





# нужно ли оно изображение самоката на главной странице
image_on_main_page = [By.XPATH, "//img[@src='/assets/ya.svg']"]
