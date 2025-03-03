from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)

    def navigate(self, url):
        """Navigate to the specified URL."""
        self.driver.get(url)

    def find_element(self, locator):
        """Find an element on the page."""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Find multiple elements on the page."""
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        """Click an element."""
        element = self.find_element(locator)
        self.actions.move_to_element(element).click(element).perform()

    def type_text(self, locator, text):
        """Type text into an element."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_attribute(self, locator, attribute):
        """Get an attribute of an element."""
        return self.find_element(locator).get_attribute(attribute)

    def wait_for_element(self, locator, timeout=10):
        """Wait for an element to be visible."""
        return self.driver.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_alert(self):
        """Wait for an alert to be present."""
        return self.driver.wait.until(EC.alert_is_present())

    def get_alert_text(self):
        """Get the text from an alert."""
        alert = self.driver.switch_to.alert
        return alert.text

    def accept_alert(self):
        """Accept an alert."""
        alert = self.driver.switch_to.alert
        alert.accept()
