
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    browser.switch_to.alert.dismiss()
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    browser.switch_to.alert.accept()
    element = WebDriverWait(browser, 1).until(
        expected_conditions.visibility_of_element_located((By.ID, "input_value"))
    )
    value = browser.find_element(By.ID, "input_value").text
    result = calc(value)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
finally:
    time.sleep(3)
    browser.quit()


