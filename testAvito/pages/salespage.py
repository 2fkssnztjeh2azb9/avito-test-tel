from selenium.webdriver.common.by import By

class SalesPage:
    # по указанному адресу должны быть объявления с доставкой, а на деле - когда как
    _sales_url = 'https://www.avito.ru/sochi/lichnye_veschi?cd=1&d=1'
    _card_header = '//h3[@itemprop="name"]'
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self._sales_url)
    def get_card_header(self):
        return self.driver.find_element(By.XPATH, self._card_header)
