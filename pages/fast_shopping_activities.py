from helpers.native_app_operations import MobileActions
from locators.fast_shopping_locators import *
import logging

logger = logging.getLogger(__name__)

def verify_fast_shopping_page_title_and_logo_presence(driver):
    """Verifies that the fast shopping page title is present with logo."""
    MobileActions.wait_for_element_present(driver, app_name_with_logo)
    title_displayed = MobileActions.is_element_displayed(driver, app_name_with_logo)
    logger.info(f"Fast Shopping page title with logo displayed: {title_displayed}")
    return title_displayed


def verify_no_list_selected_message_displayed(driver):
    """Verifies that the 'No list selected' message is displayed when no shopping list is selected."""
    MobileActions.wait_for_element_present(driver, no_list_selected_list_elem)
    message_displayed = MobileActions.is_element_displayed(driver, no_list_selected_list_elem)
    logger.info(f"'No list selected' message displayed: {message_displayed}")
    return message_displayed


def verify_show_menu_button_displayed(driver):
    """Verifies that the 'Show menu' button is displayed on the fast shopping page."""
    MobileActions.wait_for_element_present(driver, show_menu_btn)
    button_displayed = MobileActions.is_element_displayed(driver, show_menu_btn)
    logger.info(f"'Show menu' button displayed: {button_displayed}")
    return button_displayed


def verify_presence_fast_shopping_menu_options(driver):
    """Verifies that the expected options are present in the fast shopping menu."""
    MobileActions.wait_for_element_present(driver, show_menu_btn)
    MobileActions.click_on_element(driver, show_menu_btn)
    MobileActions.implicit_wait(driver, 2) # Wait for menu to open
    archive_list_option_disabled = MobileActions.is_element_disabled(driver, archive_list_btn)
    logger.info(f"'Archive list' option disabled in menu: {archive_list_option_disabled}")
    settings_option_clickable = MobileActions.is_element_clickable(driver, settings_btn)
    logger.info(f"'Settings' option clickable in menu: {settings_option_clickable}")
    return archive_list_option_disabled, settings_option_clickable


def navigate_to_settings_from_fast_shopping_menu(driver):
    """Navigates to the settings page from the fast shopping menu."""
    MobileActions.wait_for_element_present(driver, show_menu_btn)
    MobileActions.click_on_element(driver, show_menu_btn)
    MobileActions.implicit_wait(driver, 2) # Wait for menu to open
    MobileActions.click_on_element(driver, settings_btn)
    MobileActions.implicit_wait(driver, 2) # Wait for settings page to load


def verify_default_behavior_of_multiple_shopping_lists_option(driver):
    """Verifies that the 'Multiple shopping lists' option is selected by default in settings."""
    multiple_lists_option_selected = MobileActions.is_element_checked(driver, multiple_shopping_lists_radio_btn)
    logger.info(f"'Multiple shopping lists' option selected by default: {multiple_lists_option_selected}")
    return multiple_lists_option_selected


def navigate_back_to_main_page(driver):
    """Navigates back to the main page from settings or any other subpage."""
    MobileActions.wait_for_element_present(driver, navigate_back_btn)
    MobileActions.click_on_element(driver, navigate_back_btn)
    MobileActions.implicit_wait(driver, 2) # Wait for navigation to complete


def navigate_to_shopping_lists_page_from_main_page(driver):
    """Navigates to the shopping lists page from the main page."""
    MobileActions.wait_for_element_present(driver, no_list_selected_list_elem)
    MobileActions.click_on_element(driver, no_list_selected_list_elem)
    MobileActions.implicit_wait(driver, 2) # Wait for shopping lists page to load


def verify_default_behavior_and_presence_of_shopping_lists_page_elements(driver):
    """Verifies the default behavior and presence of key elements on the shopping lists page."""
    MobileActions.wait_for_element_present(driver, shoppings_list_page_title)
    title_displayed = MobileActions.is_element_displayed(driver, shoppings_list_page_title)
    logger.info(f"Shopping lists page title displayed: {title_displayed}")
    
    no_current_list_message_displayed = MobileActions.is_element_displayed(driver, current_tab_no_current_list_msg)
    logger.info(f"'There are no current lists' message displayed: {no_current_list_message_displayed}")

    new_list_button_displayed = MobileActions.is_element_displayed(driver, current_tab_new_list_btn)
    logger.info(f"'NEW LIST' button displayed: {new_list_button_displayed}")
    
    # Verify that we are on the Current tab by default
    current_tab_selected = MobileActions.is_element_displayed(driver, current_tab)
    logger.info(f"Current tab is selected by default: {current_tab_selected}")

    # Verify that the Archived tab is clickable
    archived_tab_clickable = MobileActions.is_element_clickable(driver, archived_tab)
    logger.info(f"Archived tab is clickable: {archived_tab_clickable}")

    return title_displayed, no_current_list_message_displayed, new_list_button_displayed, current_tab_selected, archived_tab_clickable


def click_new_list_button(driver):
    """Clicks on the 'NEW LIST' button on the shopping lists page."""
    MobileActions.wait_for_element_present(driver, current_tab_new_list_btn)
    MobileActions.click_on_element(driver, current_tab_new_list_btn)
    MobileActions.implicit_wait(driver, 2) # Wait for new list popup to appear


def verify_presence_of_add_new_shopping_list_popup_elements(driver):
    """Verifies the presence of key elements in the 'Add new shopping list' popup."""
    MobileActions.wait_for_element_present(driver, new_list_popup_title)
    popup_title_displayed = MobileActions.is_element_displayed(driver, new_list_popup_title)
    logger.info(f"'Add new shopping list' popup title displayed: {popup_title_displayed}")

    cancel_button_displayed = MobileActions.is_element_displayed(driver, new_list_popup_cancel_btn)
    logger.info(f"'CANCEL' button in new list popup displayed: {cancel_button_displayed}")

    add_button_displayed = MobileActions.is_element_displayed(driver, new_list_popup_add_btn)
    logger.info(f"'ADD' button in new list popup displayed: {add_button_displayed}")

    input_field_displayed = MobileActions.is_element_displayed(driver, new_list_popup_input_field)
    logger.info(f"Input field in new list popup displayed: {input_field_displayed}")

    return popup_title_displayed, cancel_button_displayed, add_button_displayed, input_field_displayed