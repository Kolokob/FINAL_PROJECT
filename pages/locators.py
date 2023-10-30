from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//*[@id='login_form']")
    REGISTRATION_FORM = (By.XPATH, "//*[@id='register_form']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK_NAME_AFTER_ADDED_TO_BASKET_MESSAGE = (By.XPATH, "//strong[contains(text(),'Coders at Work')]")
    BOOK_NAME = (By.XPATH, "//h1[contains(text(),'Coders at Work')]")
    BOOK_PRICE = (By.XPATH, "//p[contains(text(),'£19.99')]")
    BOOK_PRICE_IN_MESSAGE = (By.XPATH, "//strong[contains(text(),'£19.99')]")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-of-type(1) strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.XPATH, "//a[@class='btn btn-default']")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']")
    EMPTY_BASKET_INCORRECT_MESSAGE = (By.XPATH, "//h2[contains(text(),'Items to buy now')]")
