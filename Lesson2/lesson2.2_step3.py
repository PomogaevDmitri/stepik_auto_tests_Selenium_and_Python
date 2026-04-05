from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    result = (int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text))
    print(result)
    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_value(str(result))  # ищем элемент с текстом "Python"

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
finally:
    time.sleep(5)
    browser.quit()


