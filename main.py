import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Настройки для браузера Firefox
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--start-maximized')
driver = webdriver.Firefox(options=firefox_options)

# Открыть сайт
driver.get('https://demo.opencart-ru.ru/index.php?route=common/home')

time.sleep(1.5)

# Кликнуть на элемент слайд-шоу
slideshow_element = driver.find_element(By.XPATH, "//div[@id='slideshow0']")
slideshow_element.click()

time.sleep(1.5)

# Кликнуть на второе изображение в списке
image_element = driver.find_element(By.XPATH, "//li[2]//a[1]//img[1]")
image_element.click()

time.sleep(0.5)

# Кликнуть дважды на кнопку "Next"
next_button = driver.find_element(By.XPATH, "//button[@title='Next (Right arrow key)']")
next_button.click()
next_button.click()

time.sleep(1.5)
driver.back()

time.sleep(1.5)

# Навести курсор на раздел "Компьютеры"
actions = ActionChains(driver)
computers_menu = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle'][contains(text(),'Компьютеры')]")
actions.move_to_element(computers_menu).perform()

time.sleep(1.5)

# Кликнуть на подменю "PC (0)"
pc_submenu = driver.find_element(By.XPATH, "//a[normalize-space()='PC (0)']")
pc_submenu.click()

time.sleep(1)
driver.back()

time.sleep(1.5)

# Кликнуть на иконку "Личный кабинет"
account_icon = driver.find_element(By.XPATH, "//a[@title='Личный кабинет']")
account_icon.click()

time.sleep(1.5)

# Кликнуть на ссылку "Регистрация"
register_link = driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[contains(text(),'Регистрация')]")
register_link.click()

time.sleep(1.5)

# Заполнение формы регистрации
email_input = driver.find_element(By.XPATH, "//input[@id='register_email']")
email_input.send_keys("kosegarov@yandex.ru")
time.sleep(0.5)

password_input = driver.find_element(By.XPATH, "//input[@id='register_password']")
password_input.send_keys("123456789")
time.sleep(0.5)

confirm_password_input = driver.find_element(By.XPATH, "//input[@id='register_confirm_password']")
confirm_password_input.send_keys("123456789")
time.sleep(0.5)

firstname_input = driver.find_element(By.XPATH, "//input[@id='register_firstname']")
firstname_input.send_keys("Andrey")
time.sleep(0.5)

lastname_input = driver.find_element(By.XPATH, "//input[@id='register_lastname']")
lastname_input.send_keys("Kochegarov")
time.sleep(0.5)

telephone_input = driver.find_element(By.XPATH, "//input[@id='register_telephone']")
telephone_input.send_keys("89930021561")
time.sleep(0.5)

country_dropdown = driver.find_element(By.XPATH, "//select[@id='register_country_id']")
country_dropdown.click()
time.sleep(0.5)

country_option = driver.find_element(By.XPATH, "//option[@value='176']")
country_option.click()
time.sleep(0.5)

zone_dropdown = driver.find_element(By.XPATH, "//select[@id='register_zone_id']")
zone_dropdown.click()
time.sleep(0.5)

zone_option = driver.find_element(By.XPATH, "//option[@value='83']")
zone_option.click()
time.sleep(0.5)

city_input = driver.find_element(By.XPATH, "//input[@id='register_city']")
city_input.send_keys("Москва")
time.sleep(0.5)

postcode_input = driver.find_element(By.XPATH, "//input[@id='register_postcode']")
postcode_input.send_keys("14422")
time.sleep(0.5)

address_input = driver.find_element(By.XPATH, "//input[@id='register_address_1']")
address_input.send_keys("ВДНХ")
time.sleep(0.5)

confirm_button = driver.find_element(By.XPATH, "//a[@id='simpleregister_button_confirm']")
confirm_button.click()
time.sleep(0.5)

# Выполнение поиска
search_input = driver.find_element(By.XPATH, "//input[@placeholder='Поиск']")
search_input.click()
time.sleep(0.5)

search_input.send_keys("htc")
time.sleep(0.5)

search_button = driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
search_button.click()
time.sleep(0.5)

input("Нажмите Enter для завершения работы")

driver.quit()