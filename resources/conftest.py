import random
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.edge.options import Options as EdgeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())

@pytest.fixture(scope='function')
def driver_init(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-cookies')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--enable-logging')
    options.add_argument('--v=1')
    # Set browser name in options if needed
    options.set_capability('browserName', 'chrome')
    # Connect to Selenium Grid
    driver = webdriver.Remote(
        command_executor='http://selenium-router:4444/wd/hub',
        options=options
    )
    driver.maximize_window()
    driver.get("https://control.autofleet.io/login")
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def test_login(driver_init):
    WebDriverWait(driver_init, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginName"))).send_keys("rafael@autofleet.io")
    WebDriverWait(driver_init, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginPassword"))).send_keys("FufuM0ng0ls$")
    WebDriverWait(driver_init, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginSubmit"))).click()

    # Example assertion: check if URL changed or a specific element is present
    # Replace 'expected_element' and 'expected_url' with actual values
    WebDriverWait(driver_init, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div:nth-child(1) > aside > div > ul > li:nth-child(1) > a > div > span > svg")))
    
    expected_url = "https://control.autofleet.io/2DScU8snnrrDtvK8GytYSi/"

    actual_url = driver_init.current_url
    
    yield driver_init
