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
    wait = WebDriverWait(driver_init, 20)
    try:
        restaurants_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lithium-root > main > div.cBOoN > span > div > div > div > div:nth-child(3) > a > span.QLiHN.o.W > span"))) 
        
        restaurants_option.click()
        restaurants_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div.kaEuY > div > form > input.qjfqs._G.B-.z._J.Cj.R0")))
        restaurants_input.send_keys("poc.cafe")
        random_interval = random.uniform(2, 3)
        time.sleep(random_interval)
        #correct if needed?
        poccafe = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "poc.cafe")))
        poccafe.click()

        poccafehours = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bsALk")))
        poccafehours.click()

        poccafehours_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#BODY_BLOCK_JQUERY_REFLOW > div.KWdaU.Za.f.e > div > div > div:nth-child(2) > div")))
        assert poccafehours_div is not None
    except (TimeoutException, AssertionError) as e:
        pytest.fail(f"An error occurred during test execution: {e}")
        
@pytest.mark.usefixtures("driver_init")
def test_account_sign_in_screen(driver_init):
    wait = WebDriverWait(driver_init, 20)
    try:
        random_interval = random.uniform(1, 3)
        time.sleep(random_interval)
        signinicon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lithium-root > header > div > nav > div > div.JNlKm > a.rmyCe._G.B-.z._S.c.Wc.wSSLS.w.jWkoZ.sOtnj")))
        signinicon.click()

        iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.VZmgo.D.X0.X1.Za.Ra > div > div.TocEc._Z.S2.H2._f.WHsPz > div > div > iframe")))
        
        driver_init.switch_to.frame(iframe)

        sign_in_email_option =  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#ssoButtons > button > span.textContainer")))
        sign_in_email_option.click()

        sign_in_email_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#regSignIn\\.email")))
        sign_in_email_input.send_keys("reyesraf@oregonstate.edu")

        sign_in_email_password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#regSignIn\\.password")))
        sign_in_email_password.send_keys("ztgBS7jAiZ7yBMe")

        #to.do
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ui_button")))        
        sign_in_button.click()

        driver_init.switch_to.default_content()
        
        main_page_account_icon = driver_init.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lithium-root > header > div > nav > div > div.JNlKm > div.JLKop.w > a > div > div > div > picture > img")))
        main_page_account_icon.click()

        driver_init.get_screenshot_as_file(help.png)

        assert main_page_account_icon is not None
    except (TimeoutException, AssertionError) as e:
        pytest.fail(f"An error occurred during test execution: {e}")