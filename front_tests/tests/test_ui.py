import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from front_tests.base_page import BasePage


@allure.story('E2E ui test')
def test_ui(browser):
    with allure.step('Visit https://useinsider.com/ and check page url'):
        page = BasePage(browser)
        browser.get('https://useinsider.com/')
        assert browser.current_url == 'https://useinsider.com/'
        page.click((By.XPATH, "//a[text()='Accept All']"))

    with allure.step('Select “More” menu in navigation bar, select “Careers” and check Career page url'):
        page.click((By.XPATH, "//li[contains(@class, 'mega-menu')]//span[text()='More']"))
        page.click((By.XPATH, "//div[contains(@class, 'col-12 col-lg-4')]//h5[text()='Careers']"))
        assert browser.current_url == 'https://useinsider.com/careers/'

    with allure.step('Check Locations, Teams and Life blocks display'):
        assert browser.find_element(By.XPATH, "//section//h3[text()[contains(.,'Our Locations')]]").is_displayed()
        assert browser.find_element(By.ID, "location-slider").is_displayed()
        assert browser.find_element(By.CLASS_NAME, "location-slider-prev").is_displayed()
        assert browser.find_element(By.CLASS_NAME, "location-slider-next").is_displayed()
        assert browser.find_element(By.CLASS_NAME, "location-slider-pagination").is_displayed()

        assert browser.find_element(By.XPATH, "//section//h2[text()='Life at Insider']").is_displayed()
        assert browser.find_element(By.XPATH, "//p[text()='We’re here to grow and drive growth—as none of us did before. Together, we’re building a culture that inspires us to create our life’s work—and creates a bold(er) impact. We know that we’re smarter as a group than we are alone. Become one of us if you dare to play bigger.']").is_displayed()
        assert browser.find_element(By.CLASS_NAME, "elementor-skin-carousel").is_displayed()

        assert browser.find_element(By.XPATH, "//section//h3[text()[contains(.,'Find your calling')]]").is_displayed()
        assert browser.find_element(By.CLASS_NAME, "career-load-more").is_displayed()
        assert browser.find_element(By.XPATH, "//a[text()='See all teams']").is_displayed()
        assert browser.find_element(By.XPATH, "//a[text()='See all teams']").is_enabled()

    with allure.step('Click “See All Teams”, select Quality Assurance, click “See all QA jobs”'):
        page.click((By.XPATH, "//a[text()='See all teams']"))
        page.click((By.XPATH, "//a[@href='https://useinsider.com/careers/quality-assurance/']"))
        page.click((By.XPATH, "//a[@href='https://useinsider.com/careers/open-positions/?department=qualityassurance']"))

    with allure.step('Filter jobs by Location - Istanbul, Turkey and department - Quality Assurance, '
                     'check presence of jobs list'):
        time.sleep(2)
        page.click((By.ID, "select2-filter-by-location-container"))
        page.click((By.XPATH, "//li[contains(@id, 'Istanbul, Turkey')]"))
        time.sleep(2)
        total_number = browser.find_element(By.CLASS_NAME, "totalResult").text
        position_cards = browser.find_elements(By.CLASS_NAME, "position-list-item")
        for position_card in position_cards:
            position_card.is_displayed()
        assert total_number == str(len(position_cards))

    with allure.step('Check that jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, '
                     'Location contains “Istanbul, Turkey” and “Apply Now” button'):
        position_titles = browser.find_elements(By.CLASS_NAME, "position-title")
        departments = browser.find_elements(By.CLASS_NAME, "position-department")
        locations = browser.find_elements(By.CLASS_NAME, "position-location")
        apply_buttons = browser.find_elements(By.XPATH, "//a[text()='Apply Now']")
        assert len(position_titles) == len(departments) == len(locations) == len(apply_buttons)
        for key in range(len(position_titles)):
            assert 'QA' in position_titles[key].text or 'Quality Assurance' in position_titles[key].text
            assert 'Quality Assurance' in departments[key].text
            assert 'Istanbul, Turkey' in locations[key].text
            assert apply_buttons[key].is_enabled()

    with allure.step('Click “Apply Now” button and check that this action redirects to Lever Application form page'):
        ActionChains(browser).move_to_element(position_titles[0]).perform()
        browser.execute_script("arguments[0].click();", apply_buttons[0])
        browser.switch_to.window(browser.window_handles[1])
        page.wait.until(EC.title_is('Insider. - Management Trainee for Quality Assurance'))
        assert 'https://jobs.lever.co/useinsider/' in browser.current_url
