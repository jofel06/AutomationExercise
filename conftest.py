import pytest
import datetime
import os
import logging
from selenium import webdriver

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Create the Logs directory if it doesn't exist
    log_dir = "Logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        logging.info("Logs directory created")

    # Basic logging configuration to display logs in the console
    logging.basicConfig(
        level=logging.INFO,  # Set to INFO level
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()  # Output to console
        ]
    )
    logging.info("Logging is configured for pytest.")


"""Driver Fixture for handling different browser and dynamic logging for each"""
@pytest.fixture(params=["Chrome", "Edge"])
def driver(request):
    browser_name = request.param
    test_file_name = request.node.parent.name # This gives the test file's name
    logging.info(f"Starting the Test for: {test_file_name} using {browser_name} browser.")

    # Generate log filename based on browser and current date/time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"Test_Log_for_{test_file_name}_using_{browser_name}_on_{current_time}.log"

    # Create a new file handler for the browser-specific log file
    log_dir = "Logs"
    file_handler = logging.FileHandler(f"{log_dir}/{log_filename}")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Add file handler to the root logger
    logging.getLogger().addHandler(file_handler)

    # Set up WebDriver based on the browser
    if request.param == "Chrome":
        driver = webdriver.Chrome()
    elif request.param == "Edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser!")

    driver.maximize_window()
    yield driver
    driver.quit()
    logging.info(f"Test completed for {test_file_name} using {browser_name}.")
    logging.getLogger().removeHandler(file_handler)



"""Fixture for Capturing a Screenshot"""
@pytest.fixture
def take_screenshot(driver):
    #Take a screenshot and save it to the specified directory.
    def this_screenshot(filename):
        if not os.path.exists("Screenshots"):
            os.makedirs("Screenshots")
        screenshot_path = os.path.join("Screenshots", filename)
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
        return screenshot_path
    return this_screenshot

