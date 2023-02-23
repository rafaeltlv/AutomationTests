import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = [
    {
        "browsername": "chrome",
        "version": "latest",
        "platform": "MAC",
        "deviceName": "MacBook Pro"
    },

    {
        "browsername": "firefox",
        "version": "latest",
        "platform": "LINUX",
        "deviceName": "LINUX PC"
    },

    {
        "browsername": "safari",
        "version": "latest",
        "platform": "MAC",
        "deviceName": "Macbook Pro"
    },

    {
        "browsername": "MS Edge",
        "version": "latest",
        "platform": "WINDOWS 11",
        "deviceName": "Windows PC"
    }
]

@pytest.fixture(scope="function", params=capabilities)
def driver_init(request):
    capabilities = request.param
    driver = webdriver.Remote(
        command_executor='https://localhost:4444/wd/hub',
        desired_capabilities=capabilities
    )
    yield driver
    driver.quit()