import logging
from app.configs.env import env

# Define ANSI color codes
class ANSIColors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"

# Disable uvicorn access logger
uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True

logger = logging.getLogger("uvicorn")
logger.setLevel(env.LOGLEVEL)

class FunctionNameFormatter(logging.Formatter):
    def format(self, record):
        log_level = record.levelname
        func_name = record.funcName
        timestamp = self.formatTime(record, datefmt="%Y-%m-%d %H:%M:%S")

        # Define color based on log level
        if log_level == "INFO":
            log_color = ANSIColors.GREEN
        elif log_level == "WARNING":
            log_color = ANSIColors.YELLOW
        elif log_level == "ERROR" or log_level == "CRITICAL":
            log_color = ANSIColors.RED
        else:
            log_color = ANSIColors.RESET

        log_message = f"{timestamp} | {log_color}{log_level}{ANSIColors.RESET} | ENG | V1 | {log_color}{func_name}{ANSIColors.RESET} | {log_color}{record.getMessage()}{ANSIColors.RESET}"
        return log_message

# Set the custom formatter
for handler in logger.handlers:
    handler.setFormatter(FunctionNameFormatter())