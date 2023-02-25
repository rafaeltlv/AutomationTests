import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

executor_url = "https://localhost:4444/wd/hub"


capabilities = [
    {
        "browserName": "chrome",
        "version": "latest",
        "platformName": "MAC",
        "deviceName": "MacBook Pro"
    },

    {
        "browserName": "firefox",
        "version": "latest",
        "platformName": "LINUX",
        "deviceName": "LINUX PC"
    },

    {
        "browserName": "safari",
        "version": "latest",
        "platformName": "MAC",
        "deviceName": "Macbook Pro"
    },

    {
        "browserName": "MicrosoftEdge",
        "version": "latest",
        "platformName": "WINDOWS",
        "deviceName": "Windows PC"
    }
]

@pytest.fixture(scope="function", params=capabilities)
def driver_init(request):
    capabilities = request.param
    driver = webdriver.Remote(
        executor_url=executor_url,
        desired_capabilities=capabilities
    )
    yield driver
    driver.quit()