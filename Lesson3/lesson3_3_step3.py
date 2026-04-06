from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest


class TestReg:
    def setup_method(self):
        # Инициализация веб-драйвера перед каждым тестом
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(1)

    def teardown_method(self):
        self.browser.quit()

    def test_registration1(self):
        self.link = "https://suninjuly.github.io/registration1.html"
        fake = Faker()
        self.browser.get(self.link)

        # Заполняем обязательные поля
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(fake.first_name())
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys(fake.last_name())
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(fake.email())

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки страницы
        WebDriverWait(self.browser, 2).until(
            expected_conditions.visibility_of_element_located((By.TAG_NAME, "h1"))
        )

        # Проверяем текст
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        assert welcome_text == "Congratulations! You have successfully registered!", \
            f"Text mismatch: expected 'Congratulations! You have successfully registered!', got '{welcome_text}'"

    def test_registration2(self):
        self.link = "https://suninjuly.github.io/registration2.html"
        self.browser.get(self.link)
        fake = Faker()

        # Заполняем обязательные поля
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys(fake.first_name())
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys(fake.last_name())
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys(fake.email())

        # Отправляем заполненную форму
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки страницы
        WebDriverWait(self.browser, 2).until(
            expected_conditions.visibility_of_element_located((By.TAG_NAME, "h1"))
        )

        # Проверяем текст
        welcome_text = self.browser.find_element(By.TAG_NAME, "h1").text
        assert welcome_text == "Congratulations! You have successfully registered!", \
            f"Text mismatch: expected 'Congratulations! You have successfully registered!', got '{welcome_text}'"


if __name__ == "__main__":
    pytest.main(["-v", __file__])