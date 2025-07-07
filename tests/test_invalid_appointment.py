from src.pageObjects.login_page import LoginPage
from src.pageObjects.appointment_page import AppointmentPage
from selenium.common.exceptions import TimeoutException

def test_appointment_missing_date(browser):
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")

    appointment = AppointmentPage(browser)
    appointment.make_appointment(
        facility="Tokyo CURA Healthcare Center",
        readmission=False,
        program="Medicaid",
        visit_date="",  # Intentionally blank
        comment="No visit date"
    )

    # This will try to find the confirmation page
    try:
        confirmed = appointment.is_appointment_confirmed()
        assert not confirmed, "Confirmation should not appear when visit date is missing."
    except TimeoutException:
        # Timeout means confirmation didn't appear = expected ✅
        assert True


def test_appointment_with_past_date(browser):
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")

    appointment = AppointmentPage(browser)
    appointment.make_appointment(
        facility="Tokyo CURA Healthcare Center",
        readmission=False,
        program="Medicaid",
        visit_date="01/01/2020",  # Past date
        comment="Testing with past date"
    )

    # Check if confirmation is wrongly shown
    try:
        confirmed = appointment.is_appointment_confirmed()
        assert not confirmed, "BUG: Appointment got confirmed with a past date."
    except TimeoutException:
        # This is expected if appointment is rejected properly
        assert True
