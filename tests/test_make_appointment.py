import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from src.pageObjects.login_page import LoginPage
from src.pageObjects.appointment_page import AppointmentPage

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_make_appointment(browser):
    try:
        # Login
        login = LoginPage(browser)
        login.do_login("John Doe", "ThisIsNotAPassword")

        # Create appointment
        appointment = AppointmentPage(browser)
        appointment.make_appointment(
            facility="Hongkong CURA Healthcare Center",
            readmission=True,
            program="Medicaid",
            visit_date="01/01/2026",
            comment="This is a test appointment"
        )

        # Verify appointment confirmation with explicit wait
        WebDriverWait(browser, 20).until(
            lambda d: appointment.is_appointment_confirmed()
        )
        
        # Additional verification
        confirmation_text = appointment.get_confirmation_text()
        assert "Appointment Confirmation" in confirmation_text, \
            "Appointment confirmation text not found"
            
    except TimeoutException as e:
        pytest.fail(f"Timeout occurred while waiting for appointment confirmation: {str(e)}")
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {str(e)}")