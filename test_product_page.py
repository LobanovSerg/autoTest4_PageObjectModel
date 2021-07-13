from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link_ = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# promo_list = [f'{link_}?promo=offer{i}' for i in range(10)]
# promo_list[7] = pytest.param(promo_list[7], marks=pytest.mark.xfail)


# @pytest.mark.parametrize('link', promo_list)
# def test_guest_can_add_product_to_basket(browser, link):
#    page = ProductPage(browser, link)
#    page.open()
#    page.should_be_product_add_to_basket()


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


link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/'\
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
