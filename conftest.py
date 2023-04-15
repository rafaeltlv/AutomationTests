import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
import httpretty
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.wait import WebDriverWait
from context import *

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name (chrome, firefox or edge)")

@pytest.fixture(scope="session")
def driver(request):
    # Set up the WebDriver based on the OS and browser
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Launching Chrome driver")
        options = ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        print("Launching Firefox driver")
        options = FirefoxOptions()
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        print("Launching Edge driver")
        options.use_chromium = True
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError("Unsupported browser")

    # Set the browser window size
    driver.set_window_size(1280, 1024)
    yield driver
    driver.quit()