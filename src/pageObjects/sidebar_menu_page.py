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

    # def open_menu(self):
    #     self.click(self.MENU_BUTTON)

    def open_menu(self):
    # Instead of storing element early, always find it fresh
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        ).click()
        time.sleep(0.5)


    def go_to_history(self):
        self.wait_for_page_load() 
        self.open_menu()
        self.wait_for_element(self.HISTORY_LINK)
        self.click(self.HISTORY_LINK)

    def go_to_home(self):
        self.open_menu()
        self.click(self.HOME_LINK)

    def go_to_profile(self):
        self.open_menu()
        self.click(self.PROFILE_LINK)

    def logout(self):
        self.wait_for_page_load()
        self.open_menu()
        self.wait_for_element(self.LOGOUT_LINK)
        self.click(self.LOGOUT_LINK)



