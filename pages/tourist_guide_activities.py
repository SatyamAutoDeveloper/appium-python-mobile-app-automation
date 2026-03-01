from helpers.native_app_operations import MobileActions
from locators.tourist_guide_locators import *
import logging

logger = logging.getLogger(__name__)

def search_with_valid_city(driver, city_name):
    """Searches for a valid city name and verifies that it is displayed in the search results."""
    MobileActions.type_value(driver, enter_city_search_box, city_name)
    is_city_displayed = MobileActions.is_element_displayed(driver, valid_city_name)
    return is_city_displayed


def search_with_invalid_city(driver, city_name):
    """Searches for an invalid city name and verifies that no results are displayed."""
    MobileActions.type_value(driver, enter_city_search_box, city_name)
    is_no_city_present = MobileActions.is_element_displayed(driver, no_city_present)
    return is_no_city_present


def navigate_to_city_menu(driver, city_name):
    """Navigates to the city menu after searching for a valid city name."""
    MobileActions.type_value(driver, enter_city_search_box, city_name)
    MobileActions.wait_for_element_clickable(driver, valid_city_name)
    MobileActions.click_with_retry(driver, valid_city_name, hotel_rooms)