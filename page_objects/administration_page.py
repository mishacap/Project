import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class AdministrationPage(BasePage):
    USER_NAME = By.CSS_SELECTOR, "#input-username"
    PASSWORD = By.CSS_SELECTOR, "#input-password"
    LOGIN_BUTTON = By.CSS_SELECTOR, "#form-login > div.text-end > button"
    LOGOUT_BUTTON = By.CSS_SELECTOR, "#nav-logout > a"

    @allure.step("Выполняю логин с именем:{username} и паролем:{password}")
    def login(self, username, password):
        self.input_value(self.USER_NAME, username)
        self.input_value(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        return self

    @allure.step("Выполняю логаут")
    def logout(self):
        self.is_present(self.LOGOUT_BUTTON)
        self.click(self.LOGOUT_BUTTON)
        return self
