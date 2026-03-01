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


def get_hotel_rooms_info(driver):
    """Gets the names and addresses of hotel rooms displayed in the hotel rooms menu."""
    MobileActions.wait_for_element_clickable(driver, hotel_rooms)
    MobileActions.click_on_element(driver, hotel_rooms)
    MobileActions.wait_for_element_visible(driver, hotel_rooms_list)
    total_hotel_rooms = MobileActions.get_elements_count(driver, hotel_rooms_list)
    hotel_names = MobileActions.get_elements_texts(driver, name_elem)
    hotel_addresses = MobileActions.get_elements_texts(driver, addresses_or_info_elem)
    return total_hotel_rooms, list(zip(hotel_names, hotel_addresses))


def get_restaurants_info(driver):
    """Gets the names and addresses of restaurants displayed in the restaurants menu."""
    MobileActions.wait_for_element_clickable(driver, restaurants)
    MobileActions.click_on_element(driver, restaurants)
    MobileActions.wait_for_element_visible(driver, restaurants_list)
    total_restaurants = MobileActions.get_elements_count(driver, restaurants_list)
    restaurant_names = MobileActions.get_elements_texts(driver, name_elem)
    restaurant_addresses = MobileActions.get_elements_texts(driver, addresses_or_info_elem)
    return total_restaurants, list(zip(restaurant_names, restaurant_addresses))


def get_famous_places_info(driver):
    """Gets the names and information of famous places displayed in the famous places menu."""
    MobileActions.wait_for_element_clickable(driver, famous_places)
    MobileActions.click_on_element(driver, famous_places)
    MobileActions.wait_for_element_visible(driver, name_elem)
    place_name = MobileActions.get_element_text(driver, name_elem)
    place_info = MobileActions.get_element_text(driver, addresses_or_info_elem)
    return [place_name, place_info]


def get_bus_station_info(driver):
    """Gets the name and information of the bus station displayed in the bus station menu."""
    MobileActions.wait_for_element_clickable(driver, bus_station)
    MobileActions.click_on_element(driver, bus_station)
    MobileActions.wait_for_element_visible(driver, name_elem)
    station_name = MobileActions.get_element_text(driver, name_elem)
    station_info = MobileActions.get_element_text(driver, addresses_or_info_elem)
    return [station_name, station_info]


def get_history_info(driver):
    """Gets the history information displayed in the history menu."""
    MobileActions.wait_for_element_clickable(driver, history)
    MobileActions.click_on_element(driver, history)
    MobileActions.wait_for_element_visible(driver, name_elem)
    city_name = MobileActions.get_element_text(driver, name_elem)
    history_info = MobileActions.get_element_text(driver, addresses_or_info_elem)
    return [city_name, history_info]