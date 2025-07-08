import pytest
from src.pageObjects.login_page import LoginPage
from src.pageObjects.appointment_page import AppointmentPage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_appointment_missing_date(browser):
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")
    
    WebDriverWait(browser, 15).until(
        EC.url_contains("appointment")
    )

    appointment = AppointmentPage(browser)
    appointment.make_appointment(
        facility="Tokyo CURA Healthcare Center",
        readmission=False,
        program="Medicaid",
        visit_date="",  # Intentionally blank
        comment="No visit date"
    )

    try:
        confirmed = appointment.is_appointment_confirmed()
        assert not confirmed, "Confirmation should not appear when visit date is missing."
    except TimeoutException:
        assert True

@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_appointment_with_past_date(browser):
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")
    
    WebDriverWait(browser, 15).until(
        EC.url_contains("appointment")
    )

    appointment = AppointmentPage(browser)
    appointment.make_appointment(
        facility="Tokyo CURA Healthcare Center",
        readmission=False,
        program="Medicaid",
        visit_date="01/01/2020",  # Past date
        comment="Testing with past date"
    )

    try:
        confirmed = appointment.is_appointment_confirmed()
        assert not confirmed, "BUG: Appointment got confirmed with a past date."
    except TimeoutException:
        assert True