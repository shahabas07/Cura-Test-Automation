from selenium.webdriver.common.by import By
from src.base.base_page import BasePage

class LoginPage(BasePage):
    Username_Input = (By.ID, "txt-username")
    Password_Input = (By.ID, "txt-password")
    Login_Button = (By.ID, "btn-login")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")

    def do_login(self, username, password):
        self.enter_text(self.Username_Input, username)
        self.enter_text(self.Password_Input, password)
        self.click(self.Login_Button)

    def get_error_message(self):
        ERROR_ALERT = (By.XPATH, "//p[@class='lead text-danger']")
        return self.get_text(ERROR_ALERT)
