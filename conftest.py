import pytest
from selenium import webdriver
import os
import tempfile

@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    tmp_profile_dir = tempfile.mkdtemp()

    # Optional headless setup
    if True:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument(f"--user-data-dir={tmp_profile_dir}")

    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    chrome_path = "/usr/local/bin/chromium-114/chrome"
    if os.path.exists(chrome_path):
        options.binary_location = chrome_path
    elif os.path.exists("/usr/bin/google-chrome"):
        options.binary_location = "/usr/bin/google-chrome"

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    # ✅ Log versions
    # chrome_version = driver.capabilities.get("browserVersion")
    # driver_version = driver.capabilities.get("chrome", {}).get("chromedriverVersion", "unknown").split(' ')[0]

    # print(f"\n✅ Chrome version: {chrome_version}")
    # print(f"✅ ChromeDriver version: {driver_version}")

    yield driver

    # Save success screenshot before teardown
    if request.node.rep_call.passed:
        save_screenshot(driver, request.node, passed=True)

    # ✅ Print filtered browser logs
    print("\n📜 Filtered Browser Logs:")
    for entry in driver.get_log("browser"):
        message = entry.get("message", "")
        
        # Skip noisy logs
        if any(skip in message for skip in [
            "favicon.ico",
            "Slow network is detected",
            "Fallback font will be used"
        ]):
            continue

        print(entry)

    driver.quit()


def save_screenshot(driver, node, passed=False):
    test_name = node.nodeid.split("::")[-1].replace("/", "_").replace("\\", "_")

    folder = os.path.join("test-results", "screenshots")
    os.makedirs(folder, exist_ok=True)

    status = "PASSED" if passed else "FAILED"
    screenshot_path = os.path.join(folder, f"{status}_{test_name}.png")

    try:
        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved to: {screenshot_path}")
        if os.getenv("GITHUB_ACTIONS") == "true":
            print(f"::notice::Screenshot saved: {screenshot_path}")
    except Exception as e:
        print(f"\nFailed to capture screenshot: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

    # Only take failure screenshot after "call"
    if rep.when == "call" and rep.failed:
        if "browser" in item.funcargs:
            browser = item.funcargs["browser"]
            save_screenshot(browser, item, passed=False)
