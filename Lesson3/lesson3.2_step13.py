from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import unittest
class TestReg(unittest.TestCase):
    def test_registration1(self):
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
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",\
        "Text on the page does not match the expected text")

if __name__ == "__main__":
    unittest.main()