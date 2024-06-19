import logging

logging.basicConfig(
    level=logging.INFO,
    format='[{asctime}] #{levelname:8} {filename}:'
           '{lineno} - {name} - {message}',
    style='{'
)
logger = logging.getLogger(__name__)
file_handler = logging.handlers.RotatingFileHandler(
    'logs/logs.log', mode='a', maxBytes=10240, backupCount=1
)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)
