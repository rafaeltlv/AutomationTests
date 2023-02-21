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

    def navigate_to_search_results_page(self, query):
        driver = self.driver
        driver.get(f"https://www.tripadvisor.co.il/Search?q={query}")

    def navigate_to_poc_reveiews_page(self, query):
        driver = self.driver
        driver.get("https://www.tripadvisor.co.il/Restaurant_Review-g293984-d17581289-Reviews-Poc_cafe-Tel_Aviv_Tel_Aviv_District.html#REVIEWS")

    def test_searchTripadvisorForCafe(self):
        driver = self.driver
        elem = driver.find_element(By.CSS_SELECTOR, "#lithium-root > main > div.QvCXh.cyIij.fluiI > div > div > div > form > input.qjfqs._G.B-.z._J.Cj.R0")
        elem.send_keys("poc.cafe")
        elem.send_keys(Keys.RETURN)
        get_title = driver.title
        self.assertIn("poc.cafe", driver.title, f"Expected 'poc.cafe' to be in title, but got '{get_title}' instead.")
    
    def test_clickSoleResult(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        self.navigate_to_search_results_page("poc.cafe")
        elem1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#BODY_BLOCK_JQUERY_REFLOW > div.page > div > div.ui_container.main_wrap > div > div > div > div > div.content_column.ui_column.is-9-desktop.is-12-tablet.is-12-mobile > div > div.ui_columns.sections_wrapper > div > div.prw_rup.prw_search_search_results.ajax-content > div > div.main_content.ui_column.is-12 > div > div:nth-child(2) > div > div > div > div > div > div > div.ui_column.is-9-desktop.is-8-mobile.is-9-tablet.content-block-column > div > div.result-title")))
        tab_before_click = driver.current_window_handle
        elem1.click()
        wait.until(EC.number_of_windows_to_be(2))
        window_handles = driver.window_handles
        window_handles.remove(tab_before_click)
        tab_after_click = window_handles[0]
        driver.switch_to.window(tab_after_click)
        self.assertNotEqual(tab_before_click, tab_after_click, "Expected a new tab to be opened after clicking element, but the tab did not change")

    def test_chooseTimeConfirmHoursAppear(self):
        driver = self.driver
        self.navigate_to_poc_reveiews_page(self)
        wait = WebDriverWait(driver, 10)
        elem2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#component_53 > div > div:nth-child(3) > span.DsyBj.YTODE > div")))
        elem2.click()
        elem3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#BODY_BLOCK_JQUERY_REFLOW > div.KWdaU.Za.f.e > div > div > div:nth-child(2) > div")))
        self.assertIn("שעות", driver.page_source, f"שעות were not presented")

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()