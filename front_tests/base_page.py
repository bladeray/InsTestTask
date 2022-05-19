import time

from retry_decorator import retry
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 2)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except:
            self.browser.execute_script("arguments[0].click();", element)

    @retry(WebDriverException, tries=5, timeout_secs=0.5)
    def select_location(self, location_name: str):
        self.click((By.ID, "select2-filter-by-location-container"))
        self.click((By.XPATH, f"//li[contains(@id, '{location_name}')]"))

    @retry(AssertionError, tries=5, timeout_secs=0.5)
    def check_presence_of_jobs(self, location_name):
        locations = self.browser.find_elements(By.CLASS_NAME, "position-location")
        for location in locations:
            assert location_name in location.text
        total_number = self.browser.find_element(By.CLASS_NAME, "totalResult").text
        position_cards = self.browser.find_elements(By.CLASS_NAME, "position-list-item")
        assert total_number == str(len(position_cards))


