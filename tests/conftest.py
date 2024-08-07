import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture()
# This function runs test based on command-line provided browser option
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Creating {browser} driver.")

    # Create the browser instance based on the inputted --browser value from def pytest_addoption(parser)
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        my_driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        my_driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        my_driver = webdriver.Edge(options=options)
    elif browser == "safari":
        my_driver = webdriver.Safari()  # Safari does not support headless execution.
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' or 'edge' or 'safari' but got {browser} instead.")

    my_driver.set_window_position(0, 2000)
    my_driver.maximize_window()

    yield my_driver
    print(f"Closing {browser} driver.")
    my_driver.quit()


# @pytest.fixture(params=["chrome", "firefox", "edge"])
# # This function runs tests on all browsers provided in the params
# def driver(request):
#     browser = request.param
#     print(f"Creating {browser} driver.")
#
#     # Create the browser instance based on the inputted --browser value from def pytest_addoption(parser)
#     if browser == "chrome":
#         my_driver = webdriver.Chrome()
#     elif browser == "firefox":
#         my_driver = webdriver.Firefox()
#     elif browser == "edge":
#         my_driver = webdriver.Edge()
#     elif browser == "safari":
#         my_driver = webdriver.Safari()
#     else:
#         raise TypeError(f"Expected 'chrome' or 'firefox' or 'edge' or 'safari' but got {browser} instead.")
#
#     yield my_driver
#     print(f"Closing {browser} driver.")
#     my_driver.quit()


# This function allows user to input a browser as a command line parameter
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Input 'chrome', 'firefox', 'edge', 'safari'"
    )
