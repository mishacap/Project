
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

    COMPARE_BUTTON = By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > form > div > button:nth-child(2)"
    COMPARISON_WISHLIST_PAGE = By.CSS_SELECTOR, "#alert > div > a:nth-child(3)"
    COMPARISON_REMOVE_BUTTON = By.CSS_SELECTOR, "#content > table > tbody:nth-child(7) > tr > td.text-center > form > a"
    COMPARISON_ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "#button-confirm"

    ADD_TO_WISHLIST_BUTTON = By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(2) > form > div > button:nth-child(1)"
    WISHLIST_REMOVE_BUTTON = By.CSS_SELECTOR, "#wishlist > div > table > tbody > tr > td:nth-child(6) > form > button.btn.btn-danger"
    WISHLIST_ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "#wishlist > div > table > tbody > tr > td:nth-child(6) > form > button.btn.btn-primary"
    WISHLIST_CONTINUE_BUTTON = By.CSS_SELECTOR, "#content > div.text-end > a"
    WISHLIST = By.CSS_SELECTOR, "div > a:nth-child(5)"

    @allure.step("Кликаю на товар из подборки")
    def click_featured_product(self, index=0):
        if index == 0:
            self.click(self.FEATURED_PRODUCT_NAME)
        else:
            self.get_elements(self.FEATURED_PRODUCT_NAME)[index].click()

    @allure.step("Добавляю товар в корзину")
    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        return self

    @allure.step("Добавляю товар в сравнение")
    def add_to_compare(self):
        self.click(self.COMPARE_BUTTON)
        return self

    @allure.step("Кликаю по алерту")
    def click_alert(self):
        self.click(self.COMPARISON_WISHLIST_PAGE)
        return self

    @allure.step("Закрываю алерт")
    def close_alert(self):
        self.click(self.CLOSE_ALERT)
        return self

    @allure.step("Проверяю наличие товара в корзине")
    def item_in_cart_check(self):
        self.is_present(self.CART)
        self.click(self.CART)
        self.is_present(self.REMOVE_BUTTON)
        return self

    @allure.step("Проверяю наличие товара в сравнении")
    def comparison_check(self):
        self.is_present(self.COMPARISON_REMOVE_BUTTON)
        self.is_present(self.COMPARISON_ADD_TO_CART_BUTTON)
        return self

    @allure.step("Добавляю товар в вишлист")
    def add_to_wishlist(self):
        self.click(self.ADD_TO_WISHLIST_BUTTON)
        return self

    @allure.step("Проверяю наличие товара в вишлисте")
    def wishlist_check(self):
        self.is_present(self.WISHLIST_REMOVE_BUTTON)
        self.is_present(self.WISHLIST_ADD_TO_CART_BUTTON)
        self.is_present(self.WISHLIST_CONTINUE_BUTTON)
        return self

