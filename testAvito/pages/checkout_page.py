from selenium.webdriver.common.by import By

from src.common import Common

class CheckoutPage(Common):
    _tel_input = '//input[@data-marker="sd/order-widget-field/phone"]'
    def open_checkout_page(self):
        self.driver.get(self._sales_url)
    def check_tel_input(self):
        _tel_expected = ''
        assert self.wait(self._tel_input).get_attribute('value') == _tel_expected
