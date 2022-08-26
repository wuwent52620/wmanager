import logging
import logging.config
import os

print()
LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            'format': '%(asctime)s %(filename)s %(lineno)s %(levelname)s %(message)s',
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": os.path.join(os.path.dirname(__file__), "wmanager.log"),
            "maxBytes": 1024 * 1024 * 36,
            "backupCount": 3
        }
    },
    "disable_existing_loggers": True,
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG"
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("root")
