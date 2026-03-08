from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    # Получаем название товара
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # Получаем цену товара
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    # Проверка названия
    def should_be_correct_product_name(self, product_name):
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == message_name, "Product name in message is incorrect"

    # Проверка цены
    def should_be_correct_product_price(self, product_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price == basket_total, "Basket total is incorrect"