import pytest
import logging
from pages.tourist_guide_activities import (
    search_with_valid_city,
    search_with_invalid_city,
    navigate_to_city_menu
)

from locators.tourist_guide_locators import (
    hotel_rooms,
    restaurants,
    famous_places,
    bus_station,
    history
)

logger = logging.getLogger(__name__)

@pytest.mark.high
def test_search_with_valid_city(NativeDriver):
    """Test case to verify that searching with a valid city name displays the correct results."""
    city_name = "vijayawada"
    is_city_displayed = search_with_valid_city(NativeDriver, city_name)
    logger.info(f"Search for city '{city_name}' displayed: {is_city_displayed}")
    assert is_city_displayed, f"Expected city name '{city_name}' to be displayed, but it was not."


@pytest.mark.medium
def test_search_with_invalid_city(NativeDriver):
    """Test case to verify that searching with an invalid city name does not display any results."""
    city_name = "invalidcity"
    is_no_city_present = search_with_invalid_city(NativeDriver, city_name)
    logger.info(f"Search for invalid city '{city_name}' displayed no results: {is_no_city_present}")
    assert is_no_city_present, f"Expected no results for city name '{city_name}', but some results were displayed."


@pytest.mark.high
def test_navigate_to_city_menu_and_validate_menu_options(NativeDriver):
    """Test case to verify that navigating to a city menu displays the correct menu items."""
    city_name = "vijayawada"
    navigate_to_city_menu(NativeDriver, city_name)
    
    menu_items = {
        "Hotel Rooms": hotel_rooms,
        "Restaurants": restaurants,
        "Famous Places": famous_places,
        "Bus Station": bus_station,
        "History": history
    }
    
    for item_name, item_locator in menu_items.items():
        NativeDriver.wait_for_element_visible(item_locator)
        is_displayed = NativeDriver.is_element_displayed(item_locator)
        logger.info(f"{item_name} displayed: {is_displayed}")
        assert is_displayed, f"Expected '{item_name}' menu option to be displayed, but it was not."