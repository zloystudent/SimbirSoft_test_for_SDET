import pytest
import allure
from pages.form_fields_page_by_css import FormFieldsPageByCSS
from enums_errors.global_errors import GlobalErrorMessages


@allure.epic("Web Forms Testing")
@allure.feature("CSS Form Fields")
class TestFormFieldsByCSS:
    @allure.story("Basic Form Fields")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test validating form fields using CSS selectors")
    def test_name_input(self, driver):
        """Test the name input field."""
        form_page = FormFieldsPageByCSS(driver)
        form_page.enter_name("meleaged")
        assert form_page.get_name_value() == "meleaged",GlobalErrorMessages.TEST_NAME_INPUT_ERROR.value

    def test_password_input(self, driver):
        """Test the password input field."""
        form_page = FormFieldsPageByCSS(driver)
        form_page.enter_password("meleaged")
        assert form_page.get_password_value() == "meleaged",GlobalErrorMessages.TEST_PASSWORD_INPUT_ERROR.value

    def test_checkbox_selection(self, driver):
        """Test checkbox selection for drinks."""
        form_page = FormFieldsPageByCSS(driver)
        form_page.select_milk_checkbox()
        assert form_page.is_checkbox_selected(form_page.MILK_CHECKBOX),GlobalErrorMessages.TEST_CHECKBOX_INPUT_ERROR.value

        form_page.select_coffee_checkbox()
        assert form_page.is_checkbox_selected(form_page.COFFEE_CHECKBOX),GlobalErrorMessages.TEST_CHECKBOX_INPUT_ERROR.value

    def test_radio_button_selection(self, driver):
        """Test radio button selection for color."""
        form_page = FormFieldsPageByCSS(driver)
        form_page.select_yellow_radio()
        assert form_page.is_radio_selected(form_page.YELLOW_RADIO), GlobalErrorMessages.TEST_RADIO_BUTTON_SELECTION_ERROR.value

    def test_email_input(self, driver):
        """Test the email input field."""
        form_page = FormFieldsPageByCSS(driver)
        form_page.enter_email("name@example.com")
        assert form_page.get_email_value() == "name@example.com", GlobalErrorMessages.TEST_EMAIL_INPUT_ERROR.value

    def test_automation_dropdown(self, driver):
        """Test the automation dropdown selection."""
        form_page = FormFieldsPageByCSS(driver)
        form_page.select_automation_yes()
        assert form_page.get_selected_automation_value() == "yes", GlobalErrorMessages.TEST_AUTOMATION_DPOPDOWN_ERROR.value

    def test_message_field(self, driver):
        """Test the message field input."""
        form_page = FormFieldsPageByCSS(driver)

        # Get automation tools
        tools_list = form_page.get_automation_tools()
        tools_string = ", ".join(tools_list)
        longest_tool = max(tools_list, key=len) if tools_list else ""

        # Create and enter message
        message = f"{tools_string}\n{longest_tool}"
        form_page.enter_message(message)

        # Verify the message
        entered_message = form_page.get_message_value()
        assert tools_string in entered_message, GlobalErrorMessages.TEST_MESSAGE_FIELD_ERROR.value
        assert longest_tool in entered_message,GlobalErrorMessages.TEST_MESSAGE_FIELD_ERROR.value

    def test_form_submission(self, driver):
        """Test the complete form submission process."""
        form_page = FormFieldsPageByCSS(driver)

        # Fill the form
        form_page.fill_form_with_tools("meleaged", "name@example.com")

        # Submit the form
        form_page.submit_form()

        # Check alert
        form_page.wait_for_alert()
        assert "Message received!" in form_page.get_alert_text(),GlobalErrorMessages.TEST_FORM_SUBMISSION_ERROR.value
        form_page.accept_alert()
