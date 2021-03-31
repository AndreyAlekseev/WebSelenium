import pytest
from selenium.webdriver.common.by import By


@pytest.mark.nondestructive
def test_catalog_page(browser, base_url):
    """"Checking web elements on catalog page"""
    url = "index.php?route=product/category&path=20"
    browser.get(f'{base_url}' + f'{url}')
    assert browser.find_element(By.ID, "input-sort").find_elements(By.TAG_NAME, "option")[0].text == "Default"
    assert int(browser.find_element(By.ID, "input-limit").find_elements(By.TAG_NAME, "option")[0].text) == 20
    assert browser.find_element(By.CSS_SELECTOR, "#top .btn-link strong").text == "$"
    assert browser.find_elements(
        By.CLASS_NAME, "breadcrumb")[0].find_element(
        By.TAG_NAME, "a").get_attribute("href") == f"{base_url}" + "index.php?route=common/home"
    assert browser.find_elements(
        By.CLASS_NAME, "breadcrumb")[-1].find_element(
        By.LINK_TEXT, "Desktops").text == browser.find_element(By.TAG_NAME, "h2").text
