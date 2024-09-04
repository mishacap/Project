import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MainPage(BasePage):
    CURRENCY = By.CSS_SELECTOR, "#form-currency > div"
    CURRENCY_EURO = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(1) > a"
    CURRENCY_POUND = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(2) > a"
    CURRENCY_DOLLAR = By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(3) > a"
    CART = By.CSS_SELECTOR, "#header-cart > div > button"
    FEATURED = By.CSS_SELECTOR, "#content > div.row.row-cols-1.row-cols-sm-2.row-cols-md-3.row-cols-xl-4 > div:nth-child(1) > div"

    def click_currency_dropdown(self):
        self.is_present(self.CURRENCY)
        self.click(self.CURRENCY)
        return self

    def change_currency_euro(self):
        self.click(self.CURRENCY)
        self.is_present(self.CURRENCY_EURO)
        self.click(self.CURRENCY_EURO)
        return self

    def change_currency_pound(self):
        self.click(self.CURRENCY)
        self.is_present(self.CURRENCY_POUND)
        self.click(self.CURRENCY_POUND)
        return self

    def change_currency_dollar(self):
        self.click(self.CURRENCY)
        self.is_present(self.CURRENCY_DOLLAR)
        self.click(self.CURRENCY_DOLLAR)
        return self

    def currency_check(self):
        currency_element = self.get_element(self.CURRENCY)
        return currency_element.text

    def currency_cart_check(self):
        currency_element = self.get_element(self.CART)
        return currency_element.text

    def currency_featured_check(self):
        currency_element = self.get_element(self.FEATURED)
        return currency_element.text

