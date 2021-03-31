import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "ie"], help="Select one browser")
    parser.addoption("--headless", action="store_true", help="Enable headless")
    parser.addoption("--url", action="store", default="http://localhost/", help="Enter base url")


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="function")
def browser(request, base_url):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        driver = webdriver.Chrome(options=options)
    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
            driver = webdriver.Firefox(options=options)
    if browser == "ie":
        options = webdriver.IeOptions()
        if headless:
            options.headless = True
            driver = webdriver.Ie(options=options)

    def fin():
        driver.quit()
    request.addfinalizer(fin)

    return driver
