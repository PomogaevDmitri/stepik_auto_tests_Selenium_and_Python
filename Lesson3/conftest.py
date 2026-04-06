import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
load_dotenv(".env.test")
@pytest.fixture(scope="session")
def config():
    return {
        "username": os.getenv("LOGIN"),
        "password": os.getenv("PASSWORD"),
        "urls":{
            "url1": os.getenv("URL_TEST1"),
            "url2": os.getenv("URL_TEST2"),
            "url3": os.getenv("URL_TEST3"),
            "url4": os.getenv("URL_TEST4"),
            "url5": os.getenv("URL_TEST5"),
            "url6": os.getenv("URL_TEST6"),
            "url7": os.getenv("URL_TEST7"),
            "url8": os.getenv("URL_TEST8")
        }
    }

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture
def wait5_ID(browser):
    def _wait5_ID(Id_locator):
        return WebDriverWait(browser, 5).\
                    until(EC.visibility_of_element_located((By.ID, Id_locator))
                        )
    return _wait5_ID
@pytest.fixture
def wait5_class(browser):
    def _wait5_class(Class_name):
        return WebDriverWait(browser, 5).\
                    until(EC.element_to_be_clickable((By.CLASS_NAME, Class_name))
                        )
    return _wait5_class
@pytest.fixture
def wait5tag(browser):
    def _wait5tag(tag_name):
        return WebDriverWait(browser, 5).\
                    until(EC.element_to_be_clickable((By.TAG_NAME, tag_name))
                          )
    return _wait5tag
@pytest.fixture
def visibility_class(browser):
    def _visibility_class(class_name):
        return WebDriverWait(browser, 5).\
                    until(EC.visibility_of_element_located((By.CLASS_NAME, class_name))
                          )
    return _visibility_class


@pytest.fixture
def loader10_CLASS_NAME(browser):
    def _loader10_CLASS_NAME(Id_loader):
        try:
            WebDriverWait(browser, 5).\
                until(EC.invisibility_of_element_located((By.CLASS_NAME, Id_loader)))
        except:
            pass
    return _loader10_CLASS_NAME
def pytest_configure():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

@pytest.fixture
def logger():
    """Фикстура, предоставляющая логгер для теста"""
    return logging.getLogger(__name__)