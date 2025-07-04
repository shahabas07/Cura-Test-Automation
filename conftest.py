import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.binary_location = "/usr/local/bin/chromium-114/chrome"

    service = Service(executable_path="/usr/local/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    yield driver  # Pass driver to test
    driver.quit()