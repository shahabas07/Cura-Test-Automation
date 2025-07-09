import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from src.pageObjects.login_page import LoginPage
from src.pageObjects.appointment_page import AppointmentPage
from src.pageObjects.sidebar_menu_page import SidebarMenuPage
from src.pageObjects.history_page import HistoryPage


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_appointment_shows_in_history(browser):
    try:
        # Step 1: Login
        login = LoginPage(browser)
        login.do_login("John Doe", "ThisIsNotAPassword")

        # Step 2: Wait until the appointment page is loaded
        WebDriverWait(browser, 20).until(
            lambda d: "appointment" in d.current_url.lower() or
                      "make appointment" in d.page_source.lower()
        )

        # Step 3: Book the appointment
        appointment = AppointmentPage(browser)
        appointment.make_appointment(
            facility="Seoul CURA Healthcare Center",
            readmission=True,
            program="Medicare",
            visit_date="07/01/2025",
            comment="History check test"
        )

        # Step 4: Confirm appointment via explicit wait
        WebDriverWait(browser, 20).until(
            EC.text_to_be_present_in_element(
                AppointmentPage.CONFIRMATION_MESSAGE,
                "Appointment Confirmation"
            )
        )

        # Step 5: Navigate to History
        menu = SidebarMenuPage(browser)
        menu.go_to_history()

        # Step 6: Verify that the appointment is listed
        history = HistoryPage(browser)
        WebDriverWait(browser, 10).until(
            lambda d: history.is_appointment_listed()
        )

    except TimeoutException as e:
        pytest.fail(f"Timeout occurred: {str(e)}")
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {str(e)}")

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_logout_redirects_to_homepage(browser):
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")

    WebDriverWait(browser, 20).until(
        lambda d: "appointment" in d.current_url.lower() or
                  "make appointment" in d.page_source.lower()
    )

    menu = SidebarMenuPage(browser)
    menu.logout()

    assert "CURA Healthcare" in browser.title or "home" in browser.current_url.lower()
