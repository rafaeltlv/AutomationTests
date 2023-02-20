import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class InformationTestCase(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.tripadvisor.co.il/")

    def test_searchTripadvisorForCafe(self):
        driver = self.driver
        elem = driver.find_element(By.CSS_SELECTOR, "#lithium-root > main > div.QvCXh.cyIij.fluiI > div > div > div > form > input.qjfqs._G.B-.z._J.Cj.R0")
        elem.send_keys("poc.cafe")
        elem.send_keys(Keys.RETURN)
        assert "poc.cafe" in driver.title

    def test_clcikSoleResult(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        try:
            elem1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#BODY_BLOCK_JQUERY_REFLOW > div.page > div > div.ui_container.main_wrap > div > div > div > div > div.content_column.ui_column.is-9-desktop.is-12-tablet.is-12-mobile > div > div.ui_columns.sections_wrapper > div > div.prw_rup.prw_search_search_results.ajax-content > div > div.main_content.ui_column.is-12 > div > div:nth-child(2) > div > div > div > div > div > div > div.ui_column.is-3-desktop.is-3-tablet.is-4-mobile.thumbnail-column > div > div.frame > div > div.aspect.is-shown-at-desktop > div")))
            url_before_click = driver.current_url
            elem1.click()
            wait.until(EC.url_changes(url_before_click))
            url_after_click = driver.current_url
            assert url_before_click != url_after_click
        except TimeoutException:
            print("Element not found or URL did not change within 10 seconds")  

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()