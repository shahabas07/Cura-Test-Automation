from selenium.webdriver.common.by import By
from src.base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SidebarMenuPage(BasePage):
    MENU_BUTTON = (By.ID, "menu-toggle")
    SIDEBAR = (By.ID, "sidebar-wrapper")
    HOME_LINK = (By.LINK_TEXT, "Home")
    HISTORY_LINK = (By.LINK_TEXT, "History")
    PROFILE_LINK = (By.LINK_TEXT, "Profile")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)
        self.timeout = 15  # Increased timeout for CI

    def open_menu(self):
        """Open the sidebar menu with proper waits and retries"""
        self.wait_for_page_load()
        
        for attempt in range(3):
            try:
                WebDriverWait(self.driver, self.timeout).until(
                    EC.element_to_be_clickable(self.MENU_BUTTON)
                ).click()
                
                WebDriverWait(self.driver, self.timeout).until(
                    lambda d: d.find_element(*self.SIDEBAR).is_displayed() and 
                    d.find_element(*self.SIDEBAR).get_attribute("class") == "active"
                )
                return
            except Exception as e:
                if attempt == 2:
                    raise
                time.sleep(1)

    def go_to_history(self):
        """Navigate to History page with proper waits"""
        self.wait_for_page_load()
        self.open_menu()
        
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.HISTORY_LINK)
        ).click()
        
        self.wait_for_page_load()
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.ID, "history"))
        )

    def go_to_home(self):
        """Navigate to Home page with proper waits"""
        self.wait_for_page_load()
        self.open_menu()
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.HOME_LINK)
        ).click()
        self.wait_for_page_load()

    def go_to_profile(self):
        """Navigate to Profile page with proper waits"""
        self.wait_for_page_load()
        self.open_menu()
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.PROFILE_LINK)
        ).click()
        self.wait_for_page_load()

    def logout(self):
        """Logout with proper waits"""
        self.wait_for_page_load()
        self.open_menu()
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        ).click()
        self.wait_for_page_load()