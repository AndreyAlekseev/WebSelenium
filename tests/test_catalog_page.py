from page_objects import CatalogPage
import pytest


@pytest.mark.nondestructive
def test_catalog_page(browser, base_url):
    """"Checking web elements on catalog page"""
    catalog_page = CatalogPage(browser)
    catalog_page.open()
    assert catalog_page.get_sort_by_value() == "Default"
    assert catalog_page.get_show_by_count() == 20
    assert catalog_page.get_symbol_currency() == "$"
    assert catalog_page.get_home_link_breadcrumbs() == f"{base_url}" + "index.php?route=common/home"
    assert catalog_page.get_current_breadcrumb_name() == catalog_page.get_content_title()