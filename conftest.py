import pytest
from selenium import webdriver
import os

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()

    # For CI: run in headless mode
    Headless = True
    if Headless:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    # 🔧 Prevent SessionNotCreatedException in CI
    options.add_argument("--user-data-dir=/tmp/unique-profile")

    # Use custom Chrome binary if running locally
    chrome_path = "/usr/local/bin/chromium-114/chrome"
    if os.path.exists(chrome_path):
        options.binary_location = chrome_path

    # Use Selenium Manager to auto-download ChromeDriver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver
    driver.quit()
