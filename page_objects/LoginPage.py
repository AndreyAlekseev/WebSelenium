from .BasePage import BasePage
from selenium.webdriver.common.by import By

URL = "http://localhost/index.php?route=account/login"


class LoginPage(BasePage):
    LOGIN_INPUT = {'id': 'input-email'}
    LOGIN_PASSWORD = {'id': 'input-password'}
    RIGHT_MENU_ROWS = (By.XPATH, '//div[@class="list-group"]/a')
    LEFT_BLOCK_DESCRIPTION = (By.XPATH, '//div[@class="well"]/p/strong')
    TOP_NAVBAR = {'id': 'menu'}

    def open(self):
        self.driver.get(URL)

    def get_placeholder_username(self):
        element = self._find_element(self.LOGIN_INPUT)
        return element.get_attribute("placeholder")

    def get_placeholder_password(self):
        element = self._find_element(self.LOGIN_PASSWORD)
        return element.get_attribute("placeholder")

    def get_count_rows_of_right_menu(self):
        count = self._find_elements(self.RIGHT_MENU_ROWS)
        return len(count)

    def get_subtitle_text_on_description(self):
        element = self._find_elements(self.LEFT_BLOCK_DESCRIPTION)
        return element[0].text

    def show_top_navbar(self):
        element = self._find_element(self.TOP_NAVBAR)
        return element.is_displayed()
