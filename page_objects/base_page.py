from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 5):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _wait_until_element_is_visible(self, locator, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_hidden(self, locator, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element_located(locator))

    def goto_page_new_session(self, url: str):
        self._driver.get(url)
        self._driver.delete_all_cookies()

    def goto_page_existing_session(self, url: str):
        self._driver.get(url)

    def _click(self, locator: tuple, time: int = 5):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _get_elem_txt(self, locator: tuple) -> str:
        self._wait_until_element_is_visible(locator)
        return self._find(locator).text

    def _hover(self, locator):
        actions = ActionChains(self._driver)
        actions.move_to_element(locator).perform()
