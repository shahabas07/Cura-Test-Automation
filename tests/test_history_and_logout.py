import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from src.pageObjects.login_page import LoginPage
from src.pageObjects.appointment_page import AppointmentPage
from src.pageObjects.sidebar_menu_page import SidebarMenuPage
from src.pageObjects.history_page import HistoryPage

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_appointment_shows_in_history(browser):
    try:
        # Login
        login = LoginPage(browser)
        login.do_login("John Doe", "ThisIsNotAPassword")

        # Wait for appointment page to load
        WebDriverWait(browser, 20).until(
            lambda d: "appointment" in d.current_url.lower() or
                      "make appointment" in d.page_source.lower()
        )

        # Create appointment
        appointment = AppointmentPage(browser)
        appointment.make_appointment(
            facility="Seoul CURA Healthcare Center",
            readmission=True,
            program="Medicare",
            visit_date="07/01/2025",
            comment="History check test"
        )

        # Verify appointment confirmation
        WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element(
                appointment.CONFIRMATION_SECTION, 
                "Appointment Confirmation"
            )
        )

        # Navigate to history
        menu = SidebarMenuPage(browser)
        menu.go_to_history()

        # Verify appointment in history
        history = HistoryPage(browser)
        WebDriverWait(browser, 20).until(
            lambda d: history.is_appointment_listed()
        )
        
    except TimeoutException as e:
        pytest.fail(f"Timeout occurred: {str(e)}")
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {str(e)}")

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_logout_redirects_to_homepage(browser):
    try:
        # Login
        login = LoginPage(browser)
        login.do_login("John Doe", "ThisIsNotAPassword")

        # Wait for appointment page
        WebDriverWait(browser, 20).until(
            lambda d: "appointment" in d.current_url.lower() or
                      "make appointment" in d.page_source.lower()
        )

        # Logout
        menu = SidebarMenuPage(browser)
        menu.logout()

        # Verify logout
        WebDriverWait(browser, 20).until(
            lambda d: "CURA Healthcare" in d.title or "home" in d.current_url.lower()
        )
        
    except TimeoutException as e:
        pytest.fail(f"Timeout occurred: {str(e)}")
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {str(e)}")