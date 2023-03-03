import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DriverWithWait(webdriver.Chrome):
    def wait(self, xpath, delay=20):
            return WebDriverWait(self, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))

class GetWebDriver(unittest.TestCase):
    def setUp(self):
        self.driver = DriverWithWait()
    def tearDown(self):
        self.driver.quit()
