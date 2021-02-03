from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import CartPageLocators
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
import math
import time


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(
            *ProductPageLocators.BUTTON_ADD)
        button.click()

    def should_be_cart_product_price(self):
        price_product = self.browser.find_element(
            *CartPageLocators.PRICE_PRODUCT_CART).text
        price_cart = self.browser.find_element(
            *CartPageLocators.PRICE_CART).text
        assert price_product == price_cart, "Цена товара в каталоге не совпадает с ценой в корзине"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        time.sleep(5)

    def should_be_product_to_basket(self):
        assert self.browser.switch_to.alert, "alert is not presented"

    def should_be_message_adding_to_busket(self):
        expected_message = "has been added to your basket."
        actual_message = self.browser.find_element(
            *CartPageLocators.MESSAGE_ADDING_TO_BUSKET).text
        print("Сообщение!!!!!!!!!!", actual_message)
        assert expected_message in actual_message, "Product has NOT been added to your basket."
