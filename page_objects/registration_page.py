import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class RegistrationPage(BasePage):
    FIRST_NAME_INPUT = By.CSS_SELECTOR, "#input-firstname"
    LAST_NAME_INPUT = By.CSS_SELECTOR, "#input-lastname"
    EMAIL_INPUT = By.CSS_SELECTOR, "#input-email"
    PASSWORD_INPUT = By.CSS_SELECTOR, "#input-password"
    CONTINUE_BUTTON = By.CSS_SELECTOR, "#form-register > div > button"
    PRIVACY_POLICY_SWITCHER = By.CSS_SELECTOR, "#form-register > div > div > input"
    ACCOUNT_HAS_BEEN_CREATED = By.CSS_SELECTOR, "#content > h1"

    def wait_registration_elements(self):
        self.is_present(self.FIRST_NAME_INPUT)
        self.is_present(self.LAST_NAME_INPUT)
        self.is_present(self.EMAIL_INPUT)
        self.is_present(self.PASSWORD_INPUT)
        self.is_present(self.CONTINUE_BUTTON)
        self.is_present(self.PRIVACY_POLICY_SWITCHER)
        return self

    def registration(self, firstname, lastname, email, password):
        self.input_value(self.FIRST_NAME_INPUT, firstname)
        self.input_value(self.LAST_NAME_INPUT, lastname)
        self.input_value(self.EMAIL_INPUT, email)
        self.input_value(self.PASSWORD_INPUT, password)
        self.click(self.PRIVACY_POLICY_SWITCHER)
        self.click(self.CONTINUE_BUTTON)
        self.get_element(self.ACCOUNT_HAS_BEEN_CREATED)
        return self
