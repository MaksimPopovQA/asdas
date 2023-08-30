from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        login_link.click()

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        return book_name

    def basket_book_name(self):
        basket_book_name = self.browser.find_element(*ProductPageLocators.BASKET_BOOK_NAME).text
        return basket_book_name

    def should_be_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return price

    def basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        return basket_price

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_BOOK_NAME), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_is_not_element_present(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_BOOK_NAME), \
            "Success message is presented, but should not be"
