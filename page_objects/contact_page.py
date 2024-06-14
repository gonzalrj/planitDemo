from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactPage(BasePage):
    __submit_btn = (By.XPATH, "//a[@class='btn-contact btn btn-primary']")
    __header_msg = (By.XPATH, "//div[contains(@class, 'alert')]")

    __forename_box = (By.ID, "forename")
    __forename_err_msg = (By.ID, "forename-err")

    __email_box = (By.ID, "email")
    __email_err_msg = (By.ID, "email-err")

    __message_box = (By.ID, "message")
    __message_box_err_msg = (By.ID, "message-err")

    __modal_popup = (By.XPATH, "//div[@class='modal-header']")

    def submit_form(self):
        super()._click(self.__submit_btn)

    @property
    def get_header_message(self) -> str:
        return super()._get_elem_txt(self.__header_msg)

    @property
    def get_error_messages(self):
        err_msgs = [super()._get_elem_txt(self.__header_msg),
                    super()._get_elem_txt(self.__forename_err_msg),
                    super()._get_elem_txt(self.__email_err_msg),
                    super()._get_elem_txt(self.__message_box_err_msg)
                    ]
        return err_msgs

    def input_in_field(self, field_name, input_txt):
        if field_name == "forename":
            super()._type(self.__forename_box, input_txt)
        elif field_name == "email":
            super()._type(self.__email_box, input_txt)
        elif field_name == "message":
            super()._type(self.__message_box, input_txt)
        else:
            raise TypeError("Invalid field name was provided.")

    def wait_until_modal_is_hidden(self):
        super()._wait_until_element_is_hidden(self.__modal_popup)
