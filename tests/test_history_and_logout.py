import pytest
from src.pageObjects.login_page import LoginPage
from src.pageObjects.appointment_page import AppointmentPage
from src.pageObjects.sidebar_menu_page import SidebarMenuPage
from src.pageObjects.history_page import HistoryPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_appointment_shows_in_history(browser):
    # Take screenshot before starting
    browser.save_screenshot("test_start.png")
    
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")
    
    # Wait for appointment page with multiple conditions
    WebDriverWait(browser, 20).until(
        lambda d: "appointment" in d.current_url.lower() or 
                 "make appointment" in d.page_source.lower()
    )
    browser.save_screenshot("after_login.png")

    # Book appointment
    appointment = AppointmentPage(browser)
    appointment.make_appointment(
        facility="Seoul CURA Healthcare Center",
        readmission=True,
        program="Medicare",
        visit_date="07/01/2025",
        comment="History check test"
    )
    browser.save_screenshot("after_appointment.png")

    # Navigate to History with retries
    menu = SidebarMenuPage(browser)
    menu.go_to_history()
    browser.save_screenshot("history_page.png")

    history = HistoryPage(browser)
    assert history.is_appointment_listed(), "Appointment not listed in history!"

@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_logout_redirects_to_homepage(browser):
    browser.save_screenshot("logout_test_start.png")
    
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")
    
    WebDriverWait(browser, 20).until(
        lambda d: "appointment" in d.current_url.lower()
    )
    browser.save_screenshot("before_logout.png")

    menu = SidebarMenuPage(browser)
    menu.logout()
    browser.save_screenshot("after_logout.png")

    assert "CURA Healthcare" in browser.title or "home" in browser.current_url.lower()