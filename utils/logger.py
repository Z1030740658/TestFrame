"""
Logger initialization.
"""
import logging
from logging import handlers
from datetime import datetime
import os
from utils import PROJECT_PATH

log_folder = os.path.join(PROJECT_PATH, "logs")
log_name = "root.log"

# create folder if not exists
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

file_name = os.path.join(log_folder, log_name)

# Create logger
log = logging.getLogger("logger")
log.setLevel("DEBUG")

date_format = "%m-%d-%Y_%H.%M.%S"
name_format = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] - %(message)s"

fmt = logging.Formatter(name_format, date_format)
console_handler = logging.StreamHandler()
console_handler.setFormatter(fmt)

file_handler = handlers.RotatingFileHandler(filename=datetime.now().strftime(file_name.format(date_format)),
                                            maxBytes=(1048576 * 5),
                                            backupCount=7)
file_handler.setFormatter(fmt)
log.addHandler(console_handler)
log.addHandler(file_handler)
