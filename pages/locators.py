from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_ADDRESS = (By.ID, 'id_registration-email')
    PASSWORD = (By.ID, 'id_registration-password1')
    CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name = "registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form')
    BOOK_NAME = (By.CSS_SELECTOR, '[class="active"]')
    PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
    BASKET_BOOK_NAME = (By.CSS_SELECTOR, '[class="alertinner " ] strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-info  fade in"]')
    VIEW_BASKET = (By.CSS_SELECTOR, '[href="/en-gb/basket/"]')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, '[class="content"] p')
