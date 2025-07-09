from src.pageObjects.login_page import LoginPage
from src.pageObjects.appointment_page import AppointmentPage


def test_make_appointment(browser):
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")

    appointment = AppointmentPage(browser)
    appointment.make_appointment(
        facility="Hongkong CURA Healthcare Center",
        readmission=True,
        program="Medicaid",
        visit_date="01/01/2026",
        comment="This is a test appointment"
    )

    assert appointment.is_appointment_confirmed(), "Appointment was not confirmed successfully"
