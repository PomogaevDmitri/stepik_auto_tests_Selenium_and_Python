from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fake = Faker()
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    value = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    result = calc(value)
    browser.find_element(By.ID,"answer").send_keys(result)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
finally:
    time.sleep(3)
    browser.quit()


