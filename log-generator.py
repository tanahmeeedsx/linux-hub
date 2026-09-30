#!/usr/bin/env python3

import logging
import random
import time

LOG_FILE = "/var/log/app.log"

# Custom ALERT log level
ALERT_LEVEL = 45
logging.addLevelName(ALERT_LEVEL, "ALERT")


def alert(self, message, *args, **kwargs):
    if self.isEnabledFor(ALERT_LEVEL):
        self._log(ALERT_LEVEL, message, args, **kwargs)


logging.Logger.alert = alert

# Configure logger
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("demo-app")

messages = {
    "INFO": [
        "Application is running normally",
        "User authentication completed successfully",
        "Database query completed successfully",
        "Health check passed",
        "API request processed successfully",
    ],

    "WARNING": [
        "CPU usage is above 70%",
        "Memory usage is approaching threshold",
        "API response time is increasing",
        "Database connection pool is almost full",
    ],

    "ERROR": [
        "ConnectionRefusedError: [Errno 111] Connection refused",
        "Database connection failed",
        "Unable to connect to upstream service",
        "HTTP 500 Internal Server Error",
        "Failed to process application request",
    ],

    "CRITICAL": [
        "Database service unavailable",
        "Application dependency has crashed",
        "Disk space critically low",
    ],

    "ALERT": [
        "Multiple authentication failures detected",
        "Application health check failed repeatedly",
        "Production service may be unavailable",
    ],
}


while True:
    level = random.choice(
        ["INFO", "INFO", "INFO", "WARNING", "ERROR", "ERROR", "CRITICAL", "ALERT"]
    )

    message = random.choice(messages[level])

    if level == "INFO":
        logger.info(message)

    elif level == "WARNING":
        logger.warning(message)

    elif level == "ERROR":
        logger.error(message)

    elif level == "CRITICAL":
        logger.critical(message)

    elif level == "ALERT":
        logger.alert(message)

    time.sleep(5)
