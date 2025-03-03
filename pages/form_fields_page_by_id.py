from selenium.webdriver.support.select import Select
from pages.base_page import BasePage


class FormFieldsPageByID(BasePage):
    """Page object for the form fields page."""

    # URL
    URL = "https://practice-automation.com/form-fields/"

    # Locators
    NAME_INPUT = ("id", "name-input")
    PASSWORD_INPUT = ("xpath", '//*[@id="feedbackForm"]/label[2]/input')
    EMAIL_INPUT = ("id", "email")
    MILK_CHECKBOX = ("id", "drink2")
    COFFEE_CHECKBOX = ("id", "drink3")
    YELLOW_RADIO = ("id", "color3")
    AUTOMATION_DROPDOWN = ("xpath", '//*[@id="automation"]')
    MESSAGE_FIELD = ("id", "message")
    SUBMIT_BUTTON = ("id", "submit-btn")
    AUTOMATION_TOOLS_LIST = (
        "css selector",
        "ul li",
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.navigate(self.URL)

    def enter_name(self, name):
        """Enter a name into the name field."""
        self.type_text(self.NAME_INPUT, name)
        return self

    def get_name_value(self):
        """Get the value of the name field."""
        return self.get_element_attribute(self.NAME_INPUT, "value")

    def enter_password(self, password):
        """Enter a password into the password field."""
        self.type_text(self.PASSWORD_INPUT, password)
        return self

    def get_password_value(self):
        """Get the value of the password field."""
        return self.get_element_attribute(self.PASSWORD_INPUT, "value")

    def select_milk_checkbox(self):
        """Select the milk checkbox."""
        self.click_element(self.MILK_CHECKBOX)
        return self

    def select_coffee_checkbox(self):
        """Select the coffee checkbox."""
        self.click_element(self.COFFEE_CHECKBOX)
        return self

    def is_checkbox_selected(self, locator):
        """Check if a checkbox is selected."""
        return self.get_element_attribute(locator, "checked") is not None

    def select_yellow_radio(self):
        """Select the yellow radio button."""
        self.click_element(self.YELLOW_RADIO)
        return self

    def is_radio_selected(self, locator):
        """Check if a radio button is selected."""
        return self.get_element_attribute(locator, "checked") is not None

    def enter_email(self, email):
        """Enter an email into the email field."""
        self.type_text(self.EMAIL_INPUT, email)
        return self

    def get_email_value(self):
        """Get the value of the email field."""
        return self.get_element_attribute(self.EMAIL_INPUT, "value")

    def select_automation_yes(self):
        """Select 'Yes' from the automation dropdown."""
        dropdown = Select(self.find_element(self.AUTOMATION_DROPDOWN))
        dropdown.select_by_value("yes")
        return self

    def get_selected_automation_value(self):
        """Get the selected value from the automation dropdown."""
        dropdown = Select(self.find_element(self.AUTOMATION_DROPDOWN))
        return dropdown.first_selected_option.get_attribute("value")

    def get_automation_tools(self):
        """Get the list of automation tools."""
        tools = self.find_elements(self.AUTOMATION_TOOLS_LIST)
        tools_list = []
        for item in tools:
            tool_text = item.text.replace("::marker", "").strip()
            if tool_text:
                tools_list.append(tool_text)
        return tools_list

    def enter_message(self, message):
        """Enter a message into the message field."""
        self.type_text(self.MESSAGE_FIELD, message)
        return self

    def get_message_value(self):
        """Get the value of the message field."""
        return self.get_element_attribute(self.MESSAGE_FIELD, "value")

    def submit_form(self):
        """Submit the form."""
        self.click_element(self.SUBMIT_BUTTON)
        return self

    def fill_form_with_tools(self, name, email):
        """Fill the form with name, email, and tools list."""
        tools_list = self.get_automation_tools()
        tools_string = ", ".join(tools_list)
        longest_tool = max(tools_list, key=len) if tools_list else ""
        message = f"{tools_string}\n{longest_tool}"

        self.enter_name(name)
        self.enter_email(email)
        self.enter_message(message)
        return self
