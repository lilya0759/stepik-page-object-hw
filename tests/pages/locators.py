from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REGISTER_PASS_1 = (By.XPATH, "//input[@name='registration-password1']")
    REGISTER_PASS_2 = (By.XPATH, "//input[@name='registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators():
    BUTTON_ADD = (
        By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_ADDING_TO_BUSKET = (By.CSS_SELECTOR, "div.alertinner")
    PRICE_CART = (By.CSS_SELECTOR, "#messages div:nth-child(3)>div strong")
    PRICE_PRODUCT_CART = (By.CSS_SELECTOR, "p.price_color")
    # PRICE_CART = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs")


class CartPageLocators():
    EMPTY_MESSAGE_CART = (By.XPATH, "//div[@id='content_inner']/p")
    CART_TITLE = (By.XPATH, "//div[@id='content_inner']/div")
    CART_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    CART_DESC_OF_ORDER = (By.XPATH, "//div[@id='content_inner']/div[2]")


class BasePageLocators():
    CART_LINK = (By.CSS_SELECTOR, "div.basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
