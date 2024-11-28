import logging
import os
import requests
import threading
from queue import Queue
from datetime import datetime
from colorama import Fore, Style

# Create the /logs directory if it doesn't exist
log_dir = "./logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define the log file name based on the current date in the format YYYY-MM-DD.log
log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger()

# Color definitions for different log levels
LOG_COLORS = {
    "DEBUG": Fore.BLUE,
    "INFO": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.MAGENTA
}

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

log_queue = Queue()

def send_to_discord(embed):
    """Sends an embed to Discord using the webhook."""
    if not DISCORD_WEBHOOK_URL:
        return
    try:
        payload = {"embeds": [embed]}
        requests.post(DISCORD_WEBHOOK_URL, json=payload)
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to send log to Discord: {e}")

def discord_worker():
    """Worker function to process log messages from the queue."""
    while True:
        log_entry = log_queue.get()
        if log_entry is None:
            break  # Exit the thread
        send_to_discord(log_entry)
        log_queue.task_done()

# Start the Discord logging worker thread
discord_thread = threading.Thread(target=discord_worker, daemon=True)
discord_thread.start()

def create_discord_embed(message, level):
    """Creates a Discord embed for the log message."""
    color_map = {
        "DEBUG": 3447003,  # Blue
        "INFO": 3066993,   # Green
        "WARNING": 15105570,  # Yellow
        "ERROR": 15158332,    # Red
        "CRITICAL": 10181046  # Purple
    }
    color = color_map.get(level, 15844367)  # Default to gray
    return {
        "title": f"Log - {level}",
        "description": message,
        "color": color,
        "timestamp": datetime.utcnow().isoformat()
    }

def log(message, level="info"):
    """
    Logs a message to both console, log file, and optionally to Discord.
    
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

    if DISCORD_WEBHOOK_URL:
        embed = create_discord_embed(message, level)
        log_queue.put(embed)

# Cleanup function to stop the worker thread
def cleanup():
    log_queue.put(None)
    discord_thread.join()