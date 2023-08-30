from pages.base_page import BasePage
from pages.locators import ProductPageLocators, BasketPageLocators


class BasketPage(BasePage):

    def basket_book_name(self):
        basket_book_name = self.browser.find_element(*ProductPageLocators.BASKET_BOOK_NAME).text
        return basket_book_name

    def basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        return basket_price

    def should_be_empty_basket_text(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET).text
        assert 'Your basket is empty' in empty_basket_text
        print(empty_basket_text)
