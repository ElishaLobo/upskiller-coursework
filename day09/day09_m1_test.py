"""
UPSKILLER · DAY 09 · M1 CLOSED-NOTEBOOK MINI-TEST
Run:  python day09_m1_test.py      Goal: 10/10 in 60 minutes.
RULES: CLOSED NOTEBOOK. No notes, no earlier files, no hints, no Google, no AI. Start a 60-minute timer NOW.
RETURN, don't print. Never edit the tests. If one task fights you for 8 minutes, leave it and come back.
When the timer rings: write your score at the top of your tab, then fill an ERROR DIARY under every function that failed
(error message, line, what it meant, fix). Sealed solutions are at the very bottom: open them only AFTER the timer.
"""
import sys
import traceback

# T1 — Branches. Return "underweight" if bmi is below 18.5, "normal" if below 25, "overweight" if below 30, else "obese".
# bmi_category(24.9) -> "normal"     bmi_category(25) -> "overweight"     bmi_category(18.5) -> "normal"
def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight" 
    else:
        return "obese"
# ERROR DIARY T1: no


# T2 — Counter. How many values are STRICTLY above the limit?
# count_over([70, 40, 66, 65], 65) -> 2
def count_over(values, limit):
    count = 0
    for v in values:
        if v > limit:
            count += 1
    return count
# ERROR DIARY T2: no


# T3 — Best so far. The smallest value WITHOUT min(). Return None for an empty list.
# lowest([3.2, 1.5, 2.8]) -> 1.5      lowest([]) -> None
def lowest(values):
    low=0
    if not values:
        return None
    low = values[0]
    for v in values:
        if v < low:
            low = v
    return low
# ERROR DIARY T3: no


# T4 — Counting dictionary. Letter -> how many times it appears.
# count_letters("AATG") -> {"A": 2, "T": 1, "G": 1}      count_letters("") -> {}
def count_letters(seq):
    count={}
    for letter in seq:
        count[letter] = count.get(letter, 0) + 1
    return count
    
# ERROR DIARY T4: no

# T5 — Dictionary + best so far. `doses` maps drug name -> mg. Return the NAME of the drug with the highest dose.
# If two drugs tie, the one that comes first wins. Return None for an empty dictionary. Loop with .items().
# top_drug({"A": 10, "B": 5.5, "C": 7}) -> "A"      top_drug({"A": 1, "B": 9}) -> "B"
def top_drug(doses):
    best_name = None
    best_mg = None
    for name, mg in doses.items():
        if best_mg is None or mg > best_mg:
            best_name = name
            best_mg = mg
    return best_name
# ERROR DIARY T5: no


# T6 — Set. The DIFFERENT values in the list, as a sorted list.
# unique_sorted(["Stroke", "Epilepsy", "Stroke"]) -> ["Epilepsy", "Stroke"]
def unique_sorted(items):
    return sorted(set(items))
# ERROR DIARY T6: no


# T7 — Do not change what you are given. Return a NEW list with `value` added at the end; the caller's list must stay as it was.
# r = [1, 2]; add_reading(r, 3) -> [1, 2, 3] and r is still [1, 2]
def add_reading(readings, value):
    return readings + [value]
# ERROR DIARY T7:


# T8 — BUG HUNT. This function is broken: the second call remembers the first. Fix it so every call without a
# dictionary starts from a fresh, empty one. (Change the def line too.)
# tally("a") -> {"a": 1}     tally("a") -> {"a": 1}  (again, NOT 2)     tally("b", {"a": 2}) -> {"a": 2, "b": 1}
def tally(word, counts=None):
    if counts is None:
        counts = {}
    for letter in word:
        counts[letter] = counts.get(letter, 0) + 1
    return counts
# ERROR DIARY T8:


# T9 — LeetCode 1 "Two Sum", from a BLANK PAGE. Return the two positions [i, j] (i < j) whose numbers add up to target.
# Exactly one answer exists. two_sum([2, 7, 11, 15], 9) -> [0, 1]     two_sum([3, 3], 6) -> [0, 1]
# Aim for O(n). Say the brute-force O(n^2) idea out loud first, then improve it.
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums): # i stores index and nums stores value thus ennumerate = index,value
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
# ERROR DIARY T9: need to repeat this


# T10 — Clean a list of IDs. Remove spaces at both ends, make UPPER CASE, drop the ones that are empty after cleaning,
# keep the order, and do not change the original list.
# clean_ids([" s01", "S02 ", "", "s03", "  "]) -> ["S01", "S02", "S03"]
def clean_ids(ids):
    result = []
    for raw in ids:
        cleaned = raw.strip().upper()
        if cleaned != "":
            result.append(cleaned)
    return result
