import allure
import selenium.common.exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def get_element(self, locator: tuple, timeout=3):
        self.logger.info("%s: Get element: %s" % (self.class_name, str(locator)))
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def get_alert(self, locator: tuple, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.alert_is_present(locator))

    def click(self, locator: tuple):
        self.logger.info("%s: Clicking element: %s" % (self.class_name, str(locator)))
        ActionChains(self.browser).move_to_element(self.get_element(locator)).pause(0.3).click().perform()

    def input_value(self, locator: tuple, text: str):
        self.logger.info("%s: Input %s in input %s" % (self.class_name, text, locator))
        self.get_element(locator).click()
        self.get_element(locator).click()
        for l in text:
            self.get_element(locator).send_keys(l)

    def is_present(self, locator: tuple, timeout=3):
        self.logger.info("%s: Wait element: %s" % (self.class_name, locator))
        try:
            return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        except selenium.common.exceptions.TimeoutException:
            raise AssertionError
