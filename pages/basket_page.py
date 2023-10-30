from selenium.common import NoSuchElementException

from .locators import *
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert empty_basket_message.text == "Your basket is empty. Continue shopping", ("Basket is not empty or some "
                                                                                        "bug with UI")

    def should_not_see_incorrect_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)

        incorrect_message = "FullStack guy is a GOD"
        assert empty_basket_message.text != incorrect_message, \
            "Basket empty message displayed the incorrect text"


    def should_not_see_items_in_basket(self):

        try:
            empty_basket_incorrect_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_INCORRECT_MESSAGE)

            incorrect_message = 'Items to buy now'

            assert empty_basket_incorrect_message != incorrect_message

        except NoSuchElementException:
            "Basket is not empty or incorrect text"


