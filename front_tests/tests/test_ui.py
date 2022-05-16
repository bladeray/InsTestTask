import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# def click(browser, by: By, locator: str):
#     try:
#         element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((by, locator)))
#         element.click()
#     except:
#         browser.execute_script("arguments[0].click();", element)


@allure.story('E2E ui test')
def test_ui(browser):
    with allure.step('Visit https://useinsider.com/ and check page url'):
        wait = WebDriverWait(browser, 10)
        browser.get('https://useinsider.com/')
        assert browser.current_url == 'https://useinsider.com/'
        browser.find_element(By.XPATH, "//a[text()='Accept All']").click()

    with allure.step('Select “More” menu in navigation bar, select “Careers” and check Career page url'):
        browser.find_element(By.XPATH, "//li[contains(@class, 'mega-menu')]//span[text()='More']").click()
        browser.find_element(By.XPATH, "//div[contains(@class, 'col-12 col-lg-4')]//h5[text()='Careers']").click()
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
        teams_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='See all teams']")))
        assert teams_button.is_displayed()
        assert teams_button.is_enabled()

    with allure.step('Click “See All Teams”, select Quality Assurance, click “See all QA jobs”'):
        browser.execute_script("arguments[0].click();", teams_button)
        qa_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='https://useinsider.com/careers/quality-assurance/']")))
        browser.execute_script("arguments[0].click();", qa_button)
        browser.find_element(By.XPATH, "//a[@href='https://useinsider.com/careers/open-positions/?department=qualityassurance']").click()

    with allure.step('Filter jobs by Location - Istanbul, Turkey and department - Quality Assurance, '
                     'check presence of jobs list'):
        time.sleep(2)
        location_filter = wait.until(EC.visibility_of_element_located((By.ID, "select2-filter-by-location-container")))
        location_filter.click()
        istanbul_point = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(@id, 'Istanbul, Turkey')]")))
        istanbul_point.click()
        for second in range(5):
            try:
                total_number = browser.find_element(By.CLASS_NAME, "totalResult").text
                position_cards = browser.find_elements(By.CLASS_NAME, "position-list-item")
                for position_card in position_cards:
                    position_card.is_displayed()
                assert total_number == str(len(position_cards))
                break
            except AssertionError:
                time.sleep(1)

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
        wait.until(EC.title_is('Insider. - Management Trainee for Quality Assurance'))
        assert 'https://jobs.lever.co/useinsider/' in browser.current_url