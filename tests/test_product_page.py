from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.base_page import BasePage
import pytest
import time

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_adding_to_busket()
    page.should_be_cart_product_price()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message_disappeared()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.should_be_empty_cart()


@pytest.mark.xfail
def test_guest_can_see_message_about_empty_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.open_cart_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_message_empty_cart()


@pytest.mark.xfail
def test_guest_cant_see_message_about_empty_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.open_cart_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_message_empty_cart()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture
    def registration_user(self, browser):
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "pass"
        login_page.register_new_user(email, password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, registration_user):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_message_adding_to_busket()
        page.should_be_cart_product_price()

    def test_user_cant_see_success_message(self, browser, registration_user):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
