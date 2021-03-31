import pytest
from selenium.webdriver.common.by import By


@pytest.mark.nondestructive
def test_product_page(browser, base_url):
    """"Checking to available web elements on product card"""
    url = "index.php?route=product/product&path=57&product_id=49"
    browser.get(f'{base_url}' + f'{url}')
    item_title = "Samsung Galaxy Tab 10.1"
    assert browser.find_elements(By.XPATH, "//a[@class='thumbnail']")[0].get_attribute("title") == item_title
    assert browser.find_element(By.XPATH, "//div[@class='col-sm-4']/h1").text == item_title
    assert browser.find_element(By.ID, "button-cart").text == "Add to Cart"
    assert browser.find_element(By.ID, "tab-description").is_displayed()
    assert browser.find_element(
        By.XPATH, "//div[@class='form-group']/input[@class='form-control']").get_attribute("name") == "quantity"
