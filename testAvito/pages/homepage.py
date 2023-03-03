from selenium.webdriver.common.by import By

class HomePage:
    _homepage_url = 'https://avito.ru/'
    _login_button = '//a[@data-marker="header/login-button"]'
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self._homepage_url)
    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self._login_button)
