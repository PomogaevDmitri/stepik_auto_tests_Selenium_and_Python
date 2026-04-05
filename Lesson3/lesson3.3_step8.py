from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"
# тестовый вызов функции
test_substring("fulltext","some_value")