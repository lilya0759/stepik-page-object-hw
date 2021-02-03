from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form_Q")


class ProductPageLocators():
    BUTTON_ADD = (
        By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    # PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")


class CartPageLocators():
    MESSAGE_ADDING_TO_BUSKET = (By.CSS_SELECTOR, "div.alertinner")
    PRICE_CART = (By.CSS_SELECTOR, "#messages div:nth-child(3)>div strong")
    PRICE_PRODUCT_CART = (By.CSS_SELECTOR, "p.price_color")
