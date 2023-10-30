from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import *


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'

    page = BasePage(browser, link)
    page.open()
    page.should_be_able_to_go_to_basket()

    basket_page_link = browser.current_url
    basket_page = BasketPage(browser, basket_page_link)
    basket_page.should_not_see_incorrect_empty_basket_message()
    basket_page.should_be_empty_basket()
