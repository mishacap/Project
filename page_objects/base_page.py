import allure
import selenium.common.exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.class_name = type(self).__name__

    def get_element(self, locator: tuple, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def get_alert(self, locator: tuple, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.alert_is_present(locator))

    def click(self, locator: tuple):
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(0.3).click().perform()

    def input_value(self, locator: tuple, text: str):
        self.get_element(locator).click()
        self.get_element(locator).click()
        for l in text:
            self.get_element(locator).send_keys(l)

    def is_present(self, locator: tuple, timeout=3):
        try:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except selenium.common.exceptions.TimeoutException:
            raise AssertionError
