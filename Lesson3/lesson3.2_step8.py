from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert actual_result == expected_result, \
        f"expected {expected_result}, got {actual_result}"

# тестовый вызов функции
test_input_text(8, 11)

