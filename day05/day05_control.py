"""
UPSKILLER · DAY 05 · Lesson B exercises · Control flow: if/elif/else, loops,
enumerate, zip, while, break/continue
Run:  python day05_control.py      Goal: 7/7 (6 exercises + drill)
Rules: RETURN, don't print. Never edit the tests. ERROR DIARY under every function
you had to fix. Hints at the bottom, then the sealed drill solution.
"""
import sys
import traceback


# EX 1 — if / elif / else. BMI category:
#   below 18.5 -> "underweight" · 18.5 up to (not incl.) 25 -> "normal"
#   25 up to (not incl.) 30 -> "overweight" · 30 or more -> "obese"
def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese" 
# ERROR DIARY 1:


# EX 2 — enumerate. Number the samples starting at 1.
# number_samples(["S01", "S02"]) -> ["1: S01", "2: S02"]
def number_samples(samples):
    numbered = []
    for i, sample in enumerate(samples, start=1):
        numbered.append(f"{i}: {sample}")
    return numbered
# ERROR DIARY 2:


# EX 3 — zip. Two lists that belong together: sample IDs and their concentrations.
# Return the IDs whose concentration is at least the threshold.
# above_threshold(["S01", "S02", "S03"], [45.2, 8.7, 61.0], 40) -> ["S01", "S03"]
def above_threshold(ids, concs, threshold):
    passed = []
    for sample_id, conc in zip(ids, concs):
        if conc >= threshold:
            passed.append(sample_id)
    return passed
# ERROR DIARY 3:


# EX 4 — while. Cells double every generation. How many doublings until the
# population reaches AT LEAST the target?
# doublings_needed(100, 800) -> 3   (100 -> 200 -> 400 -> 800)
# doublings_needed(100, 100) -> 0
def doublings_needed(start, target):
    count = 0
    population = start
    while population < target:
        population *= 2
        count += 1
    return count
# ERROR DIARY 4:


# EX 5 — enumerate + early return. Position (index from 0) of the FIRST QC score
# below the cutoff. If none fail, return -1.
# first_failed([0.9, 0.95, 0.4, 0.3], 0.5) -> 2
def first_failed(scores, cutoff):
    for i, score in enumerate(scores):
        if score < cutoff:
            return i
    return -1
# ERROR DIARY 5:


# EX 6 — continue. Mean of the readings, SKIPPING missing values (None).
# If there are no real readings, return None.
# clean_mean([2.0, None, 4.0]) -> 3.0       clean_mean([None]) -> None
def clean_mean(readings):
    total = 0
    n = 0
    for r in readings:
        if r is None:
            continue
        total += r
        n += 1
    if n == 0:
        return None
    return total / n
# ERROR DIARY 6:


# DAILY DRILL B — CODING (13 min, timed) · LeetCode 242 "Valid Anagram"
# Two DNA strings are anagrams if they contain exactly the same letters the same
# number of times, in any order.
# is_anagram("GATTACA", "ACATTAG") -> True     is_anagram("AAG", "AGG") -> False
# Use Monday's COUNTING DICT (B4!) — no sorted() allowed in your first version.
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    counts_s = {}
    for letter in s:
        counts_s[letter] = counts_s.get(letter, 0) + 1
    counts_t = {}
    for letter in t:
        counts_t[letter] = counts_t.get(letter, 0) + 1
    return counts_s == counts_t


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
    assert bmi_category(17.0) == "underweight"
    assert bmi_category(18.5) == "normal"
    assert bmi_category(24.9) == "normal"
    assert bmi_category(25.0) == "overweight"
    assert bmi_category(30.0) == "obese"

def t2():
    assert number_samples(["S01", "S02"]) == ["1: S01", "2: S02"]
    assert number_samples([]) == []

def t3():
    assert above_threshold(["S01", "S02", "S03"], [45.2, 8.7, 61.0], 40) == ["S01", "S03"]
    assert above_threshold(["S01"], [40.0], 40) == ["S01"]
    assert above_threshold([], [], 10) == []

def t4():
    assert doublings_needed(100, 800) == 3
    assert doublings_needed(100, 100) == 0
    assert doublings_needed(100, 801) == 4

def t5():
    assert first_failed([0.9, 0.95, 0.4, 0.3], 0.5) == 2
    assert first_failed([0.9, 0.8], 0.5) == -1
    assert first_failed([0.1], 0.5) == 0

def t6():
    assert clean_mean([2.0, None, 4.0]) == 3.0
    assert clean_mean([None]) is None
    assert clean_mean([]) is None

def t_drill():
    assert is_anagram("GATTACA", "ACATTAG") is True
    assert is_anagram("AAG", "AGG") is False
    assert is_anagram("AT", "ATT") is False
    assert is_anagram("", "") is True

if __name__ == "__main__":
    tests = [("Ex1 bmi_category", t1), ("Ex2 number_samples", t2),
             ("Ex3 above_threshold", t3), ("Ex4 doublings_needed", t4),
             ("Ex5 first_failed", t5), ("Ex6 clean_mean", t6), ("DRILL is_anagram", t_drill)]
    passed = sum(run_test(n, f) for n, f in tests)
    print(f"\n{passed}/{len(tests)} passed")


# ===========================================================================
# HINTS (only after 10 minutes stuck)
# ===========================================================================
# Ex1: check from the lowest band up: if bmi < 18.5 ... elif bmi < 25 ... elif bmi < 30 ... else.
#      Python stops at the FIRST true branch, so "< 25" already means 18.5–24.9.
# Ex2: for i, s in enumerate(samples, start=1): -> i is 1, 2, ...; s is the sample.
# Ex3: for sample_id, conc in zip(ids, concs): ... "at least" -> >=
# Ex4: count = 0 ; population = start ; while population < target: double it, count+1.
# Ex5: for i, score in enumerate(scores): if score < cutoff: return i
#      return -1 goes AFTER the loop (same mistake to avoid as the drill on list day).
# Ex6: total and n start at 0. Inside the loop: if r is None: continue (skip).
#      After the loop: if n == 0 return None, else return total / n.
#      Test for None with "is None", not "== None".
# Drill: build a counting dict for s and one for t (two loops, B4 pattern),
#      then return counts_s == counts_t   (two dicts are equal if same keys + counts).
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
# SEALED SOLUTION — DRILL B
# ===========================================================================
# def is_anagram(s, t):
#     if len(s) != len(t):          # quick exit: different lengths can't match
#         return False
#     counts_s = {}
#     for letter in s:
#         counts_s[letter] = counts_s.get(letter, 0) + 1
#     counts_t = {}
#     for letter in t:
#         counts_t[letter] = counts_t.get(letter, 0) + 1
#     return counts_s == counts_t   # == on dicts compares every key and value
#
# Trace "AAG" vs "AGG": counts_s = {"A": 2, "G": 1}, counts_t = {"A": 1, "G": 2}
#   -> not equal -> False.
# Pattern: COUNTING DICT (your B4), used twice and compared.
# Big-O: O(n) time, O(k) space (k = number of different letters).
# The short version: sorted(s) == sorted(t) -> correct, but O(n log n) because of
#   sorting. Know both; say why the dict version is faster in an interview.
# Common wrong answer: checking only that every letter of s is IN t ->
#   "AAG" and "AGG" would wrongly pass (same letters, different counts).
