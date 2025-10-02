import os
import sys
import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.attach import add_screenshot, add_logs, add_html, add_video


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    yield browser

    add_screenshot(browser)
    add_logs(browser)
    add_html(browser)
    add_video(browser)

    browser.quit()
