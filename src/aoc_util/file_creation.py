"""Help create files and pull input for AOC"""
from argparse import ArgumentParser
from pathlib import Path
import datetime as dt
import warnings
from rich import print
import pytz

# HTTP Requests
from requests.models import HTTPError

# local module to request pages from AOC
from aoc_util.aoc_requests import get_aoc_page

# EASTERN TIME FOR EVERYTHING
EASTERN = pytz.timezone("US/Eastern")

def is_aoc_input_ready(day: int, year: int) -> bool:
    """
    checks to see if the input is ready to be pulled
    """
    today = dt.datetime.now(EASTERN)
    if EASTERN.localize(dt.datetime(year, 12, day)) <= today:
        return True
    warnings.warn_explicit(
        "\nInput is not ready. Please request a valid day, or wait for your input to be ready.",
        UserWarning,
        f"src/file_creation.py : get_input(day={day},year={year}) : line ",
        50,
        "newday",
    )
    return False


def create_input_file(day: int, year: int) -> None:
    """
    Uses your session cookie (to get your specific login) to pull your
    Puzzle Inputs. You can find session cookie
    in the developer portal of your browswer.

    For Chrome "Application" > "Storage" > "Cookies" >
    Find the session and retreave the value.

    Accepts a day, saves the input if it doesn't exist already
    Will create "./inputs" folder if it doesn't exist

    Note:
        This does not create the test input (from the question),
        you will have to create that file yourself or 
        use the -t (--test-input) flag to create an empty file
    """
    file_path = Path(f"./{year}/inputs/{day}.txt")
    # if the folder doesn't exists, create it
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True)
    # if the file doesn't exists, create it and save the request data
    if not file_path.exists():
        # HTTP request
        r = get_aoc_page(f"https://adventofcode.com/{year}/day/{day}/input")
        if not r.ok:
            raise HTTPError(
                f"Did not get status 200. STATUS: {r.status_code}, "
                "verify session cookie is correct"
            )
        with open(file_path, "w") as f:
            f.write(r.text)
        print(f"INPUT SAVED: {file_path}")
    else:
        print(f"{file_path} already exists. Will not overwrite")

def create_test_input_file(day:int,year:int,suffix:str = None) -> None:
    """
    Creates a test input file for the given day and year
    Will add a suffix to the file name if suffix is not None
    """
    if suffix is None: 
        file_path = Path(f"./{year}/inputs/{day}-test.txt")
    else:
        file_path = Path(f"./{year}/inputs/{day}-test-{suffix}.txt")
    # if the folder doesn't exists, create it
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True)
    # if the file doesn't exist, create it
    if not file_path.exists():
        file_path.touch()
        print(f"TEST INPUT FILE CREATED: {file_path}")
    else:
        print(f"TEST INPUT FILE EXISTS. NOT CREATED. {file_path}")


def create_python_file(day: int, year: int) -> None:
    """
    Will create a python file will all the lines of code I normally use
    Also will create the "./solutions" directory if it doesn't exists

    What is included in the Python File Template:
    1. Doc String with URL to today's challenge
    2. import statement to get the file reader
    3. code line to read the input
    4. part1 & part2 answer print statements

    TO RUN from the main directory in terminal:
        $ python solutions/helper.py {day int to create}
    """
    # read in the tempalte file
    with open("TEMPLATE_FILE.py", "r") as f:
        file_text = f.read()

    # alter the template to include the actual year and day
    file_text = file_text.replace("{year}", str(year)).replace("{day}", str(day))

    # creates the python file in solutions
    file_path = Path(f"./{year}/solutions/day{day}.py")
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True)
    if not file_path.exists():
        with open(file_path, "a") as f:
            f.write(file_text)
        print(f"FILE CREATED FROM TEMPLATE: {file_path}")
    else:
        print(f"{file_path} already exists. Will not overwrite")


def newday() -> None:
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
        nargs="?",
        default=False,
        const=True,
        type=bool,
        help="If tagged retrives the selected day's input. Requires session cookie as env variable.",
    )
    parser.add_argument(
        "-t",
        "--test-input",
        nargs="?",
        default="",
        type=str,
        help="Creates an empty .txt file with optional sub-tags named",
    )
    args = parser.parse_args()

    if args.day is None and args.year is None and dt.datetime.now(EASTERN).month != 12:
        raise ValueError("Sorry. Default values are only available in December.")

    if args.day is None:
        args.day = dt.datetime.now(EASTERN).day
    if args.year is None:
        args.year = dt.datetime.now(EASTERN).year

    # CHECK VALUES to make sure they are in range
    if args.day not in range(1, 26):
        raise ValueError("Day needs to be in range (1-25)")
    if args.year not in range(2015, dt.datetime.now(EASTERN).year + 1):
        raise ValueError(
            f"Year needs to be in range {range(2015,dt.datetime.now(EASTERN).year+1)}"
        )

    print(args)
    print("CREATING PYTHON FILE")
    create_python_file(args.day, args.year)
    if args.input and is_aoc_input_ready(args.day, args.year):
        print("CREATING INPUT FILE")
        create_input_file(args.day, args.year)

    if args.test_input!="":
        print("CREATING TEST INPUT FILE")
        create_test_input_file(args.day, args.year,args.test_input)
        
    print("PROCESS COMPLETE")


if __name__ == "__main__":
    newday()
