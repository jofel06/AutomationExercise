import pytest
import datetime
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


# Create the Logs directory if it doesn't exist
def create_log_dir():
    log_dir = "Logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        logging.info("Logs directory created.")

#this configures pytest and logging
@pytest.hookimpl(tryfirst=True)
def pytest_configure():
    create_log_dir()

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

    # Set up the WebDriver
    if browser_name == "Chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "Edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")  # Enable headless mode
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(options=edge_options)
    else:
        raise ValueError("Unsupported browser!")
    logging.info(f"Starting the Test for: {test_file_name} using {browser_name} browser.")
    driver.maximize_window()
    yield driver

    # Cleanup
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

