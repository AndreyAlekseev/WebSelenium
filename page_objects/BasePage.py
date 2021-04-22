from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def __element(self, selector: dict, index: int, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'id' in selector.keys():
            by = By.ID
            selector = selector['id']
        elif 'XPATH' in selector.keys():
            by = By.XPATH
            selector = selector['XPATH']
        elif 'class' in selector.keys():
            by = By.CLASS_NAME
            selector = selector['class']
        elif 'tag' in selector.keys():
            by = By.TAG_NAME
            selector = selector['tag']
        return self.driver.find_elements(by, selector)[index]

    def _find_element(self, selector, index=0):
        element = self.__element(selector, index)
        return element

    def _find_elements(self, selector):
        return WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            method=EC.visibility_of_all_elements_located(selector),
            message=f"Can't find elements by locator {selector}"
        )

    def _click(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _get_element_text(self, selector, index=0):
        element = self.__element(selector, index).text
        return element
