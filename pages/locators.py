from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators():
    ...


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGIST_FORM = (By.CSS_SELECTOR, '#register_form')
    REGIST_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGIST_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGIST_BUTTON = (By.CSS_SELECTOR, '#register_form > button')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-primary.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    MESSAGE_ELEMENTS = (By.CSS_SELECTOR, '#messages .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner')


class BasketPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, '#basket_formset')
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
