import pytest
import sys
from appium import webdriver
from appium.options.android import UiAutomator2Options
from helpers.native_app_operations import MobileActions
sys.dont_write_bytecode = True

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android_Emulator"
    options.app = "apps/tourist_guide_app.apk"
    options.automation_name = "UiAutomator2"
    options.package = "com.dataflair.myapplication"
    options.activity = ".MainActivity"
    options.set_capability("appium:disableWindowAnimation", True)
    options.set_capability("appium:adbExecTimeout", 60000)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver

    # Teardown: Quit the driver after the test
    try:
        driver.quit()
    except Exception as e:
        print(f"Error quitting driver: {e}")


@pytest.fixture(scope="function")
def NativeDriver(driver):
    return MobileActions(driver)