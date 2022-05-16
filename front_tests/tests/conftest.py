import time

import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Available: chrome, firefox')


@pytest.fixture(scope='function')
def browser(request):
    if request.config.getoption('--browser') == 'chrome':
        with allure.step('Open Chrome browser'):
            browser = webdriver.Chrome(ChromeDriverManager().install())
    elif request.config.getoption('--browser') == 'firefox':
        with allure.step('Open Firefox browser'):
            browser = webdriver.Firefox()
    browser.set_window_position(0, 0)
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(10)
    yield browser
    with allure.step('Close browser'):
        browser.quit()
