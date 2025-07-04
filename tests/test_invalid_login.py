from src.pageObjects.login_page import LoginPage

def test_invalid_login(browser):
    login = LoginPage(browser)
    login.do_login("InvalidUser", "InvalidPaasword")

    error = login.get_error_message()
    assert "Login failed" in error