from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def click(self, by_locator):
        WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self,by_locator,text,):
        WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    def wait_for_element(self, by_locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))

    def select_dropdown(self, locator, visible_text):
        element = self.driver.find_element(*locator)
        dropdown = Select(element)
        dropdown.select_by_visible_text(visible_text)