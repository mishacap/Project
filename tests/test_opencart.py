import time

import allure
from conftest import browser, base_url
from helpers import get_fake_product, get_user_data, get_random_user, get_credentials
from page_objects.administration_page import AdministrationPage
from page_objects.currency_page import CurrencyPage
from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage
from page_objects.registration_page import RegistrationPage


@allure.epic("Opencart")
@allure.feature("Main page")
@allure.story("Elements")
@allure.title("Main page elements check")
def test_main_elements(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    main_page.wait_main_elements()

@allure.epic("Opencart")
@allure.feature("Main page")
@allure.story("Search")
@allure.title("Search non existing data")
def test_main_search(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    data = get_fake_product()
    main_page.main_search(data)
    value = main_page.search_check()
    assert data in value

@allure.epic("Opencart")
@allure.feature("Main page")
@allure.story("Elements")
@allure.title("Registration elements check")
def test_registration_elements(browser, base_url):
    browser.get(f"{base_url}:8081/index.php?route=account/register")
    registration_page = RegistrationPage(browser)
    registration_page.wait_registration_elements()

@allure.epic("Opencart")
@allure.feature("Registration page")
@allure.story("Registration")
@allure.title("Registration new user")
def test_registration_new_user(browser, base_url):
    browser.get(f"{base_url}:8081/index.php?route=account/register")
    registration_page = RegistrationPage(browser)
    user_data = get_user_data()
    registration_page.registration(*user_data)
    registration_status = registration_page.registration_check()
    assert "Register Account" in registration_status

@allure.epic("Opencart")
@allure.feature("Main page")
@allure.story("Login")
@allure.title("User login")
def test_user_login(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    user_data = get_random_user()
    main_page.main_login(*user_data)

@allure.epic("Opencart")
@allure.feature("Admin page")
@allure.story("Login")
@allure.title("Administrator account login")
def test_administration_login_logout(browser, base_url):
    browser.get(f"{base_url}:8081/administration/")
    admin_page = AdministrationPage(browser)
    admin_data = get_credentials()
    admin_page.login(*admin_data)
    admin_page.logout()

@allure.epic("Opencart")
@allure.feature("Main page")
@allure.story("Сurrency")
@allure.title("Сurrency change to euro")
def test_change_currency_euro(browser, base_url):
    browser.get(f"{base_url}:8081/")
    currency_page = CurrencyPage(browser)
    currency_page.change_currency_euro()
    currency = currency_page.currency_check()
    assert "€" in currency
    currency_cart = currency_page.currency_cart_check()
    assert "€" in currency_cart
    currency_featured = currency_page.currency_featured_check()
    assert "€" in currency_featured

@allure.epic("Opencart")
@allure.feature("Main page")
@allure.story("Сurrency")
@allure.title("Сurrency change to pound")
def test_change_currency_pound(browser, base_url):
    browser.get(f"{base_url}:8081/")
    currency_page = CurrencyPage(browser)
    currency_page.change_currency_pound()
    currency = currency_page.currency_check()
    assert "£" in currency
    currency_cart = currency_page.currency_cart_check()
    assert "£" in currency_cart
    currency_featured = currency_page.currency_featured_check()
    assert "£" in currency_featured

@allure.epic("Opencart")
@allure.feature("Main page")
@allure.story("Сurrency")
@allure.title("Сurrency change to dollar")
def test_change_currency_dollar(browser, base_url):
    browser.get(f"{base_url}:8081/")
    currency_page = CurrencyPage(browser)
    currency_page.change_currency_dollar()
    currency = currency_page.currency_check()
    assert "$" in currency
    currency_cart = currency_page.currency_cart_check()
    assert "$" in currency_cart
    currency_featured = currency_page.currency_featured_check()
    assert "$" in currency_featured

@allure.epic("Opencart")
@allure.feature("Product page")
@allure.story("Addition")
@allure.title("Add to cart")
def test_add_featured_to_cart(browser, base_url):
    browser.get(f"{base_url}:8081/")
    product_page = ProductPage(browser)
    product_page.click_featured_product()
    product_page.add_to_cart()
    product_page.close_alert()
    product_page.item_in_cart_check()

@allure.epic("Opencart")
@allure.feature("Product page")
@allure.story("Addition")
@allure.title("Add to comparison")
def test_add_to_compare(browser, base_url):
    browser.get(f"{base_url}:8081/")
    product_page = ProductPage(browser)
    product_page.click_featured_product()
    product_page.add_to_compare()
    product_page.click_alert()
    product_page.comparison_check()

@allure.epic("Opencart")
@allure.feature("Product page")
@allure.story("Addition")
@allure.title("Add to wishlist")
def test_add_to_wishlist(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    user_data = get_random_user()
    main_page.main_login(*user_data)
    main_page.go_to_main()
    product_page = ProductPage(browser)
    product_page.click_featured_product()
    product_page.add_to_wishlist()
    product_page.click_alert()
    product_page.wishlist_check()
