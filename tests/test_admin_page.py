import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.nondestructive
def test_admin_page(browser, base_url):
    """"Checking to available web elements on product card"""
    url = "admin/"
    browser.get(f'{base_url}' + f'{url}')
    assert browser.find_element(
        By.XPATH, "//a[@class='navbar-brand']/img").get_attribute("src") == f"{base_url}admin/view/image/logo.png"
    assert browser.find_element(By.CLASS_NAME, "panel-title").text == "Please enter your login details."
    assert browser.find_element(By.XPATH, "//button").is_enabled()
    assert browser.find_element(By.XPATH, "//span[@class='help-block']").text == "Forgotten Password"
    assert browser.find_element(By.ID, "input-username").is_displayed()


@pytest.mark.nondestructive
def test_validation(browser, base_url):
    """Enter invalid data in input fields"""
    url = "admin/"
    browser.get(f'{base_url}' + f'{url}')
    time.sleep(1)
    browser.find_element(By.ID, "input-username").send_keys("123")
    browser.find_element(By.ID, "input-password").send_keys("123")
    browser.find_element(By.XPATH, "//button").submit()
    assert browser.find_element(By.XPATH, "//div[@class='panel-body']/div").is_displayed()


@pytest.mark.nondestructive
def test_enter_to_backoffice(browser, base_url):
    """Enter invalid data in input fields"""
    url = "admin/"
    browser.get(f'{base_url}' + f'{url}')
    time.sleep(1)
    browser.find_element(By.ID, "input-username").send_keys("user")
    browser.find_element(By.ID, "input-password").send_keys("bitnami")
    browser.find_element(By.XPATH, "//button").submit()
    assert browser.find_element(By.CLASS_NAME, "panel-title").text == "World Map"
    browser.find_element(By.ID, "menu-catalog").click()
    time.sleep(1)
    browser.find_elements(By.XPATH, "//ul[@id='collapse1']/li")[1].click()
    time.sleep(2)

