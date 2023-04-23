import random
import time
import configparser

import pytest
from ..resources.conftest import driver_init
from ..resources import context

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.mark.usefixtures("driver_init")
# @pytest.mark.parametrize("query", ["poc.cafe", "poc cafe", "poc bakery"])
def test_search_bar_returns_poc_cafe_as_top_result(driver_init):
    print(f"Current URL: {driver_init.current_url}")
    try:
        searchbar = driver_init.find_element(By.CSS_SELECTOR,
                                        "#lithium-root > main > div.QvCXh.cyIij.fluiI > div > div > div > form > input.qjfqs._G.B-.z._J.Cj.R0")
        searchbar.send_keys("poc.cafe")
        time.sleep(random.randint(1, 3))
        searchbar.send_keys(Keys.RETURN)
        assert "poc.cafe" in driver_init.title, f"Expected 'poc.cafe' to be in title, but got '{driver_init.title}' instead."
    except (TimeoutException, AssertionError) as e:
        pytest.fail(f"An error occurred during test execution: {e}")

@pytest.mark.usefixtures("driver_init")
def test_click_poc_cafe_search_result_open_new_tab(driver_init):
    wait = WebDriverWait(driver_init, 10)
    try:
        # Search for "poc.cafe" using the search bar
        searchbar = driver_init.find_element(By.CSS_SELECTOR,
                                              "#lithium-root > main > div.QvCXh.cyIij.fluiI > div > div > div > form > input.qjfqs._G.B-.z._J.Cj.R0")
        searchbar.send_keys("poc.cafe")
        searchbar.send_keys(Keys.RETURN)
        
        # Click on the search result for "poc.cafe" to open a new tab
        poccafeoption = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#BODY_BLOCK_JQUERY_REFLOW > div.page > div > div.ui_container.main_wrap > div > div > div > div > div.content_column.ui_column.is-9-desktop.is-12-tablet.is-12-mobile > div > div.ui_columns.sections_wrapper > div > div.prw_rup.prw_search_search_results.ajax-content > div > div.main_content.ui_column.is-12 > div > div:nth-child(2) > div > div > div > div > div > div > div.ui_column.is-9-desktop.is-8-mobile.is-9-tablet.content-block-column > div > div.result-title")))
        poccafeoption.click()
        time.sleep(random.randint(1, 3))
        
        # Switch to the new tab and check if the title is correct
        driver_init.switch_to.window(driver_init.window_handles[-1])
        assert "poc.cafe" in driver_init.title, f"Expected 'poc.cafe' to be in title, but got '{driver_init.title}' instead."
        
    except (TimeoutException, AssertionError) as e:
        pytest.fail(f"An error occurred during test execution: {e}")
    finally:
        # Close the new tab and switch back to the original tab
        driver_init.close()
        driver_init.switch_to.window(driver_init.window_handles[0])

@pytest.mark.usefixtures("driver_init")
def test_choose_store_hours_confirm_they_appear(driver_init):
    wait = WebDriverWait(driver_init, 10)
    try:
        driver_init.get("https://www.tripadvisor.co.il/Restaurant_Review-g293984-d17581289-Reviews-Poc_cafe-Tel_Aviv_Tel_Aviv_District.html#REVIEWS")
        poccafehours = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#component_53")))
        time.sleep(random.randint(1, 3))
        poccafehours.click()
        assert "שעות" in driver_init.page_source
    except (TimeoutException, AssertionError) as e:
        pytest.fail(f"An error occurred during test execution: {e}")

@pytest.mark.usefixtures("driver_init")
def test_sign_in_icon(driver_init):
    wait = WebDriverWait(driver_init, 10)
    try:
        signinicon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lithium-root > header > div > nav > div > div.JNlKm > a.rmyCe._G.B-.z._S.c.Wc.wSSLS.w.jWkoZ.sOtnj")))
        signinicon.click()
        popupwindow = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.bEJky.w._Z.t._U.s.l.D.Za")))
        assert popupwindow.get_attribute('outerHTML') in driver_init.page_source
    except (TimeoutException, AssertionError) as e:
        pytest.fail(f"An error occurred during test execution: {e}")