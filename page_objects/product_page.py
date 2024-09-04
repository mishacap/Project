
import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import time

class ProductPage(BasePage):
    FEATURED_PRODUCT_NAME = By.CSS_SELECTOR, "#content > div.row .product-thumb h4 a"
    ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "#button-cart"
    CART = By.CSS_SELECTOR, "#header-cart > div > button"
    REMOVE_BUTTON = By.CSS_SELECTOR, "#header-cart > div > ul > li > table > tbody > tr > td:nth-child(5) > form > button"
    CLOSE_ALERT = By.CSS_SELECTOR, "#alert > div > button"

    def click_featured_product(self, index=0):
        if index == 0:
            self.click(self.FEATURED_PRODUCT_NAME)
        else:
            self.get_elements(self.FEATURED_PRODUCT_NAME)[index].click()

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        return self

    def close_alert(self):
        self.click(self.CLOSE_ALERT)
        return self

    def item_in_cart_check(self):
        self.is_present(self.CART)
        self.click(self.CART)
        self.is_present(self.REMOVE_BUTTON)
        return self



