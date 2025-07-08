from selenium.webdriver.common.by import By
from src.base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SidebarMenuPage(BasePage):
    MENU_BUTTON = (By.ID, "menu-toggle")
    SIDEBAR = (By.ID, "sidebar-wrapper")
    HOME_LINK = (By.LINK_TEXT, "Home")
    HISTORY_LINK = (By.LINK_TEXT, "History")
    PROFILE_LINK = (By.LINK_TEXT, "Profile")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu(self):
        """Open the sidebar menu with proper waits"""
        self.wait_for_page_load()
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        ).click()
        # Wait for sidebar animation to complete
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.SIDEBAR)
        )

    def go_to_history(self):
        """Navigate to History page with proper waits"""
        self.wait_for_page_load()
        self.open_menu()
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.HISTORY_LINK)
        ).click()
        self.wait_for_page_load()

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