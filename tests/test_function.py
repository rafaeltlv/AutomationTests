import random
import time
import configparser

import pytest
from ..resources.conftest import driver_init
from ..resources.conftest import test_login
from ..resources import context

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

def test_customer_environment_dropdown(test_login):
    try:
        WebDriverWait(test_login, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.afCS__single-value"))).click()
        customer_environment_name = WebDriverWait(test_login, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='autofleet RaaS']")))
        customer_environment_name.click()  # Explicitly click the element
        # Fetch the text again to verify if it's selected or displayed
        selected_environment = WebDriverWait(test_login, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.afCS__single-value"))).text
        assert "autofleet RaaS" in selected_environment, "Expected 'autofleet RaaS' to be selected"
    except Exception as e:
        pytest.fail(f"Customer environment could not be found in dropdown menu during test execution: {str(e)}")


def test_search_user(test_login):
    try:
        WebDriverWait(test_login, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test-id='management']"))).click()
        WebDriverWait(test_login, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#drivers"))).click()
        WebDriverWait(test_login, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='searchInput']"))).send_keys("genz")
        first_name_field = WebDriverWait(test_login, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Rafa']")))
        assert "Rafa" == first_name_field.text, "Expected 'Rafa' to be in the first name field" 
    except Exception as e:
        pytest.fail(f"User's name could not be found in search input during test execution: {str(e)}")