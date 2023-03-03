from src.webdriversetup import GetWebDriver
from pages.checkoutpage import CheckoutPage

class TestCheckoutPhoneNumber(GetWebDriver):
    def test_tel(self):
        _tel_expected = ''
        page = CheckoutPage(self.driver)
        tel = page.get_tel_input().get_attribute('value')
        self.assertEqual(tel, _tel_expected)
