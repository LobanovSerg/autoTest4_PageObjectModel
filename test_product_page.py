from .pages.product_page import ProductPage
import pytest

link_ = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
# promo_list = [f'{link_}?promo=offer{i}' for i in range(10)]
# promo_list[7] = pytest.param(promo_list[7], marks=pytest.mark.xfail)


# @pytest.mark.parametrize('link', promo_list)
# def test_guest_can_add_product_to_basket(browser, link):
#    page = ProductPage(browser, link)
#    page.open()
#    page.product_add_to_basket()
#    page.should_product_in_basket()
#    page.should_product_price_equal_basket()


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
