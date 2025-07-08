# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# @pytest.fixture
# def browser():
#     options = webdriver.ChromeOptions()
#     options.binary_location = "/usr/local/bin/chromium-114/chrome"

#     service = Service(executable_path="/usr/local/bin/chromedriver")

#     driver = webdriver.Chrome(service=service, options=options)
#     driver.maximize_window()

#     yield driver 
#     driver.quit()

import pytest
from selenium import webdriver
import os

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()

    # For CI: run in headless mode
    Headless = False
    if Headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    # If running locally with custom Chrome
    chrome_path = "/usr/local/bin/chromium-114/chrome"
    if os.path.exists(chrome_path):
        options.binary_location = chrome_path

    # Use Selenium Manager to auto-download ChromeDriver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver
    driver.quit()
