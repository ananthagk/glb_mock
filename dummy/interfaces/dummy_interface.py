"""
Dummy interfaces
Description: Interfaces for Dummy module
"""

# ---------------------#
#    Import Section   #
# ---------------------#
# Import all necessary modules and packages required for the test script
import tools.module as _module

# ---------------------#
#      Constants      #
# ---------------------#
# Define any constants that will be used in the interface


# ---------------------#
#   Type Definitions  #
# ---------------------#
# Define any custom types or classes that will be used in the script


# ---------------------#
#      Exceptions     #
# ---------------------#
# Define any custom exceptions that will be used in the interface


# ---------------------#
#       Variables     #
# ---------------------#
# Declare any variables that will be used in the script


# ---------------------#
#  Public Interfaces #
# ---------------------#
# Define functions and classes that are intended to be used by other modules or scripts
def print_hello_world():
    print("Hello World")


def print_bye_world():
    print("Bye Bye World")


def register_external_interfaces():
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


# ---------------------#
#  Private Interfaces #
# ---------------------#
# Define functions and classes that are intended to be used only within this test script
