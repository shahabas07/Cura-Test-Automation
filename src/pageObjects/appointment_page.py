from selenium.webdriver.common.by import By
from src.base.base_page import BasePage

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

    def make_appointment(self, facility, readmission, program, visit_date, comment):
        self.select_dropdown(self.FACILITY_DROPDOWN, facility)
        if readmission:
            self.click(self.APPLY_CHECKBOX)

        if program.lower() == "medicaid":
            self.click(self.MEDICAID_RADIO)

        self.enter_text(self.VISIT_DATE_INPUT, visit_date)
        self.enter_text(self.COMMENT_TEXTAREA, comment)
        self.click(self.BOOK_BUTTON)

    def is_appointment_confirmed(self):
        return self.is_visible(self.CONFIRMATION_MESSAGE)

