import datetime
import logging
import allure
import pytest
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.31.66")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", default="192.168.31.66")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--bv")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--video", action="store_true")



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
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    executor_url = f"http://{executor}:4444/wd/hub"

    if executor == "local":
        caps = {"goog:chromeOption": {}}

        if browser_name == "chrome":
            service = ChromeService()
            options = ChromeOptions()
            if headless_mode:
                options.add_argument("headless=new")
                options.add_argument("--no-sandbox")
            driver = webdriver.Chrome(service=service)
        elif browser_name == "firefox":
            service = FirefoxService()
            options = FirefoxOptions()
            if headless_mode:
                options.add_argument("headless")
            driver = webdriver.Firefox(service=service)
    else:
        if browser_name == "chrome":
            options = ChromeOptions()
            # options.add_argument("headless=new")
            options.set_capability("browserName", browser_name)
        elif browser_name == "firefox":
            options = FirefoxOptions()
            # options.add_argument("--headless")
            options.set_capability("browserName", browser_name)

        caps = {
            "browserName": browser_name,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc,
                "name": request.node.name,
                "screenResolution": "1280x2000",
                "enableVideo": video,
                "enableLog": logs,
                "timeZone": "Europe/Moscow",
                "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]
            },
            "acceptInsecureCerts": True,
        }

        for k, v in caps.items():
            options.set_capability(k, v)

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )

    driver.maximize_window()

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    driver.log_level = 'INFO'
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % driver)

    def finalizer():
        driver.quit()

    request.addfinalizer(finalizer)
    return driver