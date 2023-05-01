import httpretty
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

@pytest.fixture(scope='function')
def driver_init(request):
    options = Options()
    options.add_argument('--disable-cookies')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    options = Options()
    options.add_argument('--disable-cookies')
    driver.maximize_window()
    driver.get("https://www.tripadvisor.co.il/")
    assert driver is not None 
    time.sleep(random.randint(1, 3))

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
    return driver