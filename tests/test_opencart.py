import time

import allure
from conftest import browser, base_url
from helpers import get_fake_product, get_user_data, get_random_user, get_credentials
from page_objects.administration_page import AdministrationPage
from page_objects.main_page import MainPage
from page_objects.registration_page import RegistrationPage


def test_main_elements(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    main_page.wait_main_elements()

def test_main_search(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    data = get_fake_product()
    main_page.main_search(data)
    value = main_page.search_check()
    assert data in value

def test_registration_elements(browser, base_url):
    browser.get(f"{base_url}:8081/index.php?route=account/register")
    registration_page = RegistrationPage(browser)
    registration_page.wait_registration_elements()

def test_registration_new_user(browser, base_url):
    browser.get(f"{base_url}:8081/index.php?route=account/register")
    registration_page = RegistrationPage(browser)
    user_data = get_user_data()
    registration_page.registration(*user_data)
    registration_status = registration_page.registration_check()
    assert "Register Account" in registration_status

def test_user_login(browser, base_url):
    browser.get(f"{base_url}:8081/")
    main_page = MainPage(browser)
    user_data = get_random_user()
    main_page.main_login(*user_data)

def test_administration_login_logout(browser, base_url):
    browser.get(f"{base_url}:8081/administration/")
    admin_page = AdministrationPage(browser)
    admin_data = get_credentials()
    admin_page.login(*admin_data)
    admin_page.logout()