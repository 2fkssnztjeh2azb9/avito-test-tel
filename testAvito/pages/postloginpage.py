from selenium.webdriver.common.by import By

from .loginpage import LoginPage
from src.passman import Passman

class PostLoginPage:
    _username_button = '//a[@data-marker="header/username-button"]'
    def __init__(self, driver):
        self.driver = driver
        page = LoginPage(self.driver)
        passman = Passman()
        page.login(passman.login, passman.password)
        self.driver.wait(self._username_button)
