import allure
import pytest
from selenium import webdriver

TEAM_TEXT = 'We’re here to grow and drive growth—as none of us did before. Together, we’re building a culture that ' \
            'inspires us to create our life’s work—and creates a bold(er) impact. We know that we’re smarter as a ' \
            'group than we are alone. Become one of us if you dare to play bigger.'


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox', help='Available: chrome, firefox')


@pytest.fixture(scope='function')
def browser(request):
    if request.config.getoption('--browser') == 'chrome':
        with allure.step('Open Chrome browser'):
            browser = webdriver.Chrome()
    elif request.config.getoption('--browser') == 'firefox':
        with allure.step('Open Firefox browser'):
            browser = webdriver.Firefox()
    browser.set_window_position(0, 0)
    browser.set_window_size(1920, 1080)
    yield browser
    with allure.step('Close browser'):
        browser.quit()
