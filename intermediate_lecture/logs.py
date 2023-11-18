import logging
import logging.config

logging.config.fileConfig("logging.conf")

'''
# Refer to official Python documentation
# This configuration quite literally set the format for logging messages
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S")
'''

# If import module, it will lock message from module with name of logger
import helper

# creating this logger will create a hierarchy of loggers that starts at root logger, then new loggers get added to hierachy
# the new loggers propogate their messages up to the base logger
'''
# can log to 5 different levels that indicate the severity of events
logging.debug("This is a debug message")
logging.info("This is an info message")
# only messages of level "warning" or above are printed
# if we want to change this, we have to set basic configuration (see above - logging.basicConfig)
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# by default, our logger is called the "root" logger

# if you want to log in different modules, it's best practice to create your own loggers in your modules rather than using root logger
'''

# log handlers objects dispatch appropriate log messages to the handlers destination
logger = logging.getLogger(__name__)

# create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file.log")

# set level and format
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

stream_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
# set formatter to handler
stream_handler.setFormatter(stream_formatter)
file_handler.setFormatter(stream_formatter)

# add handler to logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning("this is a warning")
logger.error("this is an error")