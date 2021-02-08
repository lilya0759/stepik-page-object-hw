from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .locators import CartPageLocators
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_empty_cart(self):
        self.open_cart_page()
        self.should_be_message_empty_cart()
        self.should_not_be_title_of_product_in_empty_cart()
        self.should_not_be_formset_cart_in_empty_cart()
        self.should_not_be_desc_of_order_in_empty_cart()

    def should_be_message_empty_cart(self):
        assert self.is_element_present(
            *CartPageLocators.EMPTY_MESSAGE_CART), "Нет уведомления, что корзина пуста"

    def should_not_be_title_of_product_in_empty_cart(self):
        assert self.is_not_element_present(
            *CartPageLocators.CART_TITLE), "Отображаются заголовки таблицы с товарами"

    def should_not_be_formset_cart_in_empty_cart(self):
        assert self.is_not_element_present(
            *CartPageLocators.CART_FORMSET), "Отображается таблица с товарами"

    def should_not_be_desc_of_order_in_empty_cart(self):
        assert self.is_not_element_present(
            *CartPageLocators.CART_DESC_OF_ORDER), "Отображается описание к заказу"
