# AOC Util for Python

A library to help create files and pull inputs for the <a href=https://adventofcode.com>Advent of Code</a>. Can be used to generate previous years input/files as well.

# AOC Star Summary
| Year   |   Stars |   Completion % |
|--------|---------|----------------|
| [2023] |         |           0    |
| [2022] |      21 |          42    |
| [2021] |      25 |          50    |
| [2020] |      14 |          28    |
| [2019] |      10 |          20    |
| [2018] |      10 |          20    |
| [2017] |      15 |          30    |
| [2016] |      20 |          40    |
| [2015] |      32 |          64    |
| TOTAL  |     147 |          32.67 |

# Installation

## Clone Repo

Navigate to your desired directory in terminal. Run the `git clone` command to download the files:

```
git clone https://github.com/jaceiverson/aoc-util.git
```

Now you have the files on your machine

## Create virtual environment

I recommended to create a virtualenv using the <a href="https://pypi.org/project/virtualenv/" target="_blank">virtualenv library</a>. Follow these steps:

## install the package to main python instance

```
pip3 install virtualenv
```

## actually create the virtual environment

```
python3 -m virtualenv venv
```

## activate the environment

```
source venv/bin/activate
```

## install all the necessary packages

```
pip install -r requirements.txt
```

Now we are all installed and need one more step before the automation can begin

# Session id cookie

You will need to have your session id saved as an environment variable. In this project I use dotenv; this allows me to store these variables in a .env file, and access them in my code after using the `load_dotenv()` function.

1. Create a `.env` file in the main directory of the project
2. Save your session id in your .env file in this format

```
COOKIE_SESSION={YOUR_SESSION_ID_HERE}
```

Now you will be able to use the automation without a hitch. Carry on.

# File Automation

The automation of this project relies on the `newday` and `update-readme` modules. We will run modules using the standard syntax of python modules: `python -m {module-name}`

## update-readme - Automatic Summary Table Update

Automatically update (or generate) your summary table like <a href=https://github.com/jaceiverson/aoc-util#AOC-Star-Summary>the one above</a>.

> 1. scrapes the AOC site to look at how many stars you have completed for each year
> 2. saves those numbers as markdown
> 3. replaces the existing table with the updated values

To do this, run the command

```
python -m update-readme
```

Note: for this to happen, you must have saved your <a href=https://github.com/jaceiverson/aoc-util#Session-id-cookie>session id</a> as an environment variable.

## newday - Running the File Creation & Input Extraction Script

Generate files for each day's solution as well as pulling in the input .txt files from the site.

1.  Creates a .py and .txt file for the specified day / year
    - directories will be created if necessary
2.  Pre-populate generic values (you can change this in the newday folder).
    - More information on the project <a href=https://github.com/jaceiverson/aoc-util#File-Structure>file structure</a>.<br>

```
python -m newday
```

### Solution Files

Below is the template for the solution .py files that are generated

```py
"""https://adventofcode.com/{year}/day/{day}"""

from helper import read

# READ INPUT
data = read("./{year}/inputs/{day}.txt")
# TEST INPUT
# data = read("./{year}/inputs/{day}-test.txt")
# PARSE INPUT

# PART 1
part_1_answer = None
print(f"PART 1: {part_1_answer}")

# PART 2
part_2_answer = None
print(f"PART 2: {part_2_answer}")
```

## newday - Flags

Use flags to add additional arguments to the script. You will add the value after you type the flag. If you wanted to create a file and get the input for Dec 7, 2014's challenge, you would do the following

```
python -m newday -i -d 7 -y 2014
```

### -i (--input)

Pulls the input for the day selected. Must have session id stored as an environment variable named COOKIE_SESSION in the .env file

default: False

### -d (--day)

Changes the day from today's date to any other daily puzzle. Selection is ints from 1-25.

default: today's date (int)

### -y (--year)

Changes the year from the current year to any of the previous. Selection is each year including and after 2015. (2015-)

default: today's year (int)

## Flag Ordering

It does not matter the order that you have your flags, just know that the values should follow the flag.

# File Structure

When you clone/fork and set up this repo for use, you should have the following file structure

```
advent_of_code/
└── src/
    └── helper/
        └── __init__.py
        └── helper.py
        └── newday/
            └── __init__.py
            └── __main__.py
            └── file_creation.py
        └── update-readme/
            └── __init__.py
            └── __main__.py
            └── update.py
└── 20**/
    └── input/
    └── solutions/
└── .env
└── venv
```
