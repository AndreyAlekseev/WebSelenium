from .BasePage import BasePage

URL = "http://localhost/index.php?route=product/category&path=20"


class CatalogPage(BasePage):
    SORT_BY_BUTTON = {'XPATH': '//select[@id="input-sort"]/option[1]'}
    SHOW_BY_BUTTON = {'XPATH': '//select[@id="input-limit"]/option[1]'}
    SYMBOL_CURRENT_CURRENCY = {'css': '#top .btn-link strong'}
    BREAD_CRUMBS_HOME_LINK = {'XPATH': '//ul[@class="breadcrumb"]/li[1]/a'}
    CONTENT_TITLE = {'XPATH': '//div[@id="content"]/h2'}
    BREAD_CRUMBS_CURRENT_LINK = {'XPATH': '//ul[@class="breadcrumb"]/li[2]/a'}

    def open(self):
        self.driver.get(URL)

    def get_sort_by_value(self):
        element = self._find_element(self.SORT_BY_BUTTON)
        return element.text

    def get_show_by_count(self):
        element = self._find_element(self.SHOW_BY_BUTTON)
        return int(element.text)

    def get_symbol_currency(self):
        element = self._find_element(self.SYMBOL_CURRENT_CURRENCY)
        return element.text

    def get_home_link_breadcrumbs(self):
        element = self._find_element(self.BREAD_CRUMBS_HOME_LINK)
        return element.get_attribute("href")

    def get_content_title(self):
        element = self._find_element(self.CONTENT_TITLE)
        return element.text

    def get_current_breadcrumb_name(self):
        element = self._find_element(self.BREAD_CRUMBS_CURRENT_LINK)
        return element.text








