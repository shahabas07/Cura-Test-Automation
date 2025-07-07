from selenium.webdriver.common.by import By
from src.base.base_page import BasePage

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
        self.click(self.MENU_BUTTON)

    def go_to_history(self):
        self.open_menu()
        self.click(self.HISTORY_LINK)

    def go_to_home(self):
        self.open_menu()
        self.click(self.HOME_LINK)

    def go_to_profile(self):
        self.open_menu()
        self.click(self.PROFILE_LINK)

    def logout(self):
        self.open_menu()
        self.click(self.LOGOUT_LINK)
