from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    # Локаторы
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")

    # Проверка, что корзина пуста
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*self.BASKET_ITEMS), "Basket is not empty"
        empty_text = self.browser.find_element(*self.EMPTY_BASKET_TEXT).text
        assert "empty" in empty_text.lower(), "No message about empty basket"