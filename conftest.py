import pytest
import sys
import pathlib
import logging
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from helpers.native_app_operations import MobileActions

sys.dont_write_bytecode = True

# 1. Configuration for Multiple Apps
APP_CONFIGS = {
    "tourist_app": {
        "app": "apps/tourist_guide_app.apk",
        "package": "com.dataflair.myapplication",
        "activity": ".MainActivity"
    },
    "fastshopping_app": {
        "app": "apps/fastshopping.apk",
        "package": "me.wolszon.fastshopping",
        "activity": ".MainActivity"
    }
}


def pytest_addoption(parser):
    """Add a command line option to select the app."""
    parser.addoption("--app_name", action="store", default="tourist_app", help="Key for the app configuration defined in APP_CONFIGS")


@pytest.fixture(scope="function")
def driver(request):
    # Get the app key from CLI or use default
    app_key = request.config.getoption("--app_name")
    config = APP_CONFIGS.get(app_key)

    if not config:
        pytest.exit(f"App configuration for '{app_key}' not found in APP_CONFIGS.")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android_Emulator"
    options.automation_name = "UiAutomator2"

    # Dynamic capabilities based on selected app
    options.app = str(pathlib.Path(config["app"]).absolute())
    options.app_package = config["package"]
    options.app_activity = config["activity"]

    options.set_capability("appium:disableWindowAnimation", True)
    options.set_capability("appium:adbExecTimeout", 90000)

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


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    """
    Pytest hook to attach the report object (rep_call, rep_setup, etc.) to the test item.
    This allows fixtures to inspect the test result, specifically for failure detection.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    # Check if the test failed during the 'call' phase (the actual test execution)
    if report.when == 'call' and report.failed:
        # Access the driver instance from the test function's arguments
        try:
            driver = item.funcargs['driver']
            # 2. Get the screenshot as Base64 encoded PNG
            screenshot_base64 = driver.get_screenshot_as_base64()
            if isinstance(screenshot_base64, bytes):
                screenshot_base64 = screenshot_base64.decode('utf-8')
            # 3. Embed the Base64 image into the HTML report
            # The extras.png method handles embedding a base64 encoded image string
            extra.append(pytest_html.extras.png(screenshot_base64, name="Failure Screenshot"))
            
            # 4. Update the report's extra list
            report.extra = extra

            print("\nScreenshot successfully embedded in HTML report.")
        except KeyError:
            # Handle cases where the 'driver' fixture isn't used
            print("\nWebDriver fixture 'driver' not found for screenshot.")
            return
        except Exception as e:
            print(f"\nFailed to capture screenshot: {e}")
            return

        # Create a unique filename with the test name and a timestamp
        test_name = item.name.replace('/', '_').replace(':', '_') # Clean up name for filename
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_dir = pathlib.Path("screenshots")
        screenshot_dir.mkdir(exist_ok=True) # Create 'screenshots' directory if it doesn't exist
        
        screenshot_filename = str(screenshot_dir / f"FAIL_{test_name}_{timestamp}.png")
        
        # Take the screenshot
        try:
            driver.save_screenshot(screenshot_filename)
            print(f"\nScreenshot saved: {screenshot_filename}")
        except Exception as e:
            print(f"\nFailed to take screenshot: {e}")


@pytest.fixture(scope="function", autouse=True)
def capture_test_level_logs(request):
    """
    Fixture to set up a function-scoped log file for each test case.
    The log file is named after the test function and placed in a 'logs' directory.
    """
    # 1. Define Log File Path
    log_dir = pathlib.Path("logs")
    log_dir.mkdir(exist_ok=True)  # Create logs directory if it doesn't exist

    # Get the test name (e.g., test_login_success)
    test_name = request.node.name
    log_file_path = log_dir / f"{test_name}.log"

    # 2. Configure Logger
    # Get the root logger
    logger = logging.getLogger() 
    logger.setLevel(logging.INFO) # Set the minimum logging level (e.g., INFO, DEBUG)

    # Remove any existing custom handlers (to prevent duplicate logging or inherited handlers)
    for handler in logger.handlers[:]:
        if isinstance(handler, logging.FileHandler):
            logger.removeHandler(handler)
    
    # 3. Create File Handler
    file_handler = logging.FileHandler(log_file_path, mode='w', encoding='utf-8') # 'w' overwrites, use 'a' to append
    
    # 4. Define Log Format
    # You can customize this format as needed
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    
    # 5. Add Handler to Logger
    logger.addHandler(file_handler)
    
    # Log a start message
    logger.info(f"--- STARTING TEST: {test_name} ---")

    # The 'yield' pauses the fixture and runs the actual test function
    yield logger

    # --- TEARDOWN phase (after the test function runs) ---
    logger.info(f"--- FINISHED TEST: {test_name} ---")
    
    # 6. Clean Up
    # Remove the file handler to ensure it doesn't leak into the next test
    logger.removeHandler(file_handler)
    file_handler.close()