from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)

        password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        password1_field.send_keys(password)

        password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        password2_field.send_keys(password)

        submit_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BTN)
        submit_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "login" in self.url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

