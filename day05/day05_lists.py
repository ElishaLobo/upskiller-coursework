"""
UPSKILLER · DAY 05 · Lesson A exercises · Lists and tuples
Run:  python day05_lists.py      Goal: 7/7 (6 exercises + drill)
Rules: RETURN, don't print. Never change the input list unless the exercise says so.
Never edit the tests. ERROR DIARY under every function you had to fix.
Hints at the bottom, then the sealed drill solution.
"""
import sys
import traceback


# EX 1 — First and last sample as a TUPLE.
# first_last(["S01", "S02", "S03"]) -> ("S01", "S03")
def first_last(samples):
    samples = samples[0], samples[-1]
    return samples
# ERROR DIARY 1:


# EX 2 — The three highest values, highest first, WITHOUT changing the input list.
# top_three([5, 1, 9, 7, 3]) -> [9, 7, 5]
def top_three(values):
    highest = sorted(values, reverse=True)[:3]
    return highest
# ERROR DIARY 2:


# EX 3 — Every other well, starting with the first (slicing with a step).
# every_other(["A1", "A2", "A3", "A4", "A5"]) -> ["A1", "A3", "A5"]
def every_other(wells):
    every_other = wells[::2]
    return every_other
# ERROR DIARY 3:


# EX 4 — A NEW list of the samples that did NOT fail QC. Keep the original order.
# passed_qc(["S01", "S02", "S03", "S04"], ["S02", "S04"]) -> ["S01", "S03"]
def passed_qc(samples, failed):
    passed = []
    for sample in samples:
        if sample not in failed:
            passed.append(sample)
    return passed
# ERROR DIARY 4:


# EX 5 — Tuple unpacking. A well is stored as (row, column), e.g. ("B", 7).
# Return its label "B07": row letter + column as 2 digits.
# well_label(("B", 7)) -> "B07"      well_label(("H", 12)) -> "H12"
def well_label(well):
    row, col = well
    return f"{row}{col:02d}"
# ERROR DIARY 5:


# EX 6 — Add a new reading to the END of a series IN PLACE (this one SHOULD change
# the list) and return how many readings there are now.
# r = [1.0, 2.0]; add_reading(r, 3.0) -> 3   and afterwards r == [1.0, 2.0, 3.0]
def add_reading(readings, value):
    readings.append(value)
    return len(readings)
# ERROR DIARY 6:


# DAILY DRILL A — CODING (13 min, timed) · LeetCode 217 "Contains Duplicate"
# Return True if any sample ID appears more than once, else False.
# contains_duplicate(["S01", "S02", "S01"]) -> True
# contains_duplicate(["S01", "S02"])        -> False
# Use one of TODAY's tools (a list of IDs seen so far) or Monday's (a dictionary).
def contains_duplicate(ids):
    seen = []
    for sample_id in ids:
        if sample_id in seen:
            return True
        seen.append(sample_id)
    return False


# ===================== TESTS — do not edit =====================
def run_test(name, fn):
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except Exception:
        print(f"FAIL  {name}")
        print("----- error message (read from the BOTTOM line upwards) -----")
        traceback.print_exc(file=sys.stdout)
        print("--------------------------------------------------------------\n")
        return False

def t1():
    assert first_last(["S01", "S02", "S03"]) == ("S01", "S03")
    assert first_last(["S09"]) == ("S09", "S09")
    assert isinstance(first_last(["a", "b"]), tuple), "must return a TUPLE"

def t2():
    v = [5, 1, 9, 7, 3]
    assert top_three(v) == [9, 7, 5]
    assert v == [5, 1, 9, 7, 3], "you changed the input list!"
    assert top_three([2, 8]) == [8, 2]

def t3():
    assert every_other(["A1", "A2", "A3", "A4", "A5"]) == ["A1", "A3", "A5"]
    assert every_other([]) == []

def t4():
    s = ["S01", "S02", "S03", "S04"]
    assert passed_qc(s, ["S02", "S04"]) == ["S01", "S03"]
    assert s == ["S01", "S02", "S03", "S04"], "you changed the input list!"
    assert passed_qc(["S01"], []) == ["S01"]

def t5():
    assert well_label(("B", 7)) == "B07"
    assert well_label(("H", 12)) == "H12"

def t6():
    r = [1.0, 2.0]
    assert add_reading(r, 3.0) == 3
    assert r == [1.0, 2.0, 3.0], "the list itself should now contain the new reading"

def t_drill():
    assert contains_duplicate(["S01", "S02", "S01"]) is True
    assert contains_duplicate(["S01", "S02"]) is False
    assert contains_duplicate([]) is False

if __name__ == "__main__":
    tests = [("Ex1 first_last", t1), ("Ex2 top_three", t2), ("Ex3 every_other", t3),
             ("Ex4 passed_qc", t4), ("Ex5 well_label", t5), ("Ex6 add_reading", t6),
             ("DRILL contains_duplicate", t_drill)]
    passed = sum(run_test(n, f) for n, f in tests)
    print(f"\n{passed}/{len(tests)} passed")


# ===========================================================================
# HINTS (only after 10 minutes stuck)
# ===========================================================================
# Ex1: index 0 is first, index -1 is last. (a, b) builds a tuple.
# Ex2: sorted(values, reverse=True) makes a NEW sorted list; .sort() would change
#      the input. Then slice the first 3.
# Ex3: list[start:stop:step]. Leave start and stop empty.
# Ex4: COUNTER-style loop, but instead of count+1 you .append() to a new list.
#      Test membership with:  if sample not in failed:
# Ex5: row, col = well   (unpacking). Then an f-string: {col:02d} = 2 digits, zero-padded.
# Ex6: .append() changes the list in place and returns None — so don't write
#      return readings.append(value). Append first, then return len(readings).
# Drill: seen = [] ; for each id: if id in seen -> return True ; else append it.
#      After the loop (all checked, no repeat) -> return False.
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
# SEALED SOLUTION — DRILL A
# ===========================================================================
# def contains_duplicate(ids):
#     seen = []                    # IDs met so far
#     for sample_id in ids:
#         if sample_id in seen:    # met before -> duplicate found
#             return True          # stop immediately: we know the answer
#         seen.append(sample_id)
#     return False                 # loop finished: no repeats anywhere
#
# Pattern: "seen so far" (a cousin of the counter).
# Big-O: `x in list` checks every item one by one -> O(n) per check -> O(n^2) total.
#   With a SET (Thursday's lesson) `x in set` is O(1) -> O(n) total. Interviewers
#   expect the set version; this list version is the honest first step.
# Common wrong answers:
#   return False inside the loop (in an else:) -> stops after the FIRST item.
#     "return False" must be AFTER the loop, at the function's indentation.
#   len(ids) != len(set(ids)) -> correct and short, but you haven't learned sets yet.
