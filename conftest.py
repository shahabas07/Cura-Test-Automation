import pytest
from selenium import webdriver
import os

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    
    # Enhanced headless options
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--user-data-dir=/tmp/chrome-profile")
    
    # Enable browser logging
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    
    # Use custom Chrome binary if available
    chrome_path = "/usr/local/bin/chromium-114/chrome"
    if os.path.exists(chrome_path):
        options.binary_location = chrome_path

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)  # Add implicit wait as fallback
    
    yield driver
    
    # Print browser logs for debugging
    print("\nBrowser logs:")
    for entry in driver.get_log("browser"):
        print(entry)
    
    driver.quit()