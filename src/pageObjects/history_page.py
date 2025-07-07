from selenium.webdriver.common.by import By
from src.base.base_page import BasePage

class HistoryPage(BasePage):
    # You can customize this locator depending on how appointments are listed
    APPOINTMENT_CARD = (By.XPATH, "//section[@id='history']//div[contains(@class,'row')]")

    def __init__(self, driver):
        super().__init__(driver)

    def is_appointment_listed(self):
        return self.is_visible(self.APPOINTMENT_CARD)
