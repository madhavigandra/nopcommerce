import pytest
from selenium import webdriver
from py.xml import html

@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
        assert isinstance(driver, object)
    elif browser == 'firefox':
        driver = webdriver.Firefox("C:\Program Files\geckodriver.exe")
    else:
        webdriver.Ie("C:\Program Files\IEDriverServer.exe")
    return driver


def pytest_addoption(parser):  # this method get value from the command line interpreter/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return browser value tothe setup method
    return request.config.getoption("--browser")


####this is a hook for adding environment to the Python html report ###############
def pytest_configure(config):
    config._metadata['project Name'] = 'NOP commerce'
    config._metadata['Module name'] = 'Customers'
    config._metadata['tester'] = 'Maddie'

    ######### it is hook for delete/modify environmen info to HTML report
@pytest.mark.optionalhooks
def pytest_metadata(metadata):
        metadata.pop("JAVA_HOME", None)
        metadata.pop("plugins", None)
