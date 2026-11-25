"""
UPSKILLER · DAY 10 · MODULE 2 · COMPREHENSIONS — exercises 2 + the coding drill
Run:  python day10_comprehensions.py      Goal: 9/9   (C1–C4 in Block 1 at 11:35, C5–C8 in Block 2, the drill at 12:05)
Rule of thumb: a comprehension is a loop that builds ONE new collection, written on one line.
    [what_to_keep  for item in source  if condition]      the "if" is optional
Rules: RETURN, don't print. Never edit the tests. If a comprehension gets hard to read, write the loop instead: readable beats short.
ERROR DIARY the minute a test goes red.
"""
import sys
import traceback

# C1 — squares(nums): a list with every number squared.   squares([1, 2, 3]) -> [1, 4, 9]
def squares(nums):
    return [n * n for n in nums]
# ERROR DIARY C1:


# C2 — adults(ages): only the ages that are 18 or more, same order.   adults([12, 18, 40, 5]) -> [18, 40]
def adults(ages):
    return [age for age in ages if age >= 18]
# ERROR DIARY C2:


# C3 — high_genes(expr, cutoff): the NAMES of the genes whose level is ABOVE the cutoff, in dictionary order.
# high_genes({"TP53": 2.0, "APP": 8.5, "MAPT": 6.1}, 5) -> ["APP", "MAPT"]      (expr.items() gives both name and level)
def high_genes(expr, cutoff):
   return [gene for gene, level in expr.items() if level > cutoff]
# ERROR DIARY C3:


# C4 — normalise_ids(ids): strip spaces and make UPPER CASE, one new list, the old list unchanged.
# normalise_ids([" p001", "p002 "]) -> ["P001", "P002"]
def normalise_ids(ids):
    return [i.strip().upper() for i in ids]
# ERROR DIARY C4:


# C5 — levels_by_gene(rows): rows is a list of (gene, level) tuples. Return a DICTIONARY {gene: level}.
# Dictionary comprehension:  {key: value for ... in ...}     If a gene appears twice, the LAST one wins (that is how dicts work).
# levels_by_gene([("APP", 8.5), ("TP53", 2.0)]) -> {"APP": 8.5, "TP53": 2.0}
def levels_by_gene(rows):
    return {gene: level for gene, level in rows}
# ERROR DIARY C5: how do you deal with dup,icates? the last one wins, that is how dicts work


# C6 — distinct_lengths(words): the set of different word lengths.   distinct_lengths(["APP", "TP53", "MAPT", "GBA"]) -> {3, 4}
# Set comprehension:  {expression for ... in ...}
def distinct_lengths(words):
    return {len(word) for word in words}
# ERROR DIARY C6: set comprehension keeps only distinct values, so the result is a set, not a list.


# C7 — weights_in_lb(weights_kg): convert each known weight to pounds (kg * 2.20462), rounded to 1 decimal; SKIP the None values.
# weights_in_lb([61.5, None, 82]) -> [135.6, 180.8]
def weights_in_lb(weights_kg):
    return [round(w*2.2046,1) for w in weights_kg if w is not None]
# ERROR DIARY C7:


# C8 — STRETCH. pairs(genes, groups): every gene with every group, as tuples, genes in the OUTER loop.
# pairs(["APP", "TP53"], ["case", "control"]) -> [("APP", "case"), ("APP", "control"), ("TP53", "case"), ("TP53", "control")]
# Two "for" parts in one comprehension, read left to right exactly like two nested loops.
def pairs(genes, groups):
    return [(gene, group) for gene in genes for group in groups]
    pass  # your code here
# ERROR DIARY C8:


# DRILL — CODING (13 min, timed) · LeetCode 217 "Contains Duplicate". Return True if any value appears at least twice.
# contains_duplicate([1, 2, 3, 1]) -> True      contains_duplicate([1, 2, 3, 4]) -> False      contains_duplicate([]) -> False
# Pattern: the SEEN-SET. before the loop: seen = set(). inside: if num is already in seen, return True; otherwise seen.add(num).
# after the loop: return False.  Do not change the input list.
def contains_duplicate(nums):
  seen =set ()
  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False
# ERROR DIARY DRILL:


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
    assert squares([1, 2, 3]) == [1, 4, 9]
    assert squares([]) == []
    assert squares([-3]) == [9]

