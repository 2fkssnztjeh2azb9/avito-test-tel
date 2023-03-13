from selenium.webdriver.common.by import By

from src.common import Common

class LoginPage(Common):
    _login_url = 'https://www.avito.ru/#login'
    _login_input = (By.NAME, 'login')
    _password_input = (By.NAME, 'password')
    _login_button = (By.NAME, 'submit')
    _username_button = (By.XPATH, '//a[@data-marker="header/username-button"]')
    def open_login_page(self):
        self.driver.get(self._login_url)
    def enter_login(self, login):
        self.wait(self._login_input).send_keys(login)
    def enter_password(self, password):
        self.wait(self._password_input).send_keys(password)
    def click_login_button(self):
        self.wait(self._login_button).click()
    def check_logged_in(self):
        return self.wait(self._username_button)
