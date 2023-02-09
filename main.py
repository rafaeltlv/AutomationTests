import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InformationTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://google.com")

    def test_GoogleSearchResults(self):
        driver = self.driver
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("poc.cafe")
        elem.send_keys(Keys.RETURN)
        assert "poc.cafe" in driver.title 

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()