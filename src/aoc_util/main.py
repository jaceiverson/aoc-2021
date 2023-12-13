"""Help create files and pull input for AOC"""
import datetime as dt
from argparse import ArgumentParser

import pytz
from rich import print

# local module to request pages from AOC
from aoc_util.files import (
    create_input_file,
    create_python_file,
    create_test_input_file,
    create_test_input_file_from_example,
)

# EASTERN TIME FOR EVERYTHING
EASTERN = pytz.timezone("US/Eastern")


def newday() -> None:
    print("[yellow]--- PROCESS STARTING ---\n")
    parser = ArgumentParser(description="Create AOC Python Files from template.")
    parser.add_argument(
        "-d",
        "--day",
        nargs="?",
        default=None,
        type=int,
        help="Defaults to today's date (day), can change to any day (1-25)",
    )
    parser.add_argument(
        "-y",
        "--year",
        nargs="?",
        default=None,
        type=int,
        help="Defaults to this year, can change to any previous year (2015-).",
    )
    parser.add_argument(
        "-i",
        "--input",
        action="store_true",
        help="If tagged retries the selected day's input. "
        "Requires session cookie as env variable.",
    )
    parser.add_argument(
        "-t",
        "--test-input",
        nargs="?",
        default="",
        type=str,
        help="Creates an empty .txt file with optional sub-tags named",
    )
    parser.add_argument(
        "-s",
        "--save-example-input",
        action="store_true",
        help="Scrape the day for the example input, save to {day}-test-e.txt file.",
    )
    args = parser.parse_args()

    if args.day is None and args.year is None and dt.datetime.now(EASTERN).month != 12:
        raise ValueError("Sorry. Default values are only available in December.")

    # if we are here that means we have some values,
    # but we may need to check and default some of our
    # values if they were omitted
    if args.day is None:
        args.day = dt.datetime.now(EASTERN).day
    if args.year is None:
        args.year = dt.datetime.now(EASTERN).year

    # now we can check the values to make sure they are in range
    # day between 1 and 25
    # year between 2015 and whatever the current year is
    if args.day not in range(1, 26):
        raise ValueError("Day needs to be in range (1-25)")
    if args.year not in range(2015, dt.datetime.now(EASTERN).year + 1):
        raise ValueError(
            f"Year needs to be in range {range(2015,dt.datetime.now(EASTERN).year+1)}"
        )

    # we will always attempt to create the python file here
    create_python_file(args.day, args.year)

    """CONDITIONAL CREATIONS"""

    # Create Input File (prod)
    if args.input:
        create_input_file(args.day, args.year)

    # Create a Test Input File (testing)
    if args.test_input != "":
        create_test_input_file(args.day, args.year, args.test_input)

    # Create a Test Input File from Example in Problem
    if args.save_example_input:
        create_test_input_file_from_example(args.year, args.day)

    print("[yellow]--- PROCESS COMPLETE ---")


if __name__ == "__main__":
    newday()
