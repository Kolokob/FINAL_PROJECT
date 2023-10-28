import time

import pytest
from selenium.common import NoAlertPresentException
from .pages.product_page import ProductPage
from .pages.main_page import *
import math
#
# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

# @pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_able_to_add_to_basket()
    page.solve_quiz_and_get_code()



