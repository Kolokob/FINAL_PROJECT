import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):

    language = request.config.getoption("language")
    options = Options()

    options.add_experimental_option('prefs', {'intl.accept_languages': language})



    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)

    yield browser

    print("\nquit browser..")
    browser.quit()