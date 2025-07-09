from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
        self.timeout = 20  # Increased timeout for CI

    def open_menu(self):
        """Open the sidebar menu with multiple fallback strategies"""
        self.wait_for_page_load()
        
        # Try different strategies to open the menu
        strategies = [
            self._open_with_standard_click,
            self._open_with_javascript_click,
            self._open_with_action_chain
        ]
        
        for attempt, strategy in enumerate(strategies, 1):
            try:
                strategy()
                # Verify menu opened
                WebDriverWait(self.driver, 5).until(
                    lambda d: d.find_element(*self.SIDEBAR).is_displayed()
                )
                return
            except Exception as e:
                if attempt == len(strategies):
                    raise
                time.sleep(1)

    def _open_with_standard_click(self):
        """Standard click approach"""
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        ).click()

    def _open_with_javascript_click(self):
        """JavaScript click as fallback"""
        button = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.MENU_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def _open_with_action_chain(self):
        """Action chains click as fallback"""
        button = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.MENU_BUTTON)
        )
        ActionChains(self.driver).move_to_element(button).click().perform()

    def go_to_history(self):
        """Navigate to History page with enhanced reliability"""
        self.wait_for_page_load()
        self.open_menu()
        
        # Scroll into view and click
        history_link = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.HISTORY_LINK)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", history_link)
        history_link.click()
        
        # Wait for history page to load
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.ID, "history"))
        )

    def logout(self):
        """Enhanced logout with multiple checks"""
        self.wait_for_page_load()
        self.open_menu()
        
        logout_link = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        )
        logout_link.click()
        
        # Wait for logout to complete
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: "CURA Healthcare" in d.title or "login" in d.current_url.lower()
        )