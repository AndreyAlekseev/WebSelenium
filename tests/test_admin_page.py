from page_objects import AdminPage
import pytest


@pytest.mark.nondestructive
def test_admin_page(browser, base_url):
    """"Checking to available web elements on product card."""
    admin_page = AdminPage(browser)
    admin_page.open()
    assert admin_page.get_logo_attribute("src") == f"{base_url}admin/view/image/logo.png"
    assert admin_page.get_title_login_form() == "Please enter your login details."
    assert admin_page.submit_button_is_active()
    assert admin_page.get_forgotten_password_button_text() == "Forgotten Password"
    assert admin_page.username_field_is_displayed()


@pytest.mark.nondestructive
def test_validation(browser, base_url):
    """Enter invalid data in input fields"""
    admin_page = AdminPage(browser)
    admin_page.open()
    admin_page.login_user(login="123", password="123")
    assert admin_page.error_message_is_displayed()


@pytest.mark.nondestructive
def test_enter_to_backoffice(browser):
    """Enter invalid data in input fields."""
    admin_page = AdminPage(browser)
    admin_page.open()
    admin_page.login_user(login="user", password="bitnami")
    assert admin_page.get_title_map() == "World Map"
