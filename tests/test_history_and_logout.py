import pytest
from selenium.webdriver.support.ui import WebDriverWait

from src.pageObjects.login_page import LoginPage
from src.pageObjects.appointment_page import AppointmentPage
from src.pageObjects.sidebar_menu_page import SidebarMenuPage
from src.pageObjects.history_page import HistoryPage


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_appointment_shows_in_history(browser):
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")

    WebDriverWait(browser, 20).until(
        lambda d: "appointment" in d.current_url.lower() or
                  "make appointment" in d.page_source.lower()
    )

    appointment = AppointmentPage(browser)
    appointment.make_appointment(
        facility="Seoul CURA Healthcare Center",
        readmission=True,
        program="Medicare",
        visit_date="07/01/2025",
        comment="History check test"
    )

    menu = SidebarMenuPage(browser)
    menu.go_to_history()

    history = HistoryPage(browser)
    assert history.is_appointment_listed(), "Appointment not listed in history!"


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
