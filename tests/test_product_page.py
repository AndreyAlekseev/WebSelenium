from page_objects import ProductPage
import pytest


@pytest.mark.nondestructive
def test_product_page(browser, base_url):
    """"Checking to available web elements on product card."""
    product_page = ProductPage(browser)
    product_page.open()
    item_title = product_page.get_title_current_item()
    assert product_page.get_title_main_pic() == item_title
    assert product_page.get_right_panel_title() == item_title
    assert product_page.get_add_to_card_button_text() == "Add to Cart"
    assert product_page.show_active_tab_description()
    assert product_page.get_name_attribute_input_quantity() == "quantity"
