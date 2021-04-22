from .BasePage import BasePage

URL = "http://localhost/admin/"


class AdminPage(BasePage):
    INPUT_USERNAME = {'id': 'input-username'}
    INPUT_PASSWORD = {'id': 'input-password'}
    SUBMIT_BUTTON = {'XPATH': '//button'}
    MAP_TITLE = {'class': 'panel-title'}
    LOGO_ON_START_PAGE = {'css': '.navbar-brand > img'}
    PANEL_TITLE = {'class': 'panel-title'}
    FORGOTTEN_PASSWORD_BUTTON = {'XPATH': "//span[@class='help-block']"}
    ERROR_MESSAGE = {'XPATH': "//div[@class='panel-body']/div"}

    def open(self):
        self.driver.get(URL)

    def login_user(self, login, password):
        self._input(self.INPUT_USERNAME, login)
        self._input(self.INPUT_PASSWORD, password)
        self._click(self.SUBMIT_BUTTON)

    def get_title_map(self):
        element = self._get_element_text(self.MAP_TITLE)
        return element

    def get_logo_attribute(self, value):
        element = self._find_element(self.LOGO_ON_START_PAGE)
        return element.get_attribute(value)

    def get_title_login_form(self):
        element = self._get_element_text(self.PANEL_TITLE)
        return element

    def submit_button_is_active(self):
        element = self._find_element(self.SUBMIT_BUTTON)
        return element.is_enabled()

    def get_forgotten_password_button_text(self):
        element = self._get_element_text(self.FORGOTTEN_PASSWORD_BUTTON)
        return element

    def username_field_is_displayed(self):
        element = self._find_element(self.INPUT_USERNAME)
        return element.is_displayed()

    def error_message_is_displayed(self):
        element = self._find_element(self.ERROR_MESSAGE)
        return element.is_displayed()

