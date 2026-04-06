import pytest
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_avtorization(browser,config,wait5_ID,loader10_CLASS_NAME,logger):
    browser.get(config["urls"]["url1"])
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

