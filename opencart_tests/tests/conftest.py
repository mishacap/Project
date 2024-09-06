import datetime
import logging

import allure
import pytest
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.31.66")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--url")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "chrome":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        browser = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "firefox":
        options = FFOptions()
        if headless_mode:
            options.add_argument("--headless")
        browser = webdriver.Firefox(service=FFService(), options=FFOptions())
    else:
        raise ValueError(f"Browser {browser_name} not supported")

    allure.attach(
        name=browser.session_id,
        body=json.dumps(browser.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )

    browser.logger = logger
    logger.info("Browser %s started" % browser_name)

    browser.maximize_window()

    yield browser

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=browser.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )

    browser.close()
    logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))
