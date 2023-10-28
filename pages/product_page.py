import math
import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


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


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

