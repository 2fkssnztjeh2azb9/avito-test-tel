from selenium.webdriver.common.by import By

from .salespage import SalesPage

class ItemPage:
    _delivery_button = '//button[@data-marker="delivery-item-button-main"]'
    def __init__(self, driver):
        self.driver = driver
        page = SalesPage(self.driver)
        page.get_card_header().click()
        self.driver.switch_to.window(self.driver.window_handles[1])
    def get_delivery_button(self):
        self.driver.wait(self._delivery_button)
        return self.driver.find_element(By.XPATH, self._delivery_button)
