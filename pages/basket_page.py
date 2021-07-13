from .base_page import BasePage
from .locators import BasketPageLocators
from .languages import languages


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_not_be_product_in_basket()
        self.should_be_empty_basket_text()

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM),\
            'Basket is not empty, but should be'

    def should_be_empty_basket_text(self):
        lang = self.browser.current_url.split('/')[3]
        text = self.browser.find_element(
            *BasketPageLocators.EMPTY_MESSAGE).text
        assert languages[lang] in text, 'Empty basket message should be'

    def should_be_disappear_empty_basket_message(self):
        assert self.is_disappeared(*BasketPageLocators.EMPTY_MESSAGE),\
            'Empty basket message is not disappear, but should be'
