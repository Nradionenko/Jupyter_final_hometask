from pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class LoginLocators:
    LOCATOR_EPAM_SSO = (By.ID, "zocial-epam-idp")
    LOCATOR_LOGIN_FIELD = (By.NAME, "UserName")
    LOCATOR_PASSWORD_FIELD = (By.NAME, "Password")
    LOCATOR_SUBMIT_BUTTON = (By.ID, "submitButton")


class LoginHelper(BasePage):

    def epam_sso(self):
        search_field = self.find_element(LoginLocators.LOCATOR_EPAM_SSO)
        search_field.click()

    def enter_login(self, login):
        search_field = self.find_element(LoginLocators.LOCATOR_LOGIN_FIELD)
        search_field.click()
        search_field.send_keys(login)

    def enter_password(self, password):
        search_field = self.find_element(LoginLocators.LOCATOR_PASSWORD_FIELD)
        search_field.click()
        search_field.send_keys(password)

    def click_on_submit_button(self):
        self.find_element(LoginLocators.LOCATOR_SUBMIT_BUTTON, time=10).click()
