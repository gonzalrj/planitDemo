import pytest

from page_objects.contact_page import ContactPage
from page_objects.homepage import Homepage


class TestSendingFeedback:

    @pytest.mark.planit
    def test_error_messages(self, driver, base_url, forename_text="Archie", email_text="test@mail.com",
                            message_text="Hope you hire me."):
        """
        Test Case 1: Validate mandatory fields
        1. From the home page go to contact page
        2. Click submit button
        3. Verify error messages
        4. Populate mandatory fields
        5. Validate errors are gone
        """

        homepage = Homepage(driver)
        homepage.goto_page_new_session(base_url)
        homepage.goto_contact_page()

        contact_page = ContactPage(driver)
        contact_page.submit_form()
        assert "but we won't get it unless you complete the form correctly." in contact_page.get_header_message, \
            "Error message is expected."
        assert not len(contact_page.get_error_messages) == 0, "Error messages are expected."

        contact_page.input_in_field("forename", forename_text)
        contact_page.input_in_field("email", email_text)
        contact_page.input_in_field("message", message_text)

        contact_page.submit_form()
        contact_page.wait_until_modal_is_hidden()
        assert "we appreciate your feedback." in contact_page.get_header_message, ("Success message is expected but "
                                                                                   "error was returned.")

    @pytest.mark.planit
    @pytest.mark.parametrize("forename_text,email_text,message_text",
                             [("Henry", "henry@mail.com", "I feel gratitude."),
                              ("Ava", "ava@mail.com", "I am thankful"),
                              ("Amelia", "amelia@mail.com", "I am blessed"),
                              ("Ivy", "ivy@mail.com", "I am happy."),
                              ("Sophia", "sophia@mail.com", "I fear no one.")])
    def test_different_mandatory_values(self, driver, forename_text, email_text, message_text, base_url):
        """
        Test Case 2: Input different correct values to mandatory fields.
        1. From the home page go to contact page
        2. Populate mandatory fields
        3. Click submit button
        4. Validate successful submission message
        ** Note: Run this test 5 times to ensure 100% pass rate
        """

        homepage = Homepage(driver)
        homepage.goto_page_new_session(base_url)
        homepage.goto_contact_page()

        contact_page = ContactPage(driver)
        contact_page.input_in_field("forename", forename_text)
        contact_page.input_in_field("email", email_text)
        contact_page.input_in_field("message", message_text)

        contact_page.submit_form()
        contact_page.wait_until_modal_is_hidden()
        assert "we appreciate your feedback." in contact_page.get_header_message, ("Success message is expected but "
                                                                                   "error was returned.")
