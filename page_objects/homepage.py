from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class Homepage(BasePage):
    __nav_btn = (By.CLASS_NAME, "btn btn-navbar")
    __contact_link = (By.XPATH, "//a[@href='#/contact']")

    def goto_contact_page(self):
        super()._click(self.__contact_link)
