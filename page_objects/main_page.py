import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class MainPage(BasePage):
    SEARCH_INPUT = By.CSS_SELECTOR, "#search > input"
    SEARCH_BUTTON = By.CSS_SELECTOR, "#search > button"
    SEARCH_ELEMENT = By.CSS_SELECTOR, "#product-search > ul > li:nth-child(2) > a"
    SEARCH_VALUE = By.CSS_SELECTOR, "#content > h1"


    def main_search(self, value):
        self.input_value(self.SEARCH_INPUT, value)
        self.click(self.SEARCH_BUTTON)
        self.get_element(self.SEARCH_ELEMENT)
        return self

    def search_check(self):
        search_value = self.get_element(self.SEARCH_VALUE)
        return search_value.text