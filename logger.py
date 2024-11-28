import logging
import os
from datetime import datetime
from colorama import Fore, Style

# Create the /logs directory if it doesn't exist
log_dir = "./logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define the log file name based on the current date
log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure the logging system
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

# Define a custom logger
logger = logging.getLogger()

# Color definitions for different log levels
LOG_COLORS = {
    "DEBUG": Fore.BLUE,
    "INFO": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.MAGENTA
}

def log(message, level="info"):
    """
    Logs a message to both console and log file.
    
    Args:
        message (str): The message to log.
        level (str): The log level. Options are 'debug', 'info', 'warn', 'error', 'critical'.
                     Default is 'info'.
    """
    level = level.upper()
    color = LOG_COLORS.get(level, Fore.WHITE)
    formatted_message = f"{color}{message}{Style.RESET_ALL}"

    # Log to console with color and to file without color
    if level == "DEBUG":
        logger.debug(formatted_message)
    elif level == "INFO":
        logger.info(formatted_message)
    elif level in ("WARNING", "WARN"):
        logger.warning(formatted_message)
    elif level == "ERROR":
        logger.error(formatted_message)
    elif level == "CRITICAL":
        logger.critical(formatted_message)
    else:
        logger.info(f"{Fore.CYAN}Invalid log level: {level}. Defaulting to INFO.{Style.RESET_ALL}")
        logger.info(formatted_message)
