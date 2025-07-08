import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def wait_for_page_load(self):
        """Wait until the page's document.readyState is 'complete'."""
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def click(self, by_locator):
        """Click an element after waiting for it to be clickable, with retry for stale elements."""
        for attempt in range(2):  # retry once on stale
            try:
                element = WebDriverWait(self.driver, self.timeout).until(
                    EC.element_to_be_clickable(by_locator)
                )
                element.click()
                return
            except StaleElementReferenceException:
                if attempt == 1:
                    raise
                time.sleep(1)  # slight delay before retry

    def enter_text(self, by_locator, text):
        """Enter text into an input field once it's visible."""
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(by_locator)
        ).send_keys(text)

    def get_text(self, by_locator):
        """Get visible text from an element."""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(by_locator)
        )
        return element.text

    def is_visible(self, by_locator):
        """Return True if the element is visible."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(by_locator)
            )
            return bool(element)
        except:
            return False

    def wait_for_element(self, by_locator):
        """Wait until a specific element is visible and return it."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(by_locator)
        )

    def select_dropdown(self, locator, visible_text):
        """Select a value from a dropdown using visible text."""
        element = self.driver.find_element(*locator)
        dropdown = Select(element)
        dropdown.select_by_visible_text(visible_text)
