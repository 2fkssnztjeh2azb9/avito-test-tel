from selenium.webdriver.common.by import By

from src.common import Common
from pages.sales_page import SalesPage

class ItemPage(Common):
    _delivery_button = (By.XPATH, '//button[@data-marker="delivery-item-button-main"]')
    def click_delivery_button(self):
        self.wait(self._delivery_button).click()
