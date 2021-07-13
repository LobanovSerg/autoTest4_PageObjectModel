from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

link_ = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email, passwd = str(time.time()) + '@fakemail.org', 'testpasswd'
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(email, passwd)
        page = MainPage(browser, browser.current_url)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_)
        page.open()
        page.should_be_product_add_to_basket()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_add_to_basket()


@pytest.mark.xfail(reason='Success message in page')
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    page = ProductPage(browser, link_)
    page.open()
    page.product_add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason='Success message not dissapear')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_)
    page.open()
    page.product_add_to_basket()
    page.should_be_disappear_success_message()


link = 'http://selenium1py.pythonanywhere.com/catalogue/'\
       'the-city-and-the-stars_95/'


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
