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
