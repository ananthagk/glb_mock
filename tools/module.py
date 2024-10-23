"""
Platform level definitions
Description: The file includes platform specific defines which are common for all modules.
"""

# ---------------------#
#    Import Section   #
# ---------------------#

from enum import Enum
import logging

# ---------------------#
#      Constants      #
# ---------------------#

# ---------------------#
#   Type Definitions  #
# ---------------------#


# Define module names
class SlkModules(Enum):
    MODULE_DUMMY = "MODULE_DUMMY"
    MODULE_TOOLS = "MODULE_TOOLS"
    MODULE_ETHERNET = "MODULE_ETHERNET"


# ---------------------#
#      Exceptions     #
# ---------------------#


# ---------------------#
#       Variables     #
# ---------------------#
registered_interfaces = {}


# ---------------------#
#  Public Interfaces #
# ---------------------#
def register_module_interface(interface_description):
    """
    Register module interfaces.

    Args:
        interface_description (list or dict): A list of interface descriptions or a single interface description.
    """
    if isinstance(interface_description, dict):
        # Convert single interface description to a list
        interface_description = [interface_description]

    for interface in interface_description:
        module = interface["MODULE_NAME"]
        function = interface["FUNCTION_NAME"]
        description = interface["DESCRIPTION"]

        if module not in SlkModules.__members__:
            raise ValueError(f"Invalid module name: {module}")

        if module not in registered_interfaces:
            registered_interfaces[module] = []

        registered_interfaces[module].append(
            {"FUNCTION_NAME": function, "DESCRIPTION": description}
        )


def display_module_functions(module: str):
    """
    Display functions and descriptions for a given module.

    Args:
        module_name (str): The name of the module.
    """
    if module not in registered_interfaces:
        print(f"No functions registered for module: {module}")
        return

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)-8s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Calculate the maximum length of function names for alignment
    max_length = max(len(func["FUNCTION_NAME"]) for func in registered_interfaces[module])

    print(f"Functions for module {module}:")
    for func in registered_interfaces[module]:
        function_name = func["FUNCTION_NAME"]
        description = func["DESCRIPTION"]
        print(f"{function_name:<{max_length}} : {description}")

    print("\n")


# ---------------------#
#  Private Interfaces #
# ---------------------#
