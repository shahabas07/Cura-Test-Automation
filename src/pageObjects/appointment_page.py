from selenium.webdriver.common.by import By
from src.base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppointmentPage(BasePage):
    FACILITY_DROPDOWN = (By.ID, "combo_facility")
    APPLY_CHECKBOX = (By.ID, "chk_hospotal_readmission")
    MEDICAID_RADIO = (By.ID, "radio_program_medicaid")
    VISIT_DATE_INPUT = (By.ID, "txt_visit_date")
    COMMENT_TEXTAREA = (By.ID, "txt_comment")
    BOOK_BUTTON = (By.ID, "btn-book-appointment")
    CONFIRMATION_MESSAGE = (By.XPATH, "//h2[contains(text(), 'Appointment Confirmation')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.timeout = 15
        WebDriverWait(driver, self.timeout).until(
            EC.presence_of_element_located((By.ID, "appointment"))
        )

    def make_appointment(self, facility, readmission, program, visit_date, comment):
        self.wait_for_page_load()
        
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(self.FACILITY_DROPDOWN)
            )
            self.select_dropdown(self.FACILITY_DROPDOWN, facility)
            
            if readmission:
                self.click(self.APPLY_CHECKBOX)

            if program.lower() == "medicaid":
                self.click(self.MEDICAID_RADIO)

            if visit_date:  # Only enter date if provided
                self.enter_text(self.VISIT_DATE_INPUT, visit_date)
                
            self.enter_text(self.COMMENT_TEXTAREA, comment)
            self.click(self.BOOK_BUTTON)
            self.wait_for_page_load()
            
        except Exception as e:
            self.driver.save_screenshot("appointment_error.png")
            raise

    def is_appointment_confirmed(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(self.CONFIRMATION_MESSAGE)
            )
        except:
            return False