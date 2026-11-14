"""
UPSKILLER · DAY 1 · Exercises
Topic: running Python from the terminal + reading error messages

HOW TO USE THIS FILE
1. Save it into your folder:  ~/upskiller/day01/
2. In the terminal (with your `ds` environment active):
       cd ~/upskiller/day01
       python day01_exercises.py
3. Every exercise prints PASS or FAIL. A FAIL shows the full error message
   (the "traceback"). READ IT: the last line names the error, the line
   above it shows where it happened.
4. Fix the function, save (Cmd+S), run again. Repeat until everything says PASS.
5. For each bug, fill in your ERROR DIARY entry (the comment under the function):
       error name / line number / what it means in plain words / your fix

RULES
- Only change the code inside the functions. Never change the tests at the bottom.
- Hints are at the very bottom of the file. Only look after 10 minutes stuck.
- The DAILY DRILL solution is sealed at the very end. Attempt first, timed (13 min).
"""

import os
import sys
import traceback


# ---------------------------------------------------------------------------
# EXERCISE 1 — Setup check (no bug: just make it PASS by setting up correctly)
# ---------------------------------------------------------------------------
def check_setup():
    """Return True if Python is 3.11 or newer AND the conda environment 'ds' is active."""
    version_ok = sys.version_info >= (3, 11)
    env_ok = os.environ.get("CONDA_DEFAULT_ENV") == "ds"
    print(f"   Python version: {sys.version.split()[0]}  (need 3.11+)")
    print(f"   Active conda environment: {os.environ.get('CONDA_DEFAULT_ENV')}  (need: ds)")
    return version_ok and env_ok
# ERROR DIARY 1: (if it failed, what did you have to do to make it pass?)


# ---------------------------------------------------------------------------
# EXERCISE 2 — BMI calculator
# BMI = weight in kg divided by (height in metres) squared.
# Example: weight 70 kg, height 1.75 m  ->  70 / 1.75**2  =  22.86 (rounded to 2 dp)
# ---------------------------------------------------------------------------
def bmi(weight, height):
    """Return BMI rounded to 2 decimal places."""
    return round((weight / height ** 2), 2)
# ERROR DIARY 2:
#   error name:  syntax error
#   line number: 174
#   what it means:  missing closing parenthesis
#   my fix:  added closing parenthesis after the round function


# ---------------------------------------------------------------------------
# EXERCISE 3 — Describe a sample
# describe_sample("S01", 12.5)  must return  "Sample S01 has 12.5 ng/ul"
# ---------------------------------------------------------------------------
def describe_sample(sample_id, concentration):
    """Return a sentence describing a sample's concentration."""
    return f"Sample {sample_id} has {concentration} ng/ul"
# ERROR DIARY 3:
#   error name:  syntax error
#   line number: 187
#   what it means:  f-string not properly formatted
#   my fix:  added missing f-string prefix


# ---------------------------------------------------------------------------
# EXERCISE 4 — Last reading
# last_reading([36.5, 37.1, 38.2])  must return  38.2
# ---------------------------------------------------------------------------
def last_reading(readings):
    """Return the last value in the list of temperature readings."""
    return readings[-1]
# ERROR DIARY 4:
#   error name:list index out of range
#   line number:76
#   what it means:
#   my fix:


# ---------------------------------------------------------------------------
# EXERCISE 5 — Gene length lookup (must work whatever case the user types)
# gene_length("brca1") and gene_length("BRCA1") must both return 81189
# ---------------------------------------------------------------------------
GENE_LENGTHS = {"BRCA1": 81189, "TP53": 19149, "APOE": 3612}

def gene_length(name):
    """Return the length in base pairs of the gene, ignoring upper/lower case."""
    if name.islower():
        name = name.upper()
    return GENE_LENGTHS[name.upper()]
# ERROR DIARY 5:
#   error name:
#   line number:
#   what it means:
#   my fix:


# ---------------------------------------------------------------------------
# EXERCISE 6 — GC count (NO error message here: the bug is silent!)
# count_gc("ATGCGC") must return 4   (G, C, G, C)
# ---------------------------------------------------------------------------
def count_gc(sequence):
    """Return how many letters in the DNA sequence are G or C."""
    count = 0
    for base in sequence:
        if base == "G" or base == "C":
            count = count + 1
    return count
# ERROR DIARY 6:
#   why is there no error message?
#   what was wrong:
#   my fix:


# ---------------------------------------------------------------------------
# EXERCISE 7 — Average of readings
# average([2, 4, 6]) must return 4.0
# average([])        must return None   (an empty list has no average)
# ---------------------------------------------------------------------------
def average(values):
    """Return the mean of the list, or None if the list is empty."""
    if not values:
        return None
    return sum(values) / len(values)
# ERROR DIARY 7:
#   error name:
#   line number:
#   what it means:
#   my fix:


# ---------------------------------------------------------------------------
# DAILY DRILL — CODING (13 minutes, timed. Start your timer now.)
# Running sum (LeetCode 1480)
# Given a list of numbers, return a NEW list where position i holds the sum of
# all numbers from position 0 up to and including position i.
#   running_sum([1, 2, 3, 4])   ->  [1, 3, 6, 10]
#   running_sum([5])            ->  [5]
#   running_sum([])             ->  []
# Lab version: daily cell counts -> cumulative cell count.
# ---------------------------------------------------------------------------
def running_sum(numbers):
    # write your code here (remember: RETURN the list, don't print it)
    i=0
    new_list = []
    for i in range(len(numbers)):
        if i == 0:
            new_list.append(numbers[i])
        else:
            new_list.append(new_list[i-1] + numbers[i])
    return new_list

    pass


# ===========================================================================
# TESTS — do not edit anything below this line (except reading it!)
# ===========================================================================
def run_test(name, test_function):
    try:
        test_function()
        print(f"PASS  {name}")
        return True
    except Exception:
        print(f"FAIL  {name}")
        print("----- error message (read from the BOTTOM line upwards) -----")
        traceback.print_exc(file=sys.stdout)
        print("--------------------------------------------------------------\n")
        return False


def test_1():
    assert check_setup() is True, "Python 3.11+ and conda env 'ds' must be active"

def test_2():
    assert bmi(70, 1.75)

def test_3():
    assert describe_sample("S01", 12.5) == "Sample S01 has 12.5 ng/ul"

def test_4():
    assert last_reading([36.5, 37.1, 38.2]) == 38.2
    assert last_reading([40.0]) == 40.0

def test_5():
    assert gene_length("BRCA1") == 81189
    assert gene_length("brca1") == 81189
    assert gene_length("Tp53") == 19149

def test_6():
    assert count_gc("ATGCGC") == 4, f"expected 4, got {count_gc('ATGCGC')}"
    assert count_gc("AAAA") == 0, f"expected 0, got {count_gc('AAAA')}"

def test_7():
    assert average([2, 4, 6]) == 4.0
    assert average([]) is None

def test_drill():
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([5]) == [5]
    assert running_sum([]) == []
    assert running_sum([3, -1, 2]) == [3, 2, 4]


if __name__ == "__main__":
    tests = [
        ("Exercise 1  setup check", test_1),
        ("Exercise 2  bmi", test_2),
        ("Exercise 3  describe_sample", test_3),
        ("Exercise 4  last_reading", test_4),
        ("Exercise 5  gene_length", test_5),
        ("Exercise 6  count_gc", test_6),
        ("Exercise 7  average", test_7),
        ("DAILY DRILL running_sum", test_drill),
    ]
    passed = sum(run_test(name, fn) for name, fn in tests)
    print(f"\n{passed}/{len(tests)} passed")


# ===========================================================================
# HINTS (only after 10 minutes stuck on one exercise)
# ===========================================================================
# Ex 1: Did you run `conda activate ds` in THIS terminal window before running
#       the file? The prompt should start with (ds).
# Ex 2: Python names must match exactly, letter for letter. Compare the name
#       in the parentheses at the top with the name used in the return line.
# Ex 3: You can only + a string to a string. 12.5 is a float. Two possible
#       fixes: str(...) around it, or an f-string: f"Sample {sample_id} ..."
# Ex 4: A list of 3 items has positions 0, 1, 2. What is len(readings)?
#       Is that a valid position? Python also allows negative positions...
# Ex 5: The dictionary keys are all UPPER case. Strings have a method that
#       turns "brca1" into "BRCA1".
# Ex 6: Python reads  base == "G" or "C"  as  (base == "G") or ("C").
#       A non-empty string like "C" counts as True on its own. So the
#       condition is ALWAYS true. Write the comparison out in full twice.
# Ex 7: What is len([])? What happens when you divide by it? Check for the
#       empty list FIRST with an if, and return None in that case.
# Drill: Start with an empty result list and a total of 0. Loop over the
#       numbers, add each to the total, append the total to the result.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# ===========================================================================
# SEALED SOLUTION — DAILY DRILL (open ONLY after your timed attempt)
# ===========================================================================
#
# def running_sum(numbers):
#     result = []          # the new list we will build and return
#     total = 0            # the sum so far, starts at nothing
#     for n in numbers:    # visit each number, left to right
#         total = total + n        # add this number to the running total
#         result.append(total)     # record the total at this position
#     return result        # RETURN (not print) so the test can check it
#
# Trace with [1, 2, 3, 4]:
#   n=1 -> total=1  -> result=[1]
#   n=2 -> total=3  -> result=[1, 3]
#   n=3 -> total=6  -> result=[1, 3, 6]
#   n=4 -> total=10 -> result=[1, 3, 6, 10]
# Empty list: the loop never runs, so we return [] — correct with no special case.
#
# Pattern name: "running total / prefix sum" (you'll meet it again in SQL as a
#   window function: SUM(...) OVER (ORDER BY ...)).
# Big-O: O(n) time (one pass over n numbers), O(n) extra space (the result list).
#
# Common wrong answer #1: sum(numbers[:i+1]) inside a loop -> correct output but
#   O(n^2): it re-adds everything from the start at every position.
# Common wrong answer #2: print(result) instead of return result -> the function
#   returns None and the test fails, even though the screen "looks right".
