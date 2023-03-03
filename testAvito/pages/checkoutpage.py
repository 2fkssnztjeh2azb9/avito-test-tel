from selenium.webdriver.common.by import By

from .postloginpage import PostLoginPage
from .itempage import ItemPage

class CheckoutPage:
    _tel_input = '//input[@data-marker="sd/order-widget-field/phone"]'
    def __init__(self, driver):
        self.driver = driver
        page = PostLoginPage(self.driver)
        page = ItemPage(self.driver)
        page.get_delivery_button().click()
    def get_tel_input(self):
        self.driver.wait(self._tel_input)
        return self.driver.find_element(By.XPATH, self._tel_input)
