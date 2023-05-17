# import pytest
import requests
# import httpretty
# from contextlib import asynccontextmanager

# from ..resources.conftest import driver_init

import requests

def test_tripadvisor():
    url = "https://www.google.com/"
    response = requests.get(url)
    print(response.status_code, response.history, response.headers)
    # assert response.status_code == 200
    # assert response.history[0].status_code == 200
    # assert response.history[0].headers['location'] == "https://www.tripadvisor.co.il/"

test_tripadvisor()
