from us_visa.logger import logging
from us_visa.exceptions import USVisaException
import sys


logging.info("This is an info message 2.")

try:
    a = 2/0
except Exception as e:
    raise USVisaException(e, sys)