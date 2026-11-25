"""
UPSKILLER · DAY 10 · WARM-UP (10 min, CLOSED NOTEBOOK, no hints, no looking at old files)
Run:  python day10_warmup.py      Goal: 3/3
Why these three: you got `bump` wrong three times, two_sum was solved but not yet from memory, and in the mini-test
`tally` was changed to count letters. Type each one from a blank line. Say "before / inside / after the loop" out loud.
Rules: RETURN, don't print. Never edit the tests. If a test goes red, write the ERROR DIARY line BEFORE you fix it.
"""
import sys
import traceback

# W1 — Add 1 to counts[key] (create the key if it is missing). Change the dictionary IN PLACE and return it.
# bump({"A": 1}, "G") -> {"A": 1, "G": 1}
def bump(counts, key):
    if key in counts:
        counts[key] = counts.get(key, 0) + 1
    else:
        counts[key] = 1
    return counts
# ERROR DIARY W1: wrote for instead of if. worked when changed to if. 


# W2 — LeetCode 1 Two Sum. Return the two INDICES [i, j] (i < j) of the numbers that add up to target. One answer exists.
# two_sum([2, 7, 11, 15], 9) -> [0, 1]
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
# ERROR DIARY W2: do this again tomorrow. learn that dict will store the list and index if we use enumerate.


# W3 — Count a WORD (the whole word, not its letters). If counts is not given, start a NEW empty dictionary.
# tally("TP53") -> {"TP53": 1}      tally("TP53", {"TP53": 1}) -> {"TP53": 2}
# Two calls without a second argument must NOT share a dictionary.
def tally(word, counts=None):
    if counts is None:
        counts = {}
    counts[word] = counts.get(word, 0) + 1
    return counts
# ERROR DIARY W3: forgot to initialize the dictionary when counts is None.


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

def t_w1():
    d = {"A": 1}
    assert bump(d, "A") == {"A": 2}
    assert bump(d, "G") == {"A": 2, "G": 1}
    assert d == {"A": 2, "G": 1}, "the dictionary itself must change"
    e = {}
    assert bump(e, "x") == {"x": 1}
    assert bump(e, "x") == {"x": 2} and e == {"x": 2}

def t_w2():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 5, 9, 14, 20], 34) == [3, 4]
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def t_w3():
    assert tally("TP53") == {"TP53": 1}, "count the WHOLE word, not its letters"
    assert tally("TP53", {"TP53": 1}) == {"TP53": 2}
    c = {}
    tally("APP", c); tally("APP", c); tally("MAPT", c)
    assert c == {"APP": 2, "MAPT": 1}
    first = tally("a")
    second = tally("b")
    assert second == {"b": 1}, "two calls must not share one dictionary"
    assert first == {"a": 1}


if __name__ == "__main__":
    results = [
        run_test("W1 bump", t_w1),
        run_test("W2 two_sum", t_w2),
        run_test("W3 tally", t_w3),
    ]
    print(f"\n{sum(results)}/{len(results)} passed")


# ===================== SEALED SOLUTIONS — open only after the 10 minutes are over =====================
#   def bump(counts, key):
#       counts[key] = counts.get(key, 0) + 1
#       return counts
#
#   def two_sum(nums, target):
#       seen = {}
#       for i, num in enumerate(nums):
#           complement = target - num
#           if complement in seen:
#               return [seen[complement], i]
#           seen[num] = i
#
#   def tally(word, counts=None):
#       if counts is None:
#           counts = {}
#       counts[word] = counts.get(word, 0) + 1
#       return counts
#
#   W1 is the same line you have written since Monday 16 Nov: left of = counts[key], right of = counts.get(key, 0) + 1.
#   W2: a dictionary of number -> index seen so far; for each num ask "have I already seen target - num?"  O(n) time.
#   W3: the default is None, not {}, because a default dictionary is created ONCE and shared by every call.
