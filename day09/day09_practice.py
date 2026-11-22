"""
UPSKILLER · DAY 09 · REDO of Friday's mistakes + the daily coding drill
Run:  python day09_practice.py      Goal: 4/4
Rules: RETURN, don't print. Never edit the tests. ERROR DIARY under every function you had to fix.
These three redo tasks are the three things you got wrong on Friday's check-yourself. Type each from a blank line.
"""
import sys
import traceback

# R1 — Friday Q2. Add 1 to counts[key], even if key is not in the dictionary yet. Change the dictionary IN PLACE and return it.
# Write the ONE line that does the work. It has a .get( ... ) in it and square brackets on BOTH sides of the =.
# d = {"A": 1}; bump(d, "A") -> {"A": 2}     bump(d, "G") -> {"A": 2, "G": 1}
def bump(counts, key):
    for letters in counts:
        if letters == key:
            counts[key] = counts.get(key, 0) + 1
    return counts
# ERROR DIARY R1:


# R2 — Friday Q3. Return a list of "gene=level" strings, one per entry, in dictionary order.
# Use the loop line that gives you BOTH the gene and its level. Remember: a method needs brackets to run.
# describe({"TP53": 2.0, "APP": 8.5}) -> ["TP53=2.0", "APP=8.5"]      describe({}) -> []
def describe(expr):
    result = []
    for gene, level in expr.items():
        result.append(f"{gene}={level}") # learn this line again, it is a common pattern to build a list of strings from a dictionary.
    return result
# ERROR DIARY R2:


# R3 — Friday Q4 (sets). How many DIFFERENT items appear in BOTH lists? Use sets.
# common_count(["TP53", "APP", "APP"], ["APP", "MAPT", "TP53"]) -> 2      common_count(["A"], ["B"]) -> 0
def common_count(list_a, list_b):
    return len(set(list_a) & set(list_b))
# ERROR DIARY R3:


# DRILL — CODING (13 min) · LeetCode 121 "Best Time to Buy and Sell Stock". prices[i] is the price on day i.
# Buy on one day, sell on a LATER day. Return the biggest profit, or 0 if no profit is possible.
# max_profit([7, 1, 5, 3, 6, 4]) -> 5   (buy at 1, sell at 6)      max_profit([7, 6, 4, 3, 1]) -> 0      max_profit([]) -> 0
# Pattern: TWO best-so-far variables in one loop: the lowest price seen so far, and the best profit so far.
def max_profit(prices):
    lowest = None
    profit = 0
    for price in prices:
        if lowest is None or price < lowest:
            lowest = price
        elif price - lowest > profit:
            profit = price - lowest
    return profit
    return best
   
# ERROR DIARY DRILL: redo this, understand the logic, and write it out in your own words. 


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

def t_r1():
    d = {"A": 1}
    assert bump(d, "A") == {"A": 2}
    assert bump(d, "G") == {"A": 2, "G": 1}
    assert d == {"A": 2, "G": 1}, "the dictionary itself must change"

def t_r2():
    assert describe({"TP53": 2.0, "APP": 8.5}) == ["TP53=2.0", "APP=8.5"]
    assert describe({}) == []

def t_r3():
    assert common_count(["TP53", "APP", "APP"], ["APP", "MAPT", "TP53"]) == 2, "count DIFFERENT items: APP once"
    assert common_count(["A"], ["B"]) == 0
    assert common_count([], []) == 0

def t_drill():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([]) == 0
    assert max_profit([2, 4, 1]) == 2, "you must sell AFTER you buy: 1 then 4 is not allowed"
    assert max_profit([3]) == 0


if __name__ == "__main__":
    results = [
        run_test("R1 bump", t_r1),
        run_test("R2 describe", t_r2),
        run_test("R3 common_count", t_r3),
        run_test("DRILL max_profit", t_drill),
    ]
    print(f"\n{sum(results)}/{len(results)} passed")


# ===================== HINTS (try first, then read) =====================
# R1: left of =  counts[key]     right of =  counts.get(key, 0) + 1   Same line you have written since Monday, with different names.
# R2: for gene, level in expr.items():     <- note the () after items. Build the text with an f-string: f"{gene}={level}"
# R3: set(a) & set(b) is "in both"; len() counts them.
# Drill: before the loop: lowest = None, best = 0. Inside: if this price is a new low, update lowest; otherwise check
#        price - lowest against best. Return best AFTER the loop.
#
#
#
# ===========================================================================
# SEALED SOLUTIONS — open only after your 13 minutes on the drill
# ===========================================================================
#   def bump(counts, key):
#       counts[key] = counts.get(key, 0) + 1
#       return counts
#
#   def describe(expr):
#       result = []
#       for gene, level in expr.items():
#           result.append(f"{gene}={level}")
#       return result
#
#   def common_count(list_a, list_b):
#       return len(set(list_a) & set(list_b))
#
#   def max_profit(prices):
#       lowest = None
#       best = 0
#       for price in prices:
#           if lowest is None or price < lowest:
#               lowest = price
#           elif price - lowest > best:
#               best = price - lowest
#       return best
#
#   Drill: O(n) time, O(1) space. Brute force (every buy day against every sell day) is O(n^2): say that first, then improve it.
#   Common wrong answers: max(prices) - min(prices) (the sell day can come BEFORE the buy day); returning a negative number
#   instead of 0; forgetting the empty list.
