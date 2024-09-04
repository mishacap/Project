import allure
from conftest import browser, base_url
from helpers import get_fake_product
from page_objects.main_page import MainPage


def test_main_search(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    main_page.main_search(get_fake_product())