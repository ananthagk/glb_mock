#!/usr/bin/env python3


"""
Test Script Template
Description: [Brief description of the test script]
"""

# ---------------------#
#    Import Section   #
# ---------------------#
# Import all necessary modules and packages required for the test script
import sys
import os

import tools.logger as _log
import tools.module as _module

# ---------------------#
#      Constants      #
# ---------------------#
# Define any constants that will be used in the test script


# ---------------------#
#   Type Definitions  #
# ---------------------#
# Define any custom types or classes that will be used in the script


# ---------------------#
#       Variables     #
# ---------------------#
# Declare any variables that will be used in the script


# ---------------------#
#  Private Interfaces #
# ---------------------#
# Define functions and classes that are intended to be used only within this test script


# ---------------------#
#  Pre-tests Section  #
# ---------------------#
# Code that sets up the environment before all tests are run


def _pre_test():
    """
    Pre-tests setup. This function is called once before all tests.
    """
    return 0


# ---------------------#
#    Setup Section    #
# ---------------------#
# Code that sets up the environment before each individual test


def _setup_test():
    """
    Setup. This function is called before each test.
    """
    interface_description = [
        {
            "MODULE_NAME": "MODULE_DUMMY",
            "FUNCTION_NAME": "print_hello_world",
            "DESCRIPTION": "Prints hello world",
        },
        {
            "MODULE_NAME": "MODULE_DUMMY",
            "FUNCTION_NAME": "print_bye_world",
            "DESCRIPTION": "Prints bye world",
        },
    ]
    _module.register_module_interface(interface_description)

    return 0


# ---------------------#
#    Execute Section  #
# ---------------------#
# Code that contains the actual tests


def _execute_test():
    """
    Execute. This function contains the actual test.
    """
    _module.display_module_functions("MODULE_DUMMY")
    return 0


# ---------------------#
#  Post-test Section  #
# ---------------------#
# Code that cleans up the environment after each individual test


def _post_test():
    """
    Post-test. This function is called after each test.
    """
    return 0


def main():
    return_code = 0

    # pre-test
    return_code += _pre_test()

    # setup test
    return_code += _setup_test()

    # execute test
    return_code += _execute_test()

    # post-test
    return_code += _post_test()


if __name__ == "__main__":
    # Configure logging
    _log.set_log_level("MODULE_TOOLS", ["LOG_LEVEL_INFO", "LOG_LEVEL_DEBUG", "LOG_LEVEL_ERROR"])

    try:
        return_code = main()
    except Exception as e:
        return_code = -1
        _log.message("LOG_LEVEL_ERROR", "MODULE_TOOLS", f"Exception: An error occurred {e}")

    _log.message(
        "LOG_LEVEL_INFO", "MODULE_TOOLS", f"Test completed with return code : {return_code}"
    )

    sys.exit(return_code)
