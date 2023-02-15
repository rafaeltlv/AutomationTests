import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class InformationTestCase(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.tripadvisor.co.il/")

    def test_searchTripadvisor(self):
        driver = self.driver
        elem = driver.find_element(By.CSS_SELECTOR, "#lithium-root > main > div.QvCXh.cyIij.fluiI > div > div > div > form > input.qjfqs._G.B-.z._J.Cj.R0")
        elem.send_keys("poc.cafe")
        elem.send_keys(Keys.RETURN)
        assert "poc.cafe" in driver.title

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()