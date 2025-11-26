import os
import random
import string
import traceback
import pandas as pd

## Imports from the project folders
from empirical.dataset_stats import getFileLength
from mining.log_op_miner import (
    checkIfParsablePython,
    hasLogImport,
    getPythonAtrributeFuncs
)
from mining.mining import (
    giveTimeStamp,
    days_between
)


## Helper Funtions

# Generate a random string
def random_string(length = 10):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


# Generate random (likely invalid) file path
def random_path():
    parts = [random_string(5) for _ in range(random.randint(1, 3))]
    return "/".join(parts)


# Genrate random date
def random_date():
    # random YYYY-MM-DD
    year = random.randint(1990, 2025)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02}-{day:02}"


# Check for presence of 'crashes' folder
def ensure_crash_dir():
    if not os.path.exists("crashes"):
        os.makedirs("crashes")


# Save crash info to crashes/ folder
def log_crash(func_name, inp, error):
    ensure_crash_dir()
    filename = f"crashes/{func_name}_crash.txt"

    with open(filename, "a") as f:
        f.write("---- CRASH ----\n")
        f.write(f"Function: {func_name}\n")
        f.write(f"Input: {inp}\n")
        f.write("Error:\n")
        f.write(error + "\n\n")


## Fuzzing functions

def fuzz_noarg(func, iterations = 30):
    print(f"[+] Fuzzing {func.__name__} (no args)")
    for _ in range(iterations):
        try:
            func()
        except Exception as e:
            log_crash(func.__name__, "NO_ARGS", traceback.format_exc())


def fuzz_onearg(func, gen, iterations = 30):
    print(f"[+] Fuzzing {func.__name__} (1 arg)")
    for _ in range(iterations):
        val = gen()
        try:
            func(val)
        except Exception as e:
            log_crash(func.__name__, val, traceback.format_exc())


def fuzz_twoarg(func, gen1, gen2, iterations = 30):
    print(f"[+] Fuzzing {func.__name__} (2 args)")
    for _ in range(iterations):
        v1 = gen1()
        v2 = gen2()
        try:
            func(v1, v2)
        except Exception as e:
            log_crash(func.__name__, (v1, v2), traceback.format_exc())


## Main

def main():
    print("=== MLForensics Project Fuzzer ===")

    # empirical/dataset_stats.py
    fuzz_onearg(getFileLength, random_path)

    # mining/log.op.miner.py
    fuzz_onearg(checkIfParsablePython, random_path)
    fuzz_onearg(hasLogImport, random_string)
    fuzz_onearg(getPythonAtrributeFuncs, random_string)

    # mining/mining.py
    fuzz_noarg(giveTimeStamp)
    fuzz_twoarg(days_between, random_date, random_date)

    print("\nFuzzing completed. Check /crashes folder for crash logs.")


if __name__ == "__main__":
    main()
