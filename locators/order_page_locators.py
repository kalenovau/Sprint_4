from selenium.webdriver.common.by import By

# Страница заказа 1
# Заголовок Для кого самокат
order_header = [By.XPATH, "//*[text()='Для кого самокат']"]

# Поле Имя
name_field = [By.XPATH, "//input[@placeholder='* Имя']"]

# Поле Фамилия
second_name_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]

# Поле Адрес: куда привезти заказ
address_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]

# Поле выбора метро
subway_field = [By.XPATH, "//div[@class='select-search__value']"]

# Поле Станция метро
subway_station = [By.XPATH, "//input[@placeholder='* Станция метро']"]

# Выпадающий список выбора метро
subway_list = [By.XPATH, "//div[@class='select-search__select']"]

# Выпадающий список станций метро
subway_list = [By.XPATH, "//div[@class='select-search__select']"]

# Поле Телефон: на него позвонит курьер
phone_number_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

# кнопка далее
next_button = [By.XPATH, "//button[text()='Далее']"]

# Страница заказа 2
# Заголовок второй страницы "Про аренду"
order_header_second = [By.XPATH, "//*[text()='Про аренду']"]

# Поле Когда привезти самокат
field_date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]

# Календарь
calendar = [By.XPATH, "//div[contains(@class'react-datepicker__day')]"]

# Поле срок аренды
rent_time = [By.XPATH, "//div[text()='* Срок аренды']"]

# Поле цвет самоката
checkbox_color_black = [By.ID, "black"]
checkbox_color_gray = [By.ID, "grey"]

# Поле Комментарий для курьера
field_comment = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

# Кнопка Заказать
order_button = [By.XPATH, "//button[contains(@class,'Middle') and text()='Заказать']"]

# Кнопка подтверждения заказа "Да"
yes_button = [By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Да']"]

# Кнопка подтверждения заказа "Нет"
no_button = [By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Нет']"]

# Заголовок Заказ оформлен
header_order_confirmed = [By.XPATH, "//div[text()='Заказ оформлен']"]
