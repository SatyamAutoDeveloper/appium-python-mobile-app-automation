# Appium Python Mobile App Automation

A sample Android mobile automation framework built with Appium, Python, and pytest. This repository contains automated test cases for two sample Android apps:

- `tourist_guide_app.apk`
- `fastshopping.apk`

The framework uses Appium's UiAutomator2 driver and a pytest-based test suite with logging, screenshot capture, and HTML reporting support.

## Project Structure

- `apps/` - APK files used for automation.
- `helpers/` - Utility modules for mobile actions and reusable operations.
- `locators/` - UI locator definitions for the app screens.
- `pages/` - Page/activity-level implementations and verification methods.
- `tests/` - Test cases for the two mobile apps.
- `conftest.py` - Pytest fixtures, Appium driver setup, and test reporting hooks.
- `requirements.txt` - Python dependencies for the automation framework.
- `.gitignore`       - To exclude virtual environment and other unwanted files from version control.
- `.github/workflows/`  - GitHub Actions workflow for CI/CD integration.
- `pytest.ini `  - For custom markers, logging and html report configuration.

## Prerequisites

- Python 3.10+ (or a supported version for the listed dependencies)
- Appium server installed and running
- Android SDK or emulator/device accessible via Appium
- `pip` available for installing dependencies

## Setup

### Enable Java and Android SDK

Ensure the following are installed and configured:

- Java JDK
- Android SDK (ADB)
- Node.js

### Install and Configure Appium

1. Install Appium globally:

```powershell
npm install -g appium
```

2. Install the UiAutomator2 driver:

```powershell
appium driver install uiautomator2
```

3. Verify the Appium installation:

```powershell
appium driver doctor uiautomator2
```

4. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

5. Install dependencies:

```powershell
pip install -r requirements.txt
```

6. Verify your Android emulator or device is available:

```powershell
adb devices
```

7. Start the Appium server:

```powershell
appium
```

### Inspect Mobile App Locators

Use the UIAutomator Viewer Inspector to identify UI elements:

8. Open the UIAutomatorViewer batch file:

```
C:\Users\username\AppData\Local\Android\Sdk\tools\bin\uiautomatorviewer.bat
```

9. Connect your emulator or device and inspect elements to determine locators for your tests.

## Running Tests

### Run the default app tests

The default app configuration is `tourist_app`.

```powershell
pytest -q
```

### Run tests for a specific app

Use the `--app_name` option with one of the configured keys:

- `tourist_app`
- `fastshopping_app`

```powershell
pytest -q --app_name=fastshopping_app
```

### Run a single test file

```powershell
pytest -q tests/test_fast_shopping_app.py --app_name=fastshopping_app
```

## Configured Apps

The supported app configurations are defined in `conftest.py`:

- `tourist_app`
  - APK: `apps/tourist_guide_app.apk`
  - Package: `com.dataflair.myapplication`
  - Activity: `.MainActivity`
- `fastshopping_app`
  - APK: `apps/fastshopping.apk`
  - Package: `me.wolszon.fastshopping`
  - Activity: `.MainActivity`

## Reporting and Logs

- Failure screenshots are saved in `screenshots/` when a test fails.
- Per-test log files are written to `logs/`.
- The framework is configured to attach screenshots into pytest HTML reports when available.

## Notes

- Ensure the Appium server URL in `conftest.py` matches your local setup (`http://127.0.0.1:4723`).
- Update device capabilities in `conftest.py` if you need to run tests on a real device or a different emulator.
- Add or modify page objects and locators in `pages/` and `locators/` as the app UI changes.


## Self-Healing Agent Documentation Used in UI Automation Framework
Primary Differences between Selenium UI (Web) and Appium (Mobile) Self-Healing Agents: [https://github.com/SatyamAutoDeveloper/appium-python-mobile-app-automation/wiki/The-primary-difference-between-a-Selenium-UI-(Web)-and-an-Appium-(Mobile)-self%E2%80%90healing-agent]