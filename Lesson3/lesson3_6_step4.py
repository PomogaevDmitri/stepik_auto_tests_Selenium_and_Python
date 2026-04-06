import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v136.fed_cm import LoginState
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
@pytest.mark.smoke
def test_avtorization(browser,config):
    link = "https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    def wait5(Id_locator):
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, Id_locator))
        )
    def loader10(Id_loader):
        WebDriverWait(browser, 10).\
            until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "loader")))

    wait5("ember501")
    browser.find_element(By.ID, "ember501").click()
    wait5("id_login_email")
    browser.find_element(By.ID, "id_login_email").send_keys(config["username"])
    browser.find_element(By.ID, "id_login_password").send_keys(config["password"])
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader").click()
    loader10("stepik-loader__message")

