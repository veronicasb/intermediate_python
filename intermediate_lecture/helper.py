import logging

# Best practice to create your own logger with this function
logger = logging.getLogger(__name__)

# if we dont want propagation to base logger, use code below
# so basically, nothing will appear in the terminal if you set this to False
logger.propagate = False
logger.info("Hello from helper")