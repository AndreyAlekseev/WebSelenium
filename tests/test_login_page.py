import pytest
from selenium.webdriver.common.by import By


@pytest.mark.nondestructive
def test_login_page(browser, base_url):
    """"Checking to available web elements on product card"""
    url = "index.php?route=account/login"
    browser.get(f'{base_url}' + f'{url}')
    assert browser.find_element(By.ID, "input-email").get_attribute("placeholder") == "E-Mail Address"
    assert browser.find_element(By.ID, "input-password").get_attribute("placeholder") == "Password"
    list_group = browser.find_elements(By.CLASS_NAME, "list-group-item")
    i = 0
    for f in list_group:
        i = i + 1
    assert i == 13
    assert browser.find_elements(
        By.CLASS_NAME, "well")[0].find_elements(By.TAG_NAME, "p")[0].text == "Register Account"
    assert browser.find_element(By.ID, "menu").is_displayed()
