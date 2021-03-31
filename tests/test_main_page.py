import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.nondestructive
def test_main_page(browser, base_url):
    """"Checking 5 elements on main page"""
    browser.get(base_url)
    time.sleep(1)
    assert browser.find_element(By.XPATH, "//div[@class='container']/p/a").text == "OpenCart"
    assert browser.find_element(By.ID, "cart").is_displayed()
    count_elements = browser.find_elements(By.XPATH, "//div[@class='row']//div[@class='product-thumb transition']")
    i = 0
    for f in count_elements:
        i = i+1
    assert i == 4
    assert browser.find_element(
        By.XPATH, "//li[@class='dropdown']/a[@title='My Account']").get_property('title') == "My Account"
    assert browser.find_element(By.ID, "logo").text == "Your Store"
