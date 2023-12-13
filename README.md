# AOC Util for Python

A library to help create files and pull inputs for the <a href=https://adventofcode.com>Advent of Code</a>. Can be used to generate previous years input/files as well.

# AOC Star Summary

| Year   | Stars | Completion % |
| ------ | ----- | ------------ |
| [2023] | 6     | 12           |
| [2022] | 21    | 42           |
| [2021] | 25    | 50           |
| [2020] | 14    | 28           |
| [2019] | 10    | 20           |
| [2018] | 13    | 26           |
| [2017] | 15    | 30           |
| [2016] | 20    | 40           |
| [2015] | 32    | 64           |
| TOTAL  | 156   | 34.67        |

# Installation and Setup

To make this project work, you will need to do 3 things as setup:

1. pip install from GitHub
2. Create a template file named TEMPLATE_FILE.py
3. Save your Advent of Code Session ID cookie as an environment variable.

## 1 - Install Directly from GitHub

The best way to install this is to do it directly from GitHub with the following command:

```
pip install git+https://github.com/jaceiverson/aoc-util.git
```

This will allow you to run the command `newday` and `update-readme` in your project.

> Remember that it is always best practice to use a virtual environment.

## 2 - TEMPLATE FILE

You will need to have a template file named `TEAMPLATE_FILE.py` in the root of your project for this to work. I have provided an example of one here. The script for `newday` will use that template to create your file for the given day. You can change the template however you'd like, and the script will replace all instances of `{year}` and `{day}` with the current year and day combination provided to the script (see defaults and flags below).

## 3 - Session ID cookie

You will need to have your session id saved as an environment variable. You can find your session ID in the chrome inspect tool (right click anywhere on the page, then find Inspect--normally on the bottom of the right click menu) in either Network or Application tab after signing into Advent of Code.

> In the Network tab you will have to inspect a request and find the cookie in the header of that request

> In the Application tab you will have to find the Cookies section on the left menu

1. Create a `.env` file in the main directory of the project
2. Save your session id in your .env file in this format

```
COOKIE_SESSION={YOUR_SESSION_ID_HERE}
```

Now you will be able to use the automation without a hitch. Carry on.

# File Automation

The automation of this project relies on the `newday` and `update-readme` modules. We will run these as scripts as defined by the pyproject.toml.

# update-readme - Automatic Summary Table Update

Automatically update (or generate) your summary table like <a href=https://github.com/jaceiverson/aoc-util#AOC-Star-Summary>the one above</a>.

> 1. scrapes the AOC site to look at how many stars you have completed for each year
> 2. saves those numbers as markdown
> 3. replaces the existing table with the updated values

To do this, run the command

```
update-readme
```

Note: for this to happen, you must have saved your <a href=https://github.com/jaceiverson/aoc-util#Session-id-cookie>session id</a> as an environment variable.

# newday - Running the File Creation & Input Extraction Script

Generate files for each day's solution as well as pulling in the input .txt files from the site.

1.  Creates a .py and .txt file for the specified day / year
    - directories will be created if necessary
    - defaults to the current date (`dt.date.today()`)
2.  Pre-populate generic values (you can change this in the `TEMPLATE_FILE.py` file)

```
newday
```

If you run `newday` outside of December it will throw an error. You can by pass this by defining flags (see below) to generate files outside of December. You will never be able to get inputs for future dates (only past ones), but you can generate files for future days by using the correct flags.

You could run it on past years, or with other flags to get around that.

> Create a solution file for December 1st (doesn't get input file)

```
newday -d 1
```

> Create a solution file for December 1st, 2015 and pulls in the input data

```
newday -d 1 -y 2015 -i
```

## newday - Flags

Use flags to add additional arguments to the script. You will add the value after you type the flag. If you wanted to create a file and get the input for Dec 7, 2014's challenge, you would do the following

```
newday -i -d 7 -y 2014 -t a
```

### -i (--input)

> Default functionality: do NOT pull input for the day

Pulls the input for the day selected. Must have session id stored as an environment variable named COOKIE_SESSION in the .env file

### -d (--day)

> Default functionality: today's date (int)

Changes the day from today's date to any other daily puzzle. Selection is ints from 1-25.

### -y (--year)

> Default functionality: today's year (int)

Changes the year from the current year to any of the previous. Selection is each year including and after 2015. (2015-)

### -t (--test-input)

> Default functionality: does not create a -test.txt file

Creates a test input file that you can use to trial code. You can also include a name (no spaces in the name) and that will add a suffix to the file name. If not included no test file will be created. Here are a few examples:

```
newday -t
```

> Creates a file named `./{year}/inputs/{day}-test.txt`

```
newday -t p1
```

> Creates a file named `./{year}/inputs/{day}-test-p1.txt`
> Common use case for when part_1 and part_2 have different sample inputs

```
newday -t custom-file-name-test
```

> Creates a file named `./{year}/inputs/{day}-test-custom-file-name-test.txt`
> Not sure why, but you could do this

## -s (--save-example-input)

> Default functionality: does NOT pull example input

Sometimes we want to go as far as creating an input .txt file from the example given directly in the problem. This flag will do that. It scrapes the problem page for the given day and saves it in a file named `./{year}/inputs/{day}-test-e.txt` (e for example).

## Other newday examples

```
newday -d 2 -i -t -s
```

> Create a new file for the 2nd of the current year. Pull the main input, create a test file, create another test file and populate the example input from the problem. Output below:

```
--- PROCESS STARTING ---

-> CREATING PYTHON FILE: 2023/solutions/day2.py
-> FILE CREATED FROM TEMPLATE: TEMPLATE_FILE.py

-> CREATING INPUT FILE: 2023/inputs/2.txt
-> INPUT FILE SAVED: 2023/inputs/2.txt

-> CREATING TEST INPUT FILE: 2023/inputs/2-test.txt
-> TEST INPUT FILE CREATED: 2023/inputs/2-test.txt

-> CREATING TEST INPUT FILE FROM EXAMPLE INPUT: ./2023/inputs/2-test-l.txt
-> TEST INPUT FILE CREATED FROM EXAMPLE: ./2023/inputs/2-test-l.txt

--- PROCESS COMPLETE ---
```

> You can run the same command again, and it will let you know that all the files already exist and the script will not overwrite them. Output below:

```
--- PROCESS STARTING ---

-> CREATING PYTHON FILE: 2023/solutions/day2.py
-> FILE EXISTS. Will not overwrite

-> CREATING INPUT FILE: 2023/inputs/2.txt
-> FILE EXISTS. Will not overwrite

-> CREATING TEST INPUT FILE: 2023/inputs/2-test.txt
-> FILE EXISTS. Will not overwrite.

-> CREATING TEST INPUT FILE FROM EXAMPLE INPUT: ./2023/inputs/2-test-l.txt
-> FILE EXISTS. Will not overwrite.

--- PROCESS COMPLETE ---
```

## Flag Ordering

It does not matter the order that you have your flags, just know that the values should follow the flag.

## Template File

Below is the `TEMPLATE_FILE.py` that other files are generated from:

```py
"""https://adventofcode.com/{year}/day/{day}"""

from aoc_util import read

# READ INPUT
data = read("./{year}/inputs/{day}.txt").strip().split("\n")
# TEST INPUT
# data = read("./{year}/inputs/{day}-test.txt").strip().split("\n")
# PARSE INPUT

# PART 1

part_1_answer = None
print(f"PART 1: {part_1_answer}")

# PART 2

part_2_answer = None
print(f"PART 2: {part_2_answer}")
```

# File Structure

When you clone/fork and set up this repo for use, you should have the following file structure

```
advent_of_code
└── src
    └── aoc_util
        ├── __init__.py
        ├── aoc_requests.py
        ├── files.py
        ├── grid.py
        ├── helper.py
        ├── main.py
        └── readme.py
├── README.md
├── TEMPLATE_FILE.py
├── pyproject.toml
├── requirements.txt
```

# Utility Functions

## helper.py

### Timing Decorators

You can use the timing decorators to time your functions. There are 2 options

- mytime
- avgtime

You will access them both using the decorator `@` and you can also specify if you'd like to return the time or just the regular function value. If you specify `return_time=True` your function will return a tuple, the regular function result and the second element will be the time it took to run. In both cases the time it took to run will be outputted to the terminal.

> The only different in the `@mytime` and `@avgtime` is the average time uses the plural `return_times=True` instead of the singular like `@mytime`. This is because `@avgtime` returns a list of values for each time it ran.

#### Return the time with the result

```py
from aoc_util.helper import mytime

@mytime(return_time=True)
def part_1():
    # read in data
    # do stuff
    # return value
    return True

result, time = part_1()
```

#### Just time the function, don't return the time

```py
from aoc_util.helper import mytime

@mytime()
def part_1():
    # read in data
    # do stuff
    # return value
    return True

result = part_1()
```

## grid.py

Really just for me to deal with the grid problems. Not really for use if you are learning as it takes some of the complexity out of dealing with 2D grids, but feel free to use as you'd like.

```py
from helper.grid import Grid
```
