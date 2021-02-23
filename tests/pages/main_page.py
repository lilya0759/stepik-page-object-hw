from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import CartPageLocators
# from tests.pages.login_page import LoginPage


class MainPage(BasePage):
    # переход на страницу логина
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
