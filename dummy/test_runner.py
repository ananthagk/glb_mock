#!/usr/bin/env python3
"""
Template for test_runner launcher script
Description: Provides basic infrastructure to pring help message and launching scripts
"""

# ---------------------#
#    Import Section    #
# ---------------------#
import argparse

import tools.module as _module
import dummy.interfaces.dummy_interface as _dummy

# ---------------------#
#      Constants       #
# ---------------------#



# ---------------------#
#   Type Definitions   #
# ---------------------#



# ---------------------#
#       Variables      #
# ---------------------#



# ---------------------#
#  Private Interfaces  #
# ---------------------#



def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="Launcher script to run GLB test scripts.",
        usage="test_runner.py [OPTIONS] <input_script>"
    )

    # Add the positional argument
    parser.add_argument(
        'input_script',
        type=str,
        nargs='?',
        help='Path to input script.'
    )

    # Add optional arguments
    parser.add_argument(
        '-l', '--list-interfaces',
        action='store_true',
        help='Lists external interfaces of this module.'
    )
    parser.add_argument(
        '-o', '--output_file',
        type=str,
        default='test_runner.log',
        help='Path to output file (default: test_runner.log).'
    )
    parser.add_argument(
        '-t', '--list-tests',
        action='store_true',
        help='Lists available tests of this module.'
    )

    # Parse the arguments
    args = parser.parse_args()

    # Register all the external interfaces
    _dummy.register_external_interfaces()

    # Implement the functionality based on the parsed arguments
    if args.list_interfaces:

        _module.display_module_functions("MODULE_DUMMY")

    if args.list_tests:
        print("Listing available tests...")
        # Add your code to list tests here

    #print(f"Running input script: {args.input_script}")
    #print(f"Output will be saved to: {args.output_file}")
    # Add your code to run the input script here

if __name__ == "__main__":
    main()
