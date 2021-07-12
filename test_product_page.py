from .pages.product_page import ProductPage
import pytest

link_ = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
promo_list = [f'{link_}?promo=offer{i}' for i in range(10)]
promo_list[7] = pytest.param(promo_list[7], marks=pytest.mark.xfail)


@pytest.mark.parametrize('link', promo_list)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.should_product_in_basket()
    page.should_product_price_equal_basket()
