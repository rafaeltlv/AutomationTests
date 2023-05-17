# import os
# import pytest
# import requests
# import json
# import pandas as pd

# URL = "https://www.google.com/"

# def print_response_info(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
        
#         print("Response Information:")
#         print(f"Status Code: {response.status_code}")
#         print(f"Location Header: {response.headers.get('location', 'Not Found')}")
        
#         headers_table = []
#         for key, value in response.headers.items():
#             headers_table.append([key, value])
        
#         print("\nResponse Headers:")
#         print(tabulate(headers_table, headers=["Header", "Value"], tablefmt="grid"))
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")

# def test_tripadvisor():
#     print_response_info(URL)

# test_tripadvisor()
