import time

import pytest
from selenium.common import NoAlertPresentException
from .pages.product_page import ProductPage
from .pages.main_page import *
import math


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
def test_guest_can_add_product_to_basket_working_links(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_able_to_add_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_able_to_see_messages()


@pytest.mark.xfail(reason="This link is expected to fail due to a known bug.")
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_can_add_product_to_basket_bugged_link(browser, link):
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
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_able_to_add_to_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.should_be_able_to_see_messages()
    time.sleep(2)
