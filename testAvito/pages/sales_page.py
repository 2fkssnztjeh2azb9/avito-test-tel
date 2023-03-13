from selenium.webdriver.common.by import By

from src.common import Common

class SalesPage(Common):
    # по указанному адресу должны быть объявления с доставкой, а на деле - когда как
    _sales_url = 'https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1'
    _card_header = (By.XPATH, '//h3[@itemprop="name"]')
    def open_sales_page(self):
        self.driver.get(self._sales_url)
    def click_first_card_header(self):
        self.wait(self._card_header).click()
