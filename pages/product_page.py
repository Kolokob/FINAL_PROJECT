from .base_page import BasePage
from .locators import *


class ProductPage(BasePage):

    def should_be_able_to_add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_able_to_see_messages(self):
        text_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_AFTER_ADDED_TO_BASKET_MESSAGE)
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price_in_message = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_MESSAGE)
        assert book_name.text == text_message.text, 'Book name and book name in the message is not same'
        assert book_price.text == book_price_in_message.text, 'Book price and book price in the message is not same'

    # --- Negative tests block start ---
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappeared, but should have"

    # --- Negative tests block end ---
