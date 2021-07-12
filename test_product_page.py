from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/\
catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.product_add_to_basket()
    page.should_product_in_basket()
    page.should_product_price_equal_basket()
