import logging
import pytest
import datetime
import os

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Create the Logs directory if it doesn't exist
    log_dir = "Logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        logging.info("Logs directory created")

    # Generate log filename with current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"test_log_{current_time}.log"

    # Set up the logging configuration
    logging.basicConfig(
        level=logging.INFO,  # Set to INFO level
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f"{log_dir}/{log_filename}"), # Log file directory
            logging.StreamHandler()  # Also log to console
        ]
    )
    logging.info("Logging is configured for pytest.")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Ensure logging handlers are closed after tests run."""
    yield  # Let the test run
    if call.when == "call":
        # Close all logging handlers to avoid ResourceWarning
        for handler in logging.getLogger().handlers:
            handler.close()
            logging.getLogger().removeHandler(handler)