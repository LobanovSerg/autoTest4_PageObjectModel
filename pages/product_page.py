from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def product_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), \
            'Button "Add to basket" not found'
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()
        self.solve_quiz_and_get_code()

    def should_product_in_basket(self):
        prod_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        name_in_message = self.browser.find_elements(
            *ProductPageLocators.MESSAGE_ELEMENTS)[0].text
        assert name_in_message == prod_name, 'Wrong product name in basket'

    def should_product_price_equal_basket(self):
        prod_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        price_in_message = self.browser.find_elements(
            *ProductPageLocators.MESSAGE_ELEMENTS)[2].text
        assert price_in_message == prod_price, 'Wrong price in basket'
