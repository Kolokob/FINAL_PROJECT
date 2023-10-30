import time

import pytest
from .pages.main_page import *
from .pages.login_page import *
from .pages.base_page import *
from .pages.basket_page import BasketPage

@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket_working_links(self, browser, link):
    page = ProductPage(browser, link)

    page.open()
    page.should_be_able_to_add_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_able_to_see_messages()


@pytest.mark.xfail(reason="This link is expected to fail due to a known bug.")
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_can_add_product_to_basket_bugged_link(self, browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_able_to_add_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_able_to_see_messages()


# backup test
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(self, browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_able_to_add_to_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.should_be_able_to_see_messages()
    time.sleep(2)

def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

    page = ProductPage(browser, link)
    page.open()
    page.should_be_able_to_add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(self, browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(self, browser):

    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

    page = ProductPage(browser, link)
    page.open()
    page.should_be_able_to_add_to_basket()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(self, browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(self, browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'

    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/'

    page = ProductPage(browser, link)
    page.open()

    page.should_be_able_to_go_to_basket()

    basket_page_link = browser.current_url
    basket_page = BasketPage(browser, basket_page_link)
    basket_page.should_not_see_items_in_basket()
    basket_page.should_be_empty_basket()



