from selenium.webdriver.common.by import By

from .homepage import HomePage

class LoginPage:
    _login_url = 'https://www.avito.ru/#login'
    _login_input = '//input[@name="login"]'
    _password_input = '//input[@name="password"]'
    _login_button = '//button[@name="submit"]'
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self._login_url)
    def login(self, login, password):
        self.driver.wait(self._login_input)
        self.get_login_input().send_keys(login)
        self.get_password_input().send_keys(password)
        self.get_login_button().click()
    def get_login_input(self):
        return self.driver.find_element(By.XPATH, self._login_input)
    def get_password_input(self):
        return self.driver.find_element(By.XPATH, self._password_input)
    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self._login_button)
