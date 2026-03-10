from .base_page import BasePage
from .locators import LoginPageLocators
from faker import Faker

class LoginPage(BasePage):

    def should_be_login_url(self):
        # Проверка, что в текущем URL есть подстрока "login"
        assert "login" in self.browser.current_url, "Login URL is not correct"

    def should_be_login_form(self):
        # Проверка, что форма логина присутствует
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # Проверка, что форма регистрации присутствует
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_repeat = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        password_repeat.send_keys(password)
        register_button.click()
