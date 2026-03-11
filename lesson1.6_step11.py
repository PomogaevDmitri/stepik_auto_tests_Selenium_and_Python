from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

try:
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fake = Faker()
    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(fake.word())
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys(fake.word())
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(fake.word())

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    element = WebDriverWait(browser, 2).until(
        expected_conditions.visibility_of_element_located((By.TAG_NAME, "h1"))
    )

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()