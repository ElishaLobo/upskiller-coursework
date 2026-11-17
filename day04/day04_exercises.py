"""
UPSKILLER · DAY 4 (Mon 16 Nov) · Module M1 Python core I · Lesson 1
Topic: values, types, variables, operators (/ // % **), comparisons, f-strings

Run:   python day04_exercises.py
Rules (same as Day 1):
- Only change code inside the functions. Never edit the tests.
- Use RETURN, not print, inside every function.
- Fill in the ERROR DIARY under each function you had to fix (4 parts: error / line / meaning / fix).
- Hints at the bottom. Then the WARM-UP ANSWERS, then the sealed DRILL solution.
"""
import sys
import traceback


# ---------------------------------------------------------------------------
# EXERCISE 1 — Drug dose per kg of body weight
# dose_per_kg(500, 70)  ->  7.14   (500 / 70, rounded to 2 decimal places)
# ---------------------------------------------------------------------------
def dose_per_kg(dose_mg, weight_kg):
    dose=dose_mg / weight_kg
    return round(dose, 2)
# ERROR DIARY 1:


# ---------------------------------------------------------------------------
# EXERCISE 2 — Sample racks
# 50 samples, 12 per rack -> 4 FULL racks and 2 samples left over.
# full_racks(50, 12) -> 4        leftover(50, 12) -> 2
# Use // and %. No loops.
# ---------------------------------------------------------------------------
def full_racks(samples, per_rack):
    full=samples // per_rack
    return full

def leftover(samples, per_rack):
    left=samples % per_rack
    return left
# ERROR DIARY 2:


# ---------------------------------------------------------------------------
# EXERCISE 3 — Fever check
# Return True if the temperature is 38.0 °C or higher, otherwise False.
# Do it in ONE line: no if/else. (Remember diagnostic B1.)
# ---------------------------------------------------------------------------
def is_fever(temp_c):
    return temp_c >= 38.0
# ERROR DIARY 3:


# ---------------------------------------------------------------------------
# EXERCISE 4 — Celsius to Fahrenheit:  F = C × 9/5 + 32
# c_to_f(37) -> 98.6     c_to_f(-40) -> -40.0
# Round to 1 decimal place.
# ---------------------------------------------------------------------------
def c_to_f(celsius):
    f = celsius * (9/5) + 32
    return round(f, 1)
# ERROR DIARY 4:


# ---------------------------------------------------------------------------
# EXERCISE 5 — Dilution (C1 × V1 = C2 × V2)
# You have a stock at concentration c1. How much stock (v1) do you need to make
# volume v2 at concentration c2?   v1 = c2 × v2 / c1
# stock_volume(c1=100, c2=10, v2=50) -> 5.0
# ---------------------------------------------------------------------------
def stock_volume(c1, c2, v2):
    v1 = c2 * v2 / c1
    return v1
# ERROR DIARY 5:


# ---------------------------------------------------------------------------
# EXERCISE 6 — Label with an f-string, concentration to 1 decimal place
# label("S01", 12.456) -> "S01: 12.5 ng/ul"
# label("S02", 7)      -> "S02: 7.0 ng/ul"
# ---------------------------------------------------------------------------
def label(sample_id, conc):
    return f"{sample_id}: {conc:.1f} ng/ul"
# ERROR DIARY 6:


# ---------------------------------------------------------------------------
# DAILY DRILL — CODING (13 min, timed) · LeetCode 1929 "Concatenation of Array"
# Return a NEW list that is the list followed by itself.
#   get_concatenation([1, 2, 1])  ->  [1, 2, 1, 1, 2, 1]
#   get_concatenation([])         ->  []
# Lab version: duplicate a plate layout for a technical replicate.
# Write it TWICE: version A with the + operator, version B with a for loop and .append()
# ---------------------------------------------------------------------------
def get_concatenation(nums):
    return nums + nums

def get_concatenation_loop(nums):
    results=[]
    for n in nums:
        results.append(n)
    for i in range(len(nums)):
        results.append(nums[i])
    return results

# ===========================================================================
# TESTS — do not edit
# ===========================================================================
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
    assert dose_per_kg(500, 70) == 7.14
    assert dose_per_kg(100, 50) == 2.0

def t2():
    assert full_racks(50, 12) == 4 and leftover(50, 12) == 2
    assert full_racks(24, 12) == 2 and leftover(24, 12) == 0
    assert full_racks(5, 12) == 0 and leftover(5, 12) == 5

def t3():
    assert is_fever(38.0) is True
    assert is_fever(39.2) is True
    assert is_fever(37.9) is False

def t4():
    assert c_to_f(37) == 98.6
    assert c_to_f(-40) == -40.0
    assert c_to_f(0) == 32.0

def t5():
    assert stock_volume(c1=100, c2=10, v2=50) == 5.0
    assert stock_volume(c1=2, c2=1, v2=10) == 5.0

def t6():
    assert label("S01", 12.456) == "S01: 12.5 ng/ul"
    assert label("S02", 7) == "S02: 7.0 ng/ul"

def t_drill():
    for f in (get_concatenation, get_concatenation_loop):
        assert f([1, 2, 1]) == [1, 2, 1, 1, 2, 1], f.__name__
        assert f([5]) == [5, 5], f.__name__
        assert f([]) == [], f.__name__
    original = [3, 4]
    get_concatenation_loop(original)
    assert original == [3, 4], "your loop version changed the input list!"

if __name__ == "__main__":
    tests = [("Ex1 dose_per_kg", t1), ("Ex2 full_racks / leftover", t2),
             ("Ex3 is_fever", t3), ("Ex4 c_to_f", t4), ("Ex5 stock_volume", t5),
             ("Ex6 label", t6), ("DRILL get_concatenation (both)", t_drill)]
    passed = sum(run_test(n, f) for n, f in tests)
    print(f"\n{passed}/{len(tests)} passed")


# ===========================================================================
# HINTS (only after 10 minutes stuck)
# ===========================================================================
# Ex1: round(value, 2). Use / (true division), not //.
# Ex2: 50 // 12 counts whole 12s in 50. 50 % 12 is what's left over.
# Ex3: a comparison like  temp_c >= 38.0  already IS True or False. Return it.
# Ex4: Python follows maths order: * and / before +. Then round(..., 1).
# Ex5: translate the formula letter by letter. Does it matter that the test uses
#      c1=..., c2=..., v2=...? (No: those are just the parameter names.)
# Ex6: f"{sample_id}: {conc:.1f} ng/ul"  — the :.1f means "1 decimal place".
# Drill B: start with result = [], loop over nums appending each item, then
#      loop AGAIN appending each item, return result. Don't append to nums itself!
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
# WARM-UP ANSWERS (Week 0 mini-test from the lesson doc) — check AFTER answering
# ===========================================================================
# 1. 3.5  3  1
# 2. 10  then  None          (no return -> None)
# 3. 1 2 3 4                 (range stops BEFORE 5)
# 4. [1, 2, 3, 4]            (b = a: one list, two names)
# 5. if x > 5:               (the colon!)
# 6. for t in temps:         (loop over the items, not len(temps))
# 7. -2.5                    (start "best" at the first item, not 0)
# 8. git add -> git commit -> git push
# 9. id_ed25519  (no .pub) is private; id_ed25519.pub can be shared
# 10. Sort first: 2 4 6 8 100 -> median 6
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
# SEALED SOLUTION — DRILL (open only after your timed attempt)
# ===========================================================================
# def get_concatenation(nums):
#     return nums + nums           # + on two lists builds a NEW joined list
#
# def get_concatenation_loop(nums):
#     result = []                  # new, empty list
#     for n in nums:               # first copy
#         result.append(n)
#     for n in nums:               # second copy
#         result.append(n)
#     return result
#
# Pattern: building a new list (never modify the input you were given).
# Big-O: O(n) time, O(n) extra space (the new list has 2n items).
# Common wrong answer: nums.extend(nums) or nums.append(...) on the INPUT ->
#   changes the caller's list (remember diagnostic A8: lists are shared, not copied).
# Another: `for n in nums: nums.append(n)` -> the list keeps growing while you
#   loop over it -> infinite loop. Ctrl+C to stop it.
