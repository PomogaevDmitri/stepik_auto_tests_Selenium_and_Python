from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    value = browser.find_element(By.ID, "input_value").text
    result = calc(value)
    Pole = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", Pole)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
    time.sleep(3)
    browser.quit()