def t2():
    assert adults([12, 18, 40, 5]) == [18, 40], "18 itself counts"
    assert adults([1, 2]) == []

def t3():
    assert high_genes({"TP53": 2.0, "APP": 8.5, "MAPT": 6.1}, 5) == ["APP", "MAPT"]
    assert high_genes({"A": 5}, 5) == [], "ABOVE the cutoff, not equal to it"
    assert high_genes({}, 1) == []

def t4():
    original = [" p001", "p002 "]
    assert normalise_ids(original) == ["P001", "P002"]
    assert original == [" p001", "p002 "], "the old list must stay unchanged"

def t5():
    assert levels_by_gene([("APP", 8.5), ("TP53", 2.0)]) == {"APP": 8.5, "TP53": 2.0}
    assert levels_by_gene([("APP", 1), ("APP", 2)]) == {"APP": 2}
    assert levels_by_gene([]) == {}

def t6():
    assert distinct_lengths(["APP", "TP53", "MAPT", "GBA"]) == {3, 4}
    assert distinct_lengths([]) == set()
    assert isinstance(distinct_lengths(["a"]), set)

def t7():
    assert weights_in_lb([61.5, None, 82]) == [135.6, 180.8]
    assert weights_in_lb([None]) == []
    assert weights_in_lb([0]) == [0.0], "0 is a real weight here; only None is skipped"

def t8():
    assert pairs(["APP", "TP53"], ["case", "control"]) == [("APP", "case"), ("APP", "control"), ("TP53", "case"), ("TP53", "control")]
    assert pairs([], ["x"]) == []
    assert pairs(["x"], []) == []

def t_drill():
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([]) is False
    assert contains_duplicate(["a", "b", "a"]) is True
    data = [3, 1, 3]
    contains_duplicate(data)
    assert data == [3, 1, 3], "do not change the input list"


if __name__ == "__main__":
    results = [
        run_test("C1 squares", t1),
        run_test("C2 adults", t2),
        run_test("C3 high_genes", t3),
        run_test("C4 normalise_ids", t4),
        run_test("C5 levels_by_gene", t5),
        run_test("C6 distinct_lengths", t6),
        run_test("C7 weights_in_lb", t7),
        run_test("C8 pairs (stretch)", t8),
        run_test("DRILL contains_duplicate", t_drill),
    ]
    print(f"\n{sum(results)}/{len(results)} passed")


# ===================== HINTS (try first, then read) =====================
# Read every comprehension as a sentence: "give me n*n FOR each n IN nums".
# C3: [gene for gene, level in expr.items() if level > cutoff]  -- the loop line is the same as in describe() on Sunday.
# C5: curly brackets with a colon inside. C6: curly brackets WITHOUT a colon. Empty {} is a dict, so the empty set is set().
# C7: filter first (the `if` at the end), then compute. `if w` would also skip 0, so compare with None.
# Drill: before the loop: seen = set(). inside: an if with return True, then seen.add(num). after: return False.
#
#
#
# ===========================================================================
# SEALED SOLUTIONS — open only after your 13 minutes on the drill
# ===========================================================================
#   def squares(nums):
#       return [n * n for n in nums]
#
#   def adults(ages):
#       return [age for age in ages if age >= 18]
#
#   def high_genes(expr, cutoff):
#       return [gene for gene, level in expr.items() if level > cutoff]
#
#   def normalise_ids(ids):
#       return [i.strip().upper() for i in ids]
#
#   def levels_by_gene(rows):
#       return {gene: level for gene, level in rows}
#
#   def distinct_lengths(words):
#       return {len(word) for word in words}
#
#   def weights_in_lb(weights_kg):
#       return [round(w * 2.20462, 1) for w in weights_kg if w is not None]
#
#   def pairs(genes, groups):
#       return [(gene, group) for gene in genes for group in groups]
#
#   def contains_duplicate(nums):
#       seen = set()
#       for num in nums:
#           if num in seen:
#               return True
#           seen.add(num)
#       return False
#
#   Drill: O(n) time, O(n) space. Brute force (compare every pair) is O(n^2): say that first, then improve it.
#   The one-liner  len(set(nums)) != len(nums)  is correct too, but it always builds the whole set; the loop stops at the first repeat.
