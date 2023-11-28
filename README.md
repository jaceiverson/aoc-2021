# AOC Util for Python

A library to help create files and pull inputs for the <a href=https://adventofcode.com>Advent of Code</a>. Can be used to generate previous years input/files as well.

# AOC Star Summary

| Year   | Stars | Completion % |
| ------ | ----- | ------------ |
| [2023] |       | 0            |
| [2022] | 21    | 42           |
| [2021] | 25    | 50           |
| [2020] | 14    | 28           |
| [2019] | 10    | 20           |
| [2018] | 10    | 20           |
| [2017] | 15    | 30           |
| [2016] | 20    | 40           |
| [2015] | 32    | 64           |
| TOTAL  | 147   | 32.67        |

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

You will need to have your session id saved as an environment variable. You can find your session ID in the chrome inspect tool in either Network or Application. In Network you will have to inspect a request and find the cookie in the header. In Application you will have to find the Cookies section.

1. Create a `.env` file in the main directory of the project
2. Save your session id in your .env file in this format

```
COOKIE_SESSION={YOUR_SESSION_ID_HERE}
```

Now you will be able to use the automation without a hitch. Carry on.

# File Automation

The automation of this project relies on the `newday` and `update-readme` modules. We will run these as scripts as defined by the pyproject.toml.

## update-readme - Automatic Summary Table Update

Automatically update (or generate) your summary table like <a href=https://github.com/jaceiverson/aoc-util#AOC-Star-Summary>the one above</a>.

> 1. scrapes the AOC site to look at how many stars you have completed for each year
> 2. saves those numbers as markdown
> 3. replaces the existing table with the updated values

To do this, run the command

```
update-readme
```

Note: for this to happen, you must have saved your <a href=https://github.com/jaceiverson/aoc-util#Session-id-cookie>session id</a> as an environment variable.

## newday - Running the File Creation & Input Extraction Script

Generate files for each day's solution as well as pulling in the input .txt files from the site.

1.  Creates a .py and .txt file for the specified day / year
    - directories will be created if necessary
2.  Pre-populate generic values (you can change this in the newday folder).
    - More information on the project <a href=https://github.com/jaceiverson/aoc-util#File-Structure>file structure</a>.<br>

```
newday
```

### Solution Files

Below is the template for the solution .py files that are generated

```py
"""https://adventofcode.com/{year}/day/{day}"""

from aoc_util import read

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
newday -i -d 7 -y 2014
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
    └── aoc_util
        ├── __init__.py
        ├── aoc_requests.py
        ├── file_creation.py
        ├── helper.py
        └── readme.py
└── 20**/
    └── input/
    └── solutions/
└── .env
```
