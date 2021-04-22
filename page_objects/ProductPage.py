from .BasePage import BasePage

URL = "http://localhost/index.php?route=product/product&path=57&product_id=49"


class ProductPage(BasePage):
    CURRENT_TITLE_ITEM = {'XPATH': '//div[@class="col-sm-4"]/h1'}
    TITLE_MAIN_PIC = {'XPATH': '//a[@class="thumbnail"]'}
    ADD_TO_CARD_BUTTON = {'id': 'button-cart'}
    ACTIVE_TAB_DESCRIPTION = {'id': 'tab-description'}
    INPUT_QUANTITY = {'XPATH': '//div[@class="form-group"]/input[1]'}
    HIDDEN = {'XPATH': '//div[@class="form-group"]/input[2]'}

    def open(self):
        self.driver.get(URL)

    def get_title_current_item(self):
        element = self._find_element(self.CURRENT_TITLE_ITEM)
        return element.text

    def get_title_main_pic(self):
        element = self._find_element(self.TITLE_MAIN_PIC)
        return element.get_attribute("title")

    def get_right_panel_title(self):
        element = self._find_element(self.CURRENT_TITLE_ITEM)
        return element.text

    def get_add_to_card_button_text(self):
        element = self._find_element(self.ADD_TO_CARD_BUTTON)
        return element.text

    def show_active_tab_description(self):
        element = self._find_element(self.ACTIVE_TAB_DESCRIPTION)
        return element.is_displayed()

    def get_name_attribute_input_quantity(self):
        element = self._find_element(self.INPUT_QUANTITY)
        return element.get_attribute('name')
