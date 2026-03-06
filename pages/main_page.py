from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            "Login link is not presented"
        login_link.click()


    def should_be_login_link(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTER_FOR), \
            "Register form is not presented"
