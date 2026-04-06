import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv(".env.test")
@pytest.fixture(scope="session")
def config():
    return {
        "username": os.getenv("LOGIN"),
        "password": os.getenv("PASSWORD"),
        "base_url": os.getenv("URL_TEST")
    }
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
    yield browser
    print("\nquit browser..")
    browser.quit()