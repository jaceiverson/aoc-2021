import datetime as dt
import warnings
from pathlib import Path

import pytz
from bs4 import BeautifulSoup
from requests.models import HTTPError
from rich import print

from aoc_util.aoc_requests import get_aoc_page
from aoc_util.helper import check_paths_create_files, write

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
        "\nInput is not ready. "
        "Please request a valid day, or wait for your input to be ready.",
        UserWarning,
        f"src/file_creation.py : get_input(day={day},year={year}) : line ",
        50,
        "newday",
    )
    return False


def get_all_code_formated_html(url: str) -> list:
    """
    Will return a list of all the code blocks on the page
    """
    r = get_aoc_page(url)

    soup = BeautifulSoup(r.text, "html.parser")
    code_elements = soup.find_all("code")

    return [code.text for code in code_elements]


def longest_code_snippet(code: list) -> str:
    """
    Will return the longest code snippet from a list of code snippets
    """
    return max(code, key=len)


def pull_example_input(url: str):
    code = get_all_code_formated_html(url)
    if code:
        return longest_code_snippet(code)
    print()


def get_main_input(url: str):
    """
    gets main input for url
    """
    r = get_aoc_page(url)
    if not r.ok:
        raise HTTPError(
            f"Did not get status 200. STATUS: {r.status_code}, "
            "verify session cookie is correct"
        )
    return r


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
    if is_aoc_input_ready(day, year):
        file_path = Path(f"./{year}/inputs/{day}.txt")
        print(f"-> CREATING INPUT FILE: [yellow]{file_path}")
        if check_paths_create_files(file_path):
            # if the file didn't exist (this function creates it),
            # get the input and save to to the file
            r = get_main_input(f"https://adventofcode.com/{year}/day/{day}/input")
            with open(file_path, "w") as f:
                f.write(r.text)
            print(f"[green]-> INPUT FILE SAVED: {file_path}\n")
        else:
            print("[blue]-> FILE EXISTS. Will not overwrite\n")
    else:
        print(f"[red]-> INPUT IS NOT READY FOR YEAR: {year} DAY: {day}")


def create_test_input_file(day: int, year: int, suffix: str = None) -> None:
    """
    Creates a test input file for the given day and year
    Will add a suffix to the file name if suffix is not None
    """
    if suffix is None:
        file_path = Path(f"./{year}/inputs/{day}-test.txt")
    else:
        file_path = Path(f"./{year}/inputs/{day}-test-{suffix}.txt")
    print(f"-> CREATING TEST INPUT FILE: [yellow]{file_path}")
    # if the folder doesn't exists, create it
    if check_paths_create_files(file_path):
        print(f"[green]-> TEST INPUT FILE CREATED: {file_path}\n")
    else:
        print("[blue]-> FILE EXISTS. Will not overwrite.\n")


def create_test_input_file_from_example(year: int, day: int):
    if is_aoc_input_ready(day, year):
        file_path = f"./{year}/inputs/{day}-test-e.txt"
        print(f"-> CREATING TEST INPUT FILE FROM EXAMPLE INPUT: [yellow]{file_path}")
        if check_paths_create_files(Path(file_path)):
            input_example = pull_example_input(
                f"https://adventofcode.com/{year}/day/{day}"
            )
            write(file_path, input_example)
            print(f"[green]-> TEST INPUT FILE CREATED FROM EXAMPLE: {file_path}\n")
        else:
            print("[blue]-> FILE EXISTS. Will not overwrite.\n")
    else:
        print(f"[red]-> INPUT IS NOT READY FOR YEAR: {year} DAY: {day}")


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
    file_path = Path(f"./{year}/solutions/day{day}.py")
    print(f"-> CREATING PYTHON FILE: [yellow]{file_path}")
    # read in the template file
    template_file_name = "TEMPLATE_FILE.py"
    file_text = Path(template_file_name).read_text()
    # alter the template to include the actual year and day
    file_text = file_text.replace("{year}", str(year)).replace("{day}", str(day))

    # creates the python file in solutions
    if check_paths_create_files(file_path):
        with open(file_path, "a") as f:
            f.write(file_text)
        print(f"[green]-> FILE CREATED FROM TEMPLATE: {template_file_name}\n")
    else:
        print("[blue]-> FILE EXISTS. Will not overwrite\n")
