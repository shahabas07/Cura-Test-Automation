import pytest
from src.pageObjects.login_page import LoginPage
from src.pageObjects.appointment_page import AppointmentPage
from src.pageObjects.sidebar_menu_page import SidebarMenuPage
from src.pageObjects.history_page import HistoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_appointment_shows_in_history(browser):
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")
    
    # Wait for appointment page to load
    WebDriverWait(browser, 15).until(
        EC.url_contains("appointment")
    )

    # Book an appointment
    appointment = AppointmentPage(browser)
    appointment.make_appointment(
        facility="Seoul CURA Healthcare Center",
        readmission=True,
        program="Medicare",
        visit_date="07/01/2025",
        comment="History check test"
    )

    # Navigate to History
    menu = SidebarMenuPage(browser)
    menu.go_to_history()

    history = HistoryPage(browser)
    assert history.is_appointment_listed(), "Appointment not listed in history!"

@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_logout_redirects_to_homepage(browser):
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")
    
    WebDriverWait(browser, 15).until(
        EC.url_contains("appointment")
    )

    menu = SidebarMenuPage(browser)
    menu.logout()

    assert "CURA Healthcare" in browser.title or "home" in browser.current_url.lower()