from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import CartPageLocators
# from tests.pages.login_page import LoginPage


class MainPage(BasePage):
    # переход на страницу логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(
            *MainPageLocators.LOGIN_LINK)
        login_link.click()

    # проверка наличия элемента(ссылки)

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.LOGIN_LINK), "Login link is not presented"
