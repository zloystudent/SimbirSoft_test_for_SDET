from enum import Enum

class GlobalErrorMessages(Enum):
    TEST_NAME_INPUT_ERROR = "The entered name does not match the expected one"
    TEST_PASSWORD_INPUT_ERROR = "The entered password does not match the expected one."
    TEST_CHECKBOX_INPUT_ERROR = "Error when selecting the checkbox."
    TEST_RADIO_BUTTON_SELECTION_ERROR = "Error when selecting the radio button."
    TEST_EMAIL_INPUT_ERROR = "The entered EMAIL does not match the expected one."
    TEST_AUTOMATION_DPOPDOWN_ERROR = "Error when working with the drop-down menu."
    TEST_MESSAGE_FIELD_ERROR = "The entered message does not match the expected one."
    TEST_FORM_SUBMISSION_ERROR = "An error occurred when the form was being validated."
    