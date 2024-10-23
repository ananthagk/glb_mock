"""
Logger Module
Description: The file includes functions to set log levels and log messages at various severities.
It initializes logging severities for each modules, which can be overridden at each module level.
"""
#---------------------#
#    Import Section   #
#---------------------#
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tools.platform_defines as platform

#---------------------#
#      Constants      #
#---------------------#

# Define log levels
LOG_LEVEL_DEBUG    = 1
LOG_LEVEL_INFO     = 2
LOG_LEVEL_WARNING  = 4
LOG_LEVEL_ERROR    = 8
LOG_LEVEL_CRITICAL = 16

#---------------------#
#   Type Definitions  #
#---------------------#

#---------------------#
#      Exceptions     #
#---------------------#

#---------------------#
#      Variables      #
#---------------------#

# Initialize Module levels log severity
module_log_levels = {
    platform.MODULE_TOOLS    : LOG_LEVEL_INFO | LOG_LEVEL_DEBUG   | LOG_LEVEL_WARNING | LOG_LEVEL_ERROR    | LOG_LEVEL_CRITICAL,
    platform.MODULE_ETHERNET : LOG_LEVEL_INFO | LOG_LEVEL_WARNING | LOG_LEVEL_ERROR   | LOG_LEVEL_CRITICAL
}

#---------------------#
#  Public Interfaces #
#---------------------#

def set_log_level(module, level):
    """
    Set the log level for a specific module.

    Args:
        module (str): The name of the module.
        level (int): The log level to set.
    """
    module_log_levels[module] = level


def message(level, module, message):
    """
    Log a message with a specific severity level for a given module.

    Args:
        level (int): The severity level of the log message.
        module (str): The name of the module.
        message (str): The log message.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)-8s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    if module in module_log_levels:
        if level & module_log_levels[module]:
            formatted_message = f"{module:<20}: {message}"
            if level == LOG_LEVEL_DEBUG:
                logging.debug(formatted_message)
            elif level == LOG_LEVEL_INFO:
                logging.info(formatted_message)
            elif level == LOG_LEVEL_WARNING:
                logging.warning(formatted_message)
            elif level == LOG_LEVEL_ERROR:
                logging.error(formatted_message)
            elif level == LOG_LEVEL_CRITICAL:
                logging.critical(formatted_message)


#---------------------#
#  Private Interfaces #
#---------------------#