# ERROR DIARY T10: no


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
    assert bmi_category(24.9) == "normal"
    assert bmi_category(25) == "overweight", "boundary: below 25 is normal, 25 itself is overweight"
    assert bmi_category(18.5) == "normal"
    assert bmi_category(17) == "underweight"
    assert bmi_category(35) == "obese"

def t2():
    assert count_over([70, 40, 66, 65], 65) == 2, "strictly above: 65 does not count"
    assert count_over([], 1) == 0

def t3():
    assert lowest([3.2, 1.5, 2.8]) == 1.5
    assert lowest([-4, -9, 0]) == -9, "start from the first value, not from 0"
    assert lowest([]) is None

def t4():
    assert count_letters("AATG") == {"A": 2, "T": 1, "G": 1}
    assert count_letters("") == {}

def t5():
    assert top_drug({"A": 10, "B": 5.5, "C": 7}) == "A"
    assert top_drug({"A": 1, "B": 9}) == "B"
    assert top_drug({"A": 5, "B": 5}) == "A", "a tie: the first one wins"
    assert top_drug({}) is None
    assert top_drug({"A": -3, "B": -8}) == "A", "all values negative"

def t6():
    assert unique_sorted(["Stroke", "Epilepsy", "Stroke"]) == ["Epilepsy", "Stroke"]
    assert unique_sorted([]) == []

def t7():
    r = [1, 2]
    assert add_reading(r, 3) == [1, 2, 3]
    assert r == [1, 2], "you changed the caller's list!"

def t8():
    assert tally("a") == {"a": 1}
    assert tally("a") == {"a": 1}, "mutable default trap: the old dictionary was reused"
    assert tally("b", {"a": 2}) == {"a": 2, "b": 1}

def t9():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]

def t10():
    original = [" s01", "S02 ", "", "s03", "  "]
    assert clean_ids(original) == ["S01", "S02", "S03"]
    assert original == [" s01", "S02 ", "", "s03", "  "], "you changed the caller's list!"
    assert clean_ids([]) == []


if __name__ == "__main__":
    results = [
        run_test("T1 bmi_category", t1),
        run_test("T2 count_over", t2),
        run_test("T3 lowest", t3),
        run_test("T4 count_letters", t4),
        run_test("T5 top_drug", t5),
        run_test("T6 unique_sorted", t6),
        run_test("T7 add_reading", t7),
        run_test("T8 tally (bug hunt)", t8),
        run_test("T9 two_sum (blank page)", t9),
        run_test("T10 clean_ids", t10),
    ]
    print(f"\n{sum(results)}/{len(results)} passed")


# ===========================================================================
# SEALED SOLUTIONS — open only after the 60-minute timer has rung
# ===========================================================================
#   def bmi_category(bmi):
#       if bmi < 18.5:
#           return "underweight"
#       elif bmi < 25:
#           return "normal"
#       elif bmi < 30:
#           return "overweight"
#       return "obese"
#
#   def count_over(values, limit):
#       count = 0
#       for v in values:
#           if v > limit:
#               count += 1
#       return count
#
#   def lowest(values):
#       if not values:
#           return None
#       best = values[0]
#       for v in values:
#           if v < best:
#               best = v
#       return best
#
#   def count_letters(seq):
#       counts = {}
#       for letter in seq:
#           counts[letter] = counts.get(letter, 0) + 1
#       return counts
#
#   def top_drug(doses):
#       best_name = None
#       best_mg = None
#       for name, mg in doses.items():
#           if best_mg is None or mg > best_mg:
#               best_name = name
#               best_mg = mg
#       return best_name
#
#   def unique_sorted(items):
#       return sorted(set(items))
#
#   def add_reading(readings, value):
#       return readings + [value]
#
#   def tally(word, counts=None):
#       if counts is None:
#           counts = {}
#       counts[word] = counts.get(word, 0) + 1
#       return counts
#
#   def two_sum(nums, target):
#       seen = {}
#       for i, n in enumerate(nums):
#           need = target - n
#           if need in seen:
#               return [seen[need], i]
#           seen[n] = i
#
#   def clean_ids(ids):
#       result = []
#       for raw in ids:
#           cleaned = raw.strip().upper()
#           if cleaned != "":
#               result.append(cleaned)
#       return result
#
#   Score guide: 9-10 = M1 is solid. 7-8 = redo the failed ones tomorrow from a blank page. Below 7 = we repeat the weakest topic on Monday.
