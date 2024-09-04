import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class MainPage(BasePage):
    SEARCH_INPUT = By.CSS_SELECTOR, "#search > input"
    SEARCH_BUTTON = By.CSS_SELECTOR, "#search > button"
    SEARCH_ELEMENT = By.CSS_SELECTOR, "#product-search > ul > li:nth-child(2) > a"
    CART_BUTTON = By.CSS_SELECTOR, "#header-cart > div > button"
    MAIN_ELEMENTS = By.CSS_SELECTOR, "#narbar-menu"
    FEATURED = By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div"
    FEATURED_ONE = By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1)"
    FEATURED_TWO = By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(2)"
    FEATURED_THREE = By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(3)"
    FEATURED_FOUR = By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(3)"
    FEATURED_PRODUCT_NAME = By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a"
    CURRENCY = By.CSS_SELECTOR, "#form-currency > div"
    CURRENCY_EURO = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(1) > a"
    CURRENCY_POUND = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > a"
    CURRENCY_DOLLAR = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(3) > a"
    CART = By.CSS_SELECTOR, "#header-cart > div > button"

    @allure.step("Выполняю поиск по значению: {value}")
    def main_search(self, value):
        self.input_value(self.SEARCH_INPUT, value)
        self.click(self.SEARCH_BUTTON)
        self.get_element(self.SEARCH_ELEMENT)
        return self