from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, ".register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ANY_ALERT_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    PRICE_MAIN = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main")




