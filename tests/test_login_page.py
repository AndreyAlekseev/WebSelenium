from page_objects import LoginPage
import pytest


@pytest.mark.nondestructive
def test_login_page(browser, base_url):
    """"Checking to available web elements on product card."""
    login_page = LoginPage(browser)
    login_page.open()
    assert login_page.get_placeholder_username() == "E-Mail Address"
    assert login_page.get_placeholder_password() == "Password"
    assert login_page.get_count_rows_of_right_menu() == 13
    assert login_page.get_subtitle_text_on_description() == "Register Account"
    assert login_page.show_top_navbar()
