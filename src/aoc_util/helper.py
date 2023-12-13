"""Helper functions to automate AOC"""

from pathlib import Path
from time import perf_counter_ns
from typing import Any


def read(path: str) -> str:
    """General Purpose Read a Text file"""
    return Path(path).read_text()


def write(path: str, data: str) -> None:
    """General Purpose Write to text file. Will create the file if it doesn't exists"""
    p = Path(path)
    if not p.parent.exists():
        p.parent.mkdir(parents=True)
    return p.write_text(data)


def check_paths_create_files(p: Path) -> bool:
    """
    Checks a pathlib Path object.
    Creates parent directories if they don't exist
    Creates the file if it doesn't exist

    Returns True if file is created
    Returns False if the file already exists
    """
    if not p.parent.exists():
        p.parent.mkdir(parents=True)
    if p.exists():
        return False
    p.touch()
    return True


def chunks(input_list: list, n: int = 5) -> list[list[Any]]:
    """
    params:
        l: taks in a list (or list like object)
        n: takes an int: default = 5 this is how big the smaller
            chunks will be
    returns:
        a list of lists with the smaller lists being size n
    """
    return [input_list[i : i + n] for i in range(0, len(input_list), n)]


"""
WRAPPERS
"""


# a timer wrapper to time functions in ns
def mytime(func):
    def wrapper(*args, **kwargs):
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        end = perf_counter_ns()
        print(f"RUN TIME: {func.__name__:>10} : {end - start:>10} ns")
        return result

    return wrapper





# average time decorator
def avgtime(run_times=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            times = []
            result = func(*args, **kwargs)
            for _ in range(run_times - 1):
                start = perf_counter_ns()
                func(*args, **kwargs)
                end = perf_counter_ns()
                times.append(end - start)
            if times:
                print(f"AVG TIME ({run_times} runs): {func.__name__:>10} : {sum(times)/len(times):>10} ns")
            return result
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator
