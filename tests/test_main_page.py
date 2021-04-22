from page_objects import MainPage
import pytest


@pytest.mark.nondestructive
def test_main_page(browser, base_url):
    """"Checking 5 elements on main page."""
    main_page = MainPage(browser)
    main_page.open()
    assert main_page.get_link_text_on_label() == "OpenCart"
    assert main_page.show_cart_button()
    assert main_page.count_display_featured_elements() == 4
    assert main_page.get_title_account_dropdown() == "My Account"
    assert main_page.get_text_logo() == "Your Store"
