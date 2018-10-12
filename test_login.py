# import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# url as an environment variable use the below + check if import is not commented
# url = os.environ['url']
url = 'http://automationpractice.com'


@unittest.skip
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # seconds

    def test_successful_login(self):
        # test successful login
        # TODO unsuccessful login
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="header_user_info"]')))
        signin_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="login"]')))
        signin_button.click()
        # keeping credentials in code is not recommended, use environment variable instead
        self.driver.find_element_by_id('email').send_keys('musowicz+6558935847@squiz.pl')
        self.driver.find_element_by_id('passwd').send_keys('QWEqwe123!@#')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'SubmitLogin')))
        self.driver.find_element_by_id('SubmitLogin').click()

        # after successful registration
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@class="logout"]')))
        self.assertEqual(self.driver.find_element_by_xpath("//h1[contains(@class, 'page-heading')]").text, "MY ACCOUNT")
        self.driver.find_element_by_xpath('//a[@class="logout"]').click()

    def tearDown(self):
        self.driver.close()