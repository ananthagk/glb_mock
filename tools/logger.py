"""
Logger Module
Description: The file includes functions to set log levels and log messages at various severities.
It initializes logging severities for each modules, which can be overridden at each module level.
"""
#---------------------#
#    Import Section   #
#---------------------#
from enum import Enum
import logging
import os
import sys
from typing import List
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tools.platform_defines as plt_def

#---------------------#
#      Constants      #
#---------------------#

#---------------------#
#   Type Definitions  #
#---------------------#
# Define log levels
class LogLevel(Enum):
    LOG_LEVEL_DEBUG    = "LOG_LEVEL_DEBUG"
    LOG_LEVEL_INFO     = "LOG_LEVEL_INFO"
    LOG_LEVEL_WARNING  = "LOG_LEVEL_WARNING"
    LOG_LEVEL_ERROR    = "LOG_LEVEL_ERROR"
    LOG_LEVEL_CRITICAL = "LOG_LEVEL_CRITICAL"

#---------------------#
#      Exceptions     #
#---------------------#

#---------------------#
#      Variables      #
#---------------------#

# Initialize Module levels log severity
module_log_levels = {
    "MODULE_TOOLS"    : {"LOG_LEVEL_INFO", "LOG_LEVEL_DEBUG",  "LOG_LEVEL_WARNING", "LOG_LEVEL_ERROR",   "LOG_LEVEL_CRITICAL" },
    "MODULE_ETHERNET" : {"LOG_LEVEL_INFO",                     "LOG_LEVEL_WARNING", "LOG_LEVEL_ERROR",   "LOG_LEVEL_CRITICAL"                      }
}

#---------------------#
#  Public Interfaces #
#---------------------#

def set_log_level(module: str, levels: List[str]):
    """
    Set the log level for a specific module.

    Args:
        module (str): The name of the module.
        levels (List[str]): The log levels to set.
    """
    if module not in plt_def.SlkModules.__members__:
        raise ValueError(f"Invalid module name: {module}")

    level_enums = set()
    for level in levels:
        if level not in LogLevel.__members__:
            raise ValueError(f"Invalid log level: {level}")
        level_enums.add(LogLevel[level])

    module_log_levels[module] = level_enums


def message(level: str, module: str, message: str):
    """
    Log a message with a specific severity level for a given module.

    Args:
        level (str): The severity level of the log message.
        module (str): The name of the module.
        message (str): The log message.
    """
    if level not in LogLevel.__members__:
        raise ValueError(f"Invalid log level: {level}")

    if module not in plt_def.SlkModules.__members__:
        raise ValueError(f"Invalid module name: {module}")

    level_enum  = LogLevel[level]
    module_enum = plt_def.SlkModules[module]

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)-8s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    if level_enum in module_log_levels.get(module, set()):
        # Align the module name to a fixed width (e.g., 20 characters)
        formatted_message = f"{module_enum.value:<20}: {message}"
        if level_enum == LogLevel.LOG_LEVEL_DEBUG:
            logging.debug(formatted_message)
        elif level_enum == LogLevel.LOG_LEVEL_INFO:
            logging.info(formatted_message)
        elif level_enum == LogLevel.LOG_LEVEL_WARNING:
            logging.warning(formatted_message)
        elif level_enum == LogLevel.LOG_LEVEL_ERROR:
            logging.error(formatted_message)
        elif level_enum == LogLevel.LOG_LEVEL_CRITICAL:
            logging.critical(formatted_message)


#---------------------#
#  Private Interfaces #
#---------------------#
