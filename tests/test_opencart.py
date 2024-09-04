import allure
from conftest import browser, base_url
from helpers import get_fake_product
from page_objects.main_page import MainPage


def test_main_search(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    data = get_fake_product()
    main_page.main_search(data)
    value = main_page.search_check()
    assert data in value

