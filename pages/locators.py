from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")

class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//*[@id='login_form']")
    REGISTRATION_FORM = (By.XPATH, "//*[@id='register_form']")

