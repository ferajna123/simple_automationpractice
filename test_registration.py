# import os
import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# url as an environment variable use the below + check if import is not commented
# url = os.environ['url']
url = 'http://automationpractice.com'
random_number = random.randrange(1, 9999999999)
random_email = 'musowicz+' + str(random_number) + '@squiz.pl'


@unittest.skip
class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # seconds

    def test_successful_registration(self):
        # test if it is possible to register an account using correct random email address
        # TODO email address validation
        self.driver.get(url+'/index.php?controller=authentication')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'create-account_form')))
        email_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'email_create')))
        email_field.send_keys(random_email)
        print( random_email)
        self.driver.find_element_by_id('SubmitCreate').click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'account-creation_form')))
        self.assertEqual(self.driver.find_element_by_xpath("//h1[contains(@class, 'page-heading')]").text, "CREATE AN ACCOUNT")

        # filling registration form, required fields only
        self.driver.find_element_by_id("customer_firstname").send_keys("Marek")
        self.driver.find_element_by_id("customer_lastname").send_keys("Usowicz")
        self.driver.find_element_by_id("passwd").send_keys("QWEqwe123!@#")
        self.driver.find_element_by_id("address1").send_keys("Street")
        self.driver.find_element_by_id("city").send_keys("Szczecin")
        self.driver.find_element_by_xpath("//select[@id='id_state']//option[13]").click()
        self.driver.find_element_by_id("postcode").send_keys("44444")
        self.driver.find_element_by_id("phone_mobile").send_keys("444444444444")
        self.driver.find_element_by_id("submitAccount").click()

        # after successful registration
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@class="logout"]')))
        self.assertEqual(self.driver.find_element_by_xpath("//h1[contains(@class, 'page-heading')]").text, "MY ACCOUNT")
        self.driver.find_element_by_xpath('//a[@class="logout"]').click()

    def tearDown(self):
        self.driver.close()
