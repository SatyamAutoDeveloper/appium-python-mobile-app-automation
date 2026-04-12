import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

logger = logging.getLogger(__name__)


class MobileActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def find_element(self, locator):
        """Finds a single element with an explicit wait."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Finds multiple elements."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except Exception:
            return []

    def click_on_element(self, locator):
        """find element and clicks it."""
        logger.info(f"Attempting to click element with locator: {locator}")
        element = self.find_element(locator)
        element.click()

    def move_to_element_and_click(self, locator):
        """Moves to an element and clicks it."""
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        logger.info(f"Moved to element and clicked element with locator: {locator}")

    def tap_center(self, locator):
        logger.info(f"Performing tap on element at locator: {locator}")
        element = self.find_element(locator)
        location = element.location
        size = element.size
        # Calculate the dead center of the element
        x = location['x'] + (size['width'] / 2)
        y = location['y'] + (size['height'] / 2)

        actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.pointer_action.move_to_location(x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(0.1) # Small pause to simulate a real finger press
        actions.pointer_action.pointer_up()
        actions.perform()
        

    def click_with_retry(self, locator, target_locator, retries=3):
        """Attempts to click an element with retries in case of transient issues."""
        logger.info(f"Attempting to click element with locator: {locator} with up to {retries} retries")
        for attempt in range(retries):
            try:
                self.click_on_element(locator)
                if self.wait_for_element_present(target_locator):
                    logger.info(f"Successfully clicked element on attempt {attempt + 1}")
                    return # Click was successful and target element is present
                else:
                    logger.warning(f"Element clicked but target element not present after click attempt {attempt + 1}")
            except Exception as e:
                logger.warning(f"Click attempt {attempt + 1} failed for {locator}: {e}")
                if attempt == retries - 1:
                    raise

    def tap_center_with_retry(self, locator, retries=3):
        """Attempts to tap the center of an element with retries in case of transient issues."""
        logger.info(f"Attempting to tap center of element with locator: {locator} with up to {retries} retries")
        for attempt in range(retries):
            try:
                self.tap_center(locator)
                logger.info(f"Successfully Taped element on attempt {attempt + 1}")
                return
            except Exception as e:
                logger.warning(f"Tap attempt {attempt + 1} failed for {locator}: {e}")
                if attempt == retries - 1:
                    raise

    def click_with_replace_value(self, *locator, value):
        """Replaces a placeholder in the locator with a value and clicks the element."""
        if isinstance(*locator, tuple):
            by, loc = locator
            loc = loc.replace("{value}", value)
            new_locator = (by, loc)
            self.click_on_element(new_locator)
        else:
            raise ValueError("Locator must be a tuple of (By, locator_string)")

    def get_element_text(self, locator):
        """Gets the text of an element."""
        element = self.find_element(locator)
        return element.text
    
    def get_elements_texts(self, locator):
        """Gets the texts of multiple elements."""
        elements = self.find_elements(locator)
        return [element.text for element in elements]
    
    def get_elements_count(self, locator):
        """Gets the count of elements matching the locator."""
        elements = self.find_elements(locator)
        return len(elements)

    def is_element_displayed(self, locator):
        """Checks if an element is displayed."""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except Exception:
            return False

    def wait_for_element_visible(self, locator):
        """Waits until the element is visible."""
        logger.info(f"Waiting for element to be visible: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator):
        """Waits until the element is invisible."""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        """Waits until the element is clickable."""
        logger.info(f"Waiting for element to be clickable: {locator}")
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_present(self, locator):
        """Waits until the element is present in the DOM."""
        logger.info(f"Waiting for element to be present: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def implicit_wait(self, seconds):
        """Sets an implicit wait for the driver."""
        self.driver.implicitly_wait(seconds)

    def type_value(self, locator, value, clear_first=True):
        """Sends keys to an input field."""
        element = self.find_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(value)
        logger.info("Typed value into element: {} with locator: {}".format(value, locator))

    def move_to_element_and_type_value(self, locator, value, clear_first=True):
        """Moves to an element and sends keys to it."""
        element = self.find_element(locator)
        if clear_first:
            element.clear()
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys(value)
        actions.perform()
        logger.info("Moved to element and typed value: {} into element with locator: {}".format(value, locator))

    def scroll_element_into_view(self, locator):
        """Scrolls until the element is in view using mobile UIAutomator (Android focus)."""
        # Note: For iOS, you'd typically use 'mobile: scroll' script
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_element_clickable(self, locator):
        """Checks if an element is clickable."""
        try:
            element = self.find_element(locator)
            return element.is_enabled() and element.is_displayed()
        except Exception:
            return False
        
    def is_element_disabled(self, locator):
        """Checks if an element is disabled."""
        try:
            element = self.find_element(locator)
            return not element.is_enabled()
        except Exception:
            return False
        
    def is_element_selected(self, locator):
        """Checks if an element is selected"""
        try:
            element = self.find_element(locator)
            return element.is_selected()
        except Exception:
            return False

    def is_element_checked(self, locator):
        """Checks if a checkbox or radio button is checked."""
        try:
            element = self.find_element(locator)
            return element.get_attribute("checked") == "true"
        except Exception:
            return False
        
    def is_element_enabled(self, locator):
        """Checks if an element is enabled."""
        try:
            element = self.find_element(locator)
            return element.is_enabled() or element.get_attribute("enabled") == "true"
        except Exception:
            return False

