#!/usr/bin/env python3


"""
Test Script Template
Description: [Brief description of the test script]
"""


#---------------------#
#    Import Section   #
#---------------------#
# Import all necessary modules and packages required for the test script
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tools.logger as log
import tools.platform_defines as platform

#---------------------#
#      Constants      #
#---------------------#
# Define any constants that will be used in the test script


#---------------------#
#   Type Definitions  #
#---------------------#
# Define any custom types or classes that will be used in the script


#---------------------#
#       Variables     #
#---------------------#
# Declare any variables that will be used in the script


#---------------------#
#  Private Interfaces #
#---------------------#
# Define functions and classes that are intended to be used only within this test script


#---------------------#
#  Pre-tests Section  #
#---------------------#
# Code that sets up the environment before all tests are run

def _pre_test():
    """
    Pre-tests setup. This function is called once before all tests.
    """
    return 0


#---------------------#
#    Setup Section    #
#---------------------#
# Code that sets up the environment before each individual test

def _setup_test():
    """
    Setup. This function is called before each test.
    """
    return 0


#---------------------#
#    Execute Section  #
#---------------------#
# Code that contains the actual tests

def _execute_test():
    """
    Execute. This function contains the actual test.
    """
    return 0


#---------------------#
#  Post-test Section  #
#---------------------#
# Code that cleans up the environment after each individual test

def _post_test():

    """
    Post-test. This function is called after each test.
    """
    pass


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
    log.set_log_level(platform.MODULE_TOOLS, log.LOG_LEVEL_INFO | log.LOG_LEVEL_DEBUG | log.LOG_LEVEL_ERROR)

    try:
        return_code = main()
    except:
        return_code = -1
        log.message(log.LOG_LEVEL_ERROR, platform.MODULE_TOOLS, "Exception: An error occurred")

    log.message(log.LOG_LEVEL_INFO, platform.MODULE_TOOLS, f"Test completed with return code : {return_code}")

    sys.exit(return_code)
