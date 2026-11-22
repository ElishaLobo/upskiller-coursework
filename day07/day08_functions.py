"""
UPSKILLER · DAY 08 · Functions in depth
Run:  python day08_functions.py      Goal: 7/7 (6 exercises + drill)
Rules: RETURN, don't print. Never edit the tests. ERROR DIARY under every function you had to fix.
"""
import sys
import traceback

# EX 1 — Default parameter. BMI = weight / height squared, rounded to 1 decimal. height_m defaults to 1.70.
# bmi(70) -> 24.2      bmi(70, 1.8) -> 21.6
def bmi(weight_kg, height_m=1.70):
    return round(weight_kg / height_m ** 2, 1)
# ERROR DIARY 1:


# EX 2 — Return THREE values as a tuple: (smallest, largest, mean rounded to 2 decimals). No min()/max()/sum().
# summarise([3.0, 1.0, 2.0]) -> (1.0, 3.0, 2.0)
def summarise(values):
    smallest = values[0]
    largest = values[0]
    total = 0
    for v in values:
        if v < smallest:
            smallest = v
        if v > largest:
            largest = v
        total += v
    mean = round(total / len(values), 2)
    return (smallest, largest, mean)
# ERROR DIARY 2:


# EX 3 — Keyword arguments. Label = prefix + number padded to `width` digits.
# make_label(7) -> "S007"     make_label(7, prefix="CTRL", width=2) -> "CTRL07"
def make_label(number, prefix="S", width=3):
    return f"{prefix}{number:0{width}d}"
# ERROR DIARY 3:


# EX 4 — Do NOT change the caller's list. Return a NEW list with the value added at the end.
# r = [1, 2]; add_copy(r, 3) -> [1, 2, 3] and r is still [1, 2]
def add_copy(readings, value):
    return readings + [value]
# ERROR DIARY 4:


# EX 5 — The mutable-default trap. Add item to `target` and return it; if no list is given, start a NEW empty one
# EVERY call. Default must be None, not [].
# collect("a") -> ["a"]    collect("b") -> ["b"]  (NOT ["a", "b"])    collect("c", ["x"]) -> ["x", "c"]
def collect(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
# ERROR DIARY 5:


# EX 6 — Two functions working together. count_status counts how many items equal `wanted`;
# percent_failed uses it: percent of "fail" in the list, rounded to 1 decimal, 0.0 for an empty list.
# percent_failed(["pass", "fail", "pass", "pass"]) -> 25.0
def count_status(items, wanted):
    count = 0
    for item in items:
        if item == wanted:
            count += 1
    return count

def percent_failed(items):
    failed_count = count_status(items, "fail")
    return round(failed_count / len(items) * 100, 1) if items else 0.0
# ERROR DIARY 6:


# DRILL — CODING (13 min) · LeetCode 387 "First Unique Character". Return the INDEX of the first character that
# appears exactly once in the string, or -1. first_unique("leetcode") -> 0   first_unique("aabb") -> -1
# first_unique("loveleetcode") -> 2
def first_unique(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return -1

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
    assert bmi(70) == 24.2
    assert bmi(70, 1.8) == 21.6
    assert bmi(weight_kg=70, height_m=1.8) == 21.6

def t2():
    assert summarise([3.0, 1.0, 2.0]) == (1.0, 3.0, 2.0)
    assert summarise([5.0]) == (5.0, 5.0, 5.0)

def t3():
    assert make_label(7) == "S007"
    assert make_label(7, prefix="CTRL", width=2) == "CTRL07"
    assert make_label(12, width=4) == "S0012"

def t4():
    r = [1, 2]
    assert add_copy(r, 3) == [1, 2, 3]
    assert r == [1, 2], "you changed the caller's list!"

def t5():
    assert collect("a") == ["a"]
    assert collect("b") == ["b"], "mutable default trap: the old list was reused"
    assert collect("c", ["x"]) == ["x", "c"]

def t6():
    assert count_status(["pass", "fail", "fail"], "fail") == 2
    assert percent_failed(["pass", "fail", "pass", "pass"]) == 25.0
    assert percent_failed([]) == 0.0

def t_drill():
    assert first_unique("leetcode") == 0
    assert first_unique("loveleetcode") == 2
    assert first_unique("aabb") == -1


if __name__ == "__main__":
    results = [
        run_test("Ex1 bmi", t1),
        run_test("Ex2 summarise", t2),
        run_test("Ex3 make_label", t3),
        run_test("Ex4 add_copy", t4),
        run_test("Ex5 collect", t5),
        run_test("Ex6 count_status + percent_failed", t6),
        run_test("DRILL first_unique", t_drill),
    ]
    print(f"\n{sum(results)}/{len(results)} passed")


# ===================== HINTS (try first, then read) =====================
# Ex1: def f(a, b=default). Parameters with a default are optional. Required ones come FIRST.
# Ex2: one loop, three accumulators: best-so-far x2 (low, high) and a running total. return (low, high, mean).
# Ex3: f-string with a nested width: f"{number:0{width}d}"  (the inner {width} is filled first).
# Ex4: list + list makes a NEW list. readings.append(...) would change the caller's list.
# Ex5: def f(item, target=None): if target is None: target = []. A default [] is created ONCE and shared by all calls.
# Ex6: write count_status first, test it alone, THEN call it inside percent_failed. Guard the empty list BEFORE dividing.
# Drill: pass 1 = counting dict over the string. pass 2 = enumerate again and return the first index whose count is 1.
#        return -1 AFTER the second loop.







# ===========================================================================
# SEALED SOLUTION — DRILL (open only after your 13 minutes)
# ===========================================================================
#   counts = {}
#   for ch in s:
#       counts[ch] = counts.get(ch, 0) + 1          # pass 1: count every character
#   for i, ch in enumerate(s):
#       if counts[ch] == 1:                          # pass 2: first one that is unique
#           return i
#   return -1                                        # AFTER the loop
#   Pattern: counting dict, then a second pass in the ORIGINAL order (dicts remember insertion order, but the
#   two-pass version is the one interviewers expect). Big-O: O(n) time, O(1) space for a fixed alphabet (O(k) in general).
#   Common wrong answers: returning the character instead of the index; returning -1 inside the second loop
#   (stops after the first character); using s.count(ch) in a loop (correct but O(n^2)).
