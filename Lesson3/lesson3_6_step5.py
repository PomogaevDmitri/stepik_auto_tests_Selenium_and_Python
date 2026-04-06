import math
import time
from math import trunc

import pytest
from selenium.webdriver.common.by import By

@pytest.fixture
def answer():
   return math.log(int(time.time()))

@pytest.mark.smoke
@pytest.mark.parametrize("urltest", ["url1", "url2", "url3", "url4", "url5", "url6", "url7", "url8"])
def test_avtorization(browser,config,wait5_ID,loader10_CLASS_NAME,logger,urltest,answer,wait5_class,wait5tag):
    browser.get(config["urls"][urltest])
    wait5_ID("ember501")
    logger.info("Страница загружена")
    browser.find_element(By.ID, "ember501").click()
    logger.info("Клик по кнопке Войти")
    wait5_ID("id_login_email")
    logger.info("Попап загружен")
    browser.find_element(By.ID, "id_login_email").send_keys(config["username"])
    browser.find_element(By.ID, "id_login_password").send_keys(config["password"])
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader").click()
    loader10_CLASS_NAME("stepik-loader__message")
    try:
        wait5_class("again-btn")
        browser.find_element(By.CLASS_NAME, "again-btn").click()
        browser.find_element(By.XPATH, "//button[text()='OK']").click()
    except:
        pass
    answer_field = wait5tag("textarea")
    answer_field.clear()
    time.sleep(2)
    answer_field.send_keys(answer)
    wait5_class("submit-submission")
    browser.find_element(By.CLASS_NAME,"submit-submission").click()
    smarthints = wait5_class("smart-hints__hint")

    assert "Correct!" == smarthints.text