import pytest
from selenium import webdriver
driver = None
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def setup_and_teardown(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(config.get("Url","base_url"))
    request.cls.driver = driver
    yield
    driver.quit()
