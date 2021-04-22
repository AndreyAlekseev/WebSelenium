from .BasePage import BasePage
from selenium.webdriver.common.by import By

URL = "http://localhost/"


class MainPage(BasePage):
    LINK_IN_FOOTER_ON_LABEL = {'XPATH': '//div[@class="container"]/p/a'}
    CART_BUTTON = {'id': 'cart'}
    ELEMENT_ON_FEATURE_ROW = (By.XPATH, "//div[@class='product-thumb transition']")
    ACCOUNT_DROPDOWN_BUTTON = {'XPATH': '//li[@class="dropdown"]/a[@title="My Account"]'}
    LOGO = {'id': 'logo'}

    def open(self):
        self.driver.get(URL)

    def get_link_text_on_label(self):
        element = self._find_element(self.LINK_IN_FOOTER_ON_LABEL)
        return element.text

    def show_cart_button(self):
        element = self._find_element(self.CART_BUTTON)
        return element.is_displayed()

    def count_display_featured_elements(self):
        count = self._find_elements(self.ELEMENT_ON_FEATURE_ROW)
        return len(count)

    def get_title_account_dropdown(self):
        element = self._find_element(self.ACCOUNT_DROPDOWN_BUTTON)
        return element.get_attribute("title")

    def get_text_logo(self):
        element = self._find_element(self.LOGO)
        return element.text
