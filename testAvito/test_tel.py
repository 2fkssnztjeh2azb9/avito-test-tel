import pytest

from src.passman import Passman
from pages.login_page import LoginPage
from pages.item_page import ItemPage
from pages.sales_page import SalesPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def logged_in(driver):
    page = LoginPage(driver)
    page.open_login_page()
    creds = Passman()
    page.enter_login(creds.password)
    page.enter_password(creds.login)
    page.click_login_button()
    assert page.check_logged_in()
    return driver

@pytest.fixture
def item_page(logged_in):
    page = SalesPage(logged_in)
    page.open_sales_page()
    page.click_first_card_header()
    page.switch_tab(1)
    return logged_in

@pytest.fixture
def checkout_page(item_page):
    page = ItemPage(item_page)
    page.click_delivery_button()
    return item_page

def test_check_tel(checkout_page):
    page = CheckoutPage(checkout_page)
    assert page.check_tel_input()
