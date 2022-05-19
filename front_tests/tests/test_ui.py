import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from front_tests.base_page import BasePage
from front_tests.tests.conftest import TEAM_TEXT


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
        assert browser.find_element(By.XPATH, f"//p[text()='{TEAM_TEXT}']").is_displayed()
        assert browser.find_element(By.CLASS_NAME, "elementor-skin-carousel").is_displayed()

        assert browser.find_element(By.XPATH, "//section//h3[text()[contains(.,'Find your calling')]]").is_displayed()
        assert browser.find_element(By.CLASS_NAME, "career-load-more").is_displayed()
        assert browser.find_element(By.XPATH, "//a[text()='See all teams']").is_displayed()
        assert browser.find_element(By.XPATH, "//a[text()='See all teams']").is_enabled()

    with allure.step('Click “See All Teams”, select Quality Assurance, click “See all QA jobs”'):
        page.click((By.CLASS_NAME, "loadmore"))
        page.click((By.XPATH, "//a[@href='https://useinsider.com/careers/quality-assurance/']"))
        page.click((By.XPATH, "//a[@href='https://useinsider.com/careers/open-positions/?department=qualityassurance']"))

    with allure.step('Filter jobs by Location - Istanbul, Turkey and check presence of jobs list'):
        page.select_location('Istanbul, Turkey')
        page.check_presence_of_jobs('Istanbul, Turkey')

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
