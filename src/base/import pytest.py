import pytest
from unittest.mock import MagicMock, patch
from src.base.base_page import BasePage

# src/base/test_base_page.py


@pytest.fixture
def mock_driver():
    return MagicMock()

@pytest.fixture
def base_page(mock_driver):
    return BasePage(mock_driver)

@patch("src.base.base_page.WebDriverWait")
@patch("src.base.base_page.EC")
def test_click_calls_element_to_be_clickable_and_click(mock_ec, mock_wait, base_page, mock_driver):
    mock_element = MagicMock()
    mock_wait.return_value.until.return_value = mock_element
    locator = ("id", "someid")
    base_page.click(locator)
    mock_wait.assert_called_with(mock_driver, base_page.timeout)
    mock_ec.element_to_be_clickable.assert_called_with(locator)
    mock_element.click.assert_called_once()

@patch("src.base.base_page.WebDriverWait")
@patch("src.base.base_page.EC")
def test_enter_text_calls_visibility_and_send_keys(mock_ec, mock_wait, base_page, mock_driver):
    mock_element = MagicMock()
    mock_wait.return_value.until.return_value = mock_element
    locator = ("id", "input")
    base_page.enter_text(locator, "hello")
    mock_ec.visibility_of_element_located.assert_called_with(locator)
    mock_element.send_keys.assert_called_with("hello")

@patch("src.base.base_page.WebDriverWait")
@patch("src.base.base_page.EC")
def test_get_text_returns_element_text(mock_ec, mock_wait, base_page, mock_driver):
    mock_element = MagicMock()
    mock_element.text = "sample"
    mock_wait.return_value.until.return_value = mock_element
    locator = ("id", "label")
    result = base_page.get_text(locator)
    assert result == "sample"
    mock_ec.visibility_of_element_located.assert_called_with(locator)

@patch("src.base.base_page.WebDriverWait")
@patch("src.base.base_page.EC")
def test_is_visible_returns_true_if_element_found(mock_ec, mock_wait, base_page, mock_driver):
    mock_element = MagicMock()
    mock_wait.return_value.until.return_value = mock_element
    locator = ("id", "visible")
    assert base_page.is_visible(locator) is True

@patch("src.base.base_page.WebDriverWait")
@patch("src.base.base_page.EC")
def test_wait_for_element_returns_element(mock_ec, mock_wait, base_page, mock_driver):
    mock_element = MagicMock()
    mock_wait.return_value.until.return_value = mock_element
    locator = ("id", "wait")
    result = base_page.wait_for_element(locator)
    assert result == mock_element

@patch("src.base.base_page.Select")
def test_select_dropdown_selects_by_visible_text(mock_select, base_page, mock_driver):
    mock_element = MagicMock()
    mock_driver.find_element.return_value = mock_element
    mock_dropdown = MagicMock()
    mock_select.return_value = mock_dropdown
    locator = ("id", "dropdown")
    base_page.select_dropdown(locator, "Option 1")
    mock_driver.find_element.assert_called_with(*locator)
    mock_select.assert_called_with(mock_element)
    mock_dropdown.select_by_visible_text.assert_called_with("Option 1")

@patch("src.base.base_page.WebDriverWait")
def test_wait_for_page_load_waits_for_document_ready(mock_wait, base_page, mock_driver):
    base_page.wait_for_page_load()
    args, kwargs = mock_wait.return_value.until.call_args
    # The lambda should be called with driver
    assert callable(args[0])