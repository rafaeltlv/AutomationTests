import pytest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class TestWebsite():
    @pytest.fixture(scope='function')
    def driver_init(self, request):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.tripadvisor.co.il/")
        time.sleep(random.randint(1, 3))

        def teardown():
            driver.quit()

        request.addfinalizer(teardown)
        return driver

    def test_search_bar_returns_poc_cafe_as_top_result(self, driver_init):
        driver = driver_init
        try:
            searchbar = driver.find_element(By.CSS_SELECTOR, "#lithium-root > main > div.QvCXh.cyIij.fluiI > div > div > div > form > input.qjfqs._G.B-.z._J.Cj.R0")
            searchbar.send_keys("poc.cafe")
            time.sleep(random.randint(1, 3))
            searchbar.send_keys(Keys.RETURN)
            assert "poc.cafe" in driver.title, f"Expected 'poc.cafe' to be in title, but got '{driver.title}' instead."
        except (TimeoutException, AssertionError) as e:
            pytest.fail(f"An error occurred during test execution: {e}")
    
    def test_click_poc_cafe_search_result_open_new_tab(self, driver_init):
        driver = driver_init
        wait = WebDriverWait(driver, 10)
        try:
            driver.get("https://www.tripadvisor.co.il/Search?q=poc.cafe")
            poccafeoption = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#BODY_BLOCK_JQUERY_REFLOW > div.page > div > div.ui_container.main_wrap > div > div > div > div > div.content_column.ui_column.is-9-desktop.is-12-tablet.is-12-mobile > div > div.ui_columns.sections_wrapper > div > div.prw_rup.prw_search_search_results.ajax-content > div > div.main_content.ui_column.is-12 > div > div:nth-child(2) > div > div > div > div > div > div > div.ui_column.is-9-desktop.is-8-mobile.is-9-tablet.content-block-column > div > div.result-title")))
            poccafeoption.click()
            tab_before_click = driver.current_window_handle
            wait.until(EC.number_of_windows_to_be(2))
            window_handles = driver.window_handles
            window_handles.remove(tab_before_click)
            tab_after_click = window_handles[0]
            driver.switch_to.window(tab_after_click)
            assert tab_before_click != tab_after_click, f"Expected a new tab to be opened after clicking element, but the tab did not change"
        except (TimeoutException, AssertionError) as e:
            pytest.fail(f"An error occurred during test execution: {e}")
    
    def test_choose_store_hours_confirm_they_appear(self, driver_init):
        driver = driver_init
        wait = WebDriverWait(driver, 10)
        try:
            driver.get("https://www.tripadvisor.co.il/Restaurant_Review-g293984-d17581289-Reviews-Poc_cafe-Tel_Aviv_Tel_Aviv_District.html#REVIEWS")
            poccafehours = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#component_53")))
            time.sleep(random.randint(1, 3))
            poccafehours.click()
            assert "שעות" in driver.page_source
        except (TimeoutException, AssertionError) as e:
            pytest.fail(f"An error occurred during test execution: {e}")