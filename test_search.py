# import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# url as an environment variable use the below + check if import is not commented
# url = os.environ['url']
url = 'http://automationpractice.com'


# @unittest.skip
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # seconds

    def test_empty_query_search(self):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'search_query_top')))
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, 'submit_search')))
        search_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//p[@class="alert alert-warning"]')))
        self.assertEqual(self.driver.find_element_by_xpath('//p[@class="alert alert-warning"]').text, "Please enter a search keyword")

    def test_query_search(self):
        self.driver.get(url)
        search_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'search_query_top')))
        search_field.send_keys('Printed Chiffon Dress')
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, 'submit_search')))
        search_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="heading-counter"]')))
        # self.assertEqual(self.driver.find_element_by_xpath('//span[@class="heading-counter"]').text, "2 results have been found.")
        self.assertNotEquals(self.driver.find_element_by_xpath('//span[@class="heading-counter"]').text, "Please enter a search keyword")

    def tearDown(self):
        self.driver.close()
