from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url, "url is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL)
        reg_email.send_keys(email)
        reg_pass_1 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASS_1)
        reg_pass_1.send_keys(password)
        reg_pass_2 = self.browser.find_element(
            *LoginPageLocators.REGISTER_PASS_2)
        reg_pass_2.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        btn.click()
