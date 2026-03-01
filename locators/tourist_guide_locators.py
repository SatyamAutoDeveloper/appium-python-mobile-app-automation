from appium.webdriver.common.appiumby import AppiumBy

enter_city_search_box = (AppiumBy.ID, "com.dataflair.myapplication:id/editSearchbox")
valid_city_name = (AppiumBy.ID, "com.dataflair.myapplication:id/txtCityname")
no_city_present = (AppiumBy.ID, "com.dataflair.myapplication:id/recyclerview")
hotel_rooms = (AppiumBy.ID, "com.dataflair.myapplication:id/btnHotelrooms")
hotel_rooms_list = (AppiumBy.CLASS_NAME, "androidx.cardview.widget.CardView")
restaurants = (AppiumBy.ID, "com.dataflair.myapplication:id/btnRestaurant")
restaurants_list = (AppiumBy.CLASS_NAME, "androidx.cardview.widget.CardView")
famous_places = (AppiumBy.ID, "com.dataflair.myapplication:id/btnFamousplaces")
bus_station = (AppiumBy.ID, "com.dataflair.myapplication:id/btnBusstation")
history = (AppiumBy.ID, "com.dataflair.myapplication:id/btnHistory")
name_elem = (AppiumBy.ID, "com.dataflair.myapplication:id/titleTxtView")
addresses_or_info_elem = (AppiumBy.ID, "com.dataflair.myapplication:id/dataTxtView")