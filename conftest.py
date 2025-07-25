import os
from pickle import GLOBAL

import pytest

from selenium import webdriver

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser name: chrome or firefox")
    #don't give spaces after = in action, default, help

@pytest.fixture()
def browserInstance(request):

    # browser setup
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--incognito")

    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--start-maximized")
    edge_options.add_argument("--ignore-certificate-errors")
    edge_options.add_argument("--incognito")

    browser_name = request.config.getoption("browser_name")   #get value from command line argument

    if browser_name == "chrome":
        driver = webdriver.Chrome(options=chrome_options)

    if browser_name == "edge":
        driver = webdriver.Edge(options=edge_options)

    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(4)
    yield driver
    driver.close()

'''
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__),'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("File name is "+file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


'''
