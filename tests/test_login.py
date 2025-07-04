import pytest
from src.pageObjects.login_page import LoginPage

def test_valid_login(browser):
    login = LoginPage(browser)
    login.do_login("John Doe", "ThisIsNotAPassword")

    assert "appointment" in browser.current_url or "Make Appointment" in browser.page_source, "Login failed or incorrect page loaded"