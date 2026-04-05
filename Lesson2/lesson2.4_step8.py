from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    element = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    browser.find_element(By.ID, "book").click()
    value = browser.find_element(By.ID, "input_value").text
    result = calc(value)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(3)
    browser.quit()


