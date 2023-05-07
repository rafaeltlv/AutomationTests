import pytest
import requests
import httpretty
from ..resources import context
from ..resources.conftest import driver_init


@httpretty.activate
def test_registration_api(driver_init):
    httpretty.register_uri(httpretty.GET, "https://www.tripadvisor.co.il/", 
                        body="Access Denied")
    response = requests.get('https://www.tripadvisor.co.il/RegistrationController')
    assert response.text == "Access Denied"
    httpretty.disable()
    httpretty.reset()

#add more apis