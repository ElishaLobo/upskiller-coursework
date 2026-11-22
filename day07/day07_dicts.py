"""
UPSKILLER · DAY 07 · Dictionaries and sets
Run:  python day07_dicts.py      Goal: 8/8 (6 exercises + 2 drills)
Rules: RETURN, don't print. Never edit the tests. ERROR DIARY under every function you had to fix:
   (1) the error message  (2) the line  (3) what it meant in plain words  (4) the fix.
Hints at the bottom, then the sealed drill solutions. Write "before / inside / after the loop" in your head.
"""
import sys
import traceback

# EX 1 — Look up a gene's chromosome in a dictionary. If the gene is not there, return "unknown".
# chrom({"TP53": "17", "APP": "21"}, "APP") -> "21"     chrom({"TP53": "17"}, "BRCA1") -> "unknown"
def chrom(chrom, gene):
        return chrom.get(gene, "unknown")
# ERROR DIARY 1:
#no error

# EX 2 — Add or update a gene in the dictionary IN PLACE, then return how many genes it holds now.
# d = {"TP53": 5}; set_level(d, "APP", 9) -> 2 and d == {"TP53": 5, "APP": 9}; setting an existing key replaces its value.
def set_level(d, gene, level):
    d[gene] = level
    return len(d)
   
# ERROR DIARY 2:


# EX 3 — Total dose in mg. The dictionary maps drug name -> mg. Loop over the VALUES (no sum() allowed).
# total_dose({"A": 10, "B": 5.5}) -> 15.5      total_dose({}) -> 0
def total_dose(doses):
    total = 0
    for mg in doses.values():
        total += mg
    return total
    
# ERROR DIARY 3:


# EX 4 — Genes whose expression is AT LEAST the cutoff, as a SORTED list of names. Loop with .items().
# high_expression({"TP53": 2.0, "APP": 8.5, "TREM2": 9.1}, 8.5) -> ["APP", "TREM2"]
def high_expression(expr, cutoff):
    result = []
    for gene, level in expr.items():
        if level >= cutoff:
            result.append(gene)
    return sorted(result)

# ERROR DIARY 4:


# EX 5 — How many DIFFERENT diagnoses are in the list? Use a set.
# distinct_count(["Stroke", "Epilepsy", "Stroke"]) -> 2
def distinct_count(diagnoses):
    return len(set(diagnoses))
# ERROR DIARY 5:


# EX 6 — Genes found in BOTH lists, as a sorted list. Use set intersection (&).
# shared_genes(["TP53", "APP", "MAPT"], ["MAPT", "TP53", "SNCA"]) -> ["MAPT", "TP53"]
def shared_genes(list_a, list_b):
    return sorted(set(list_a) & set(list_b))
# ERROR DIARY 6:


# DRILL A — CODING (13 min) · LeetCode 217 again, now O(n): Contains Duplicate with a SET.
# contains_duplicate(["S01", "S02", "S01"]) -> True
def contains_duplicate(ids):
    seen = set()
    for sample_id in ids:
        if sample_id in seen:
            return True
        seen.add(sample_id)
    return False

# DRILL B — CODING (13 min) · LeetCode 1 "Two Sum". Return the two positions [i, j] (i < j) whose numbers add up to the target.
# Exactly one answer exists. two_sum([2, 7, 11, 15], 9) -> [0, 1]     two_sum([3, 2, 4], 6) -> [1, 2]
def two_sum(nums, target):
    seen = {}  # value -> position
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i

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
    assert chrom({"TP53": "17", "APP": "21"}, "APP") == "21"
    assert chrom({"TP53": "17"}, "BRCA1") == "unknown"
    assert chrom({}, "X") == "unknown"

def t2():
    d = {"TP53": 5}
    assert set_level(d, "APP", 9) == 2
    assert d == {"TP53": 5, "APP": 9}, "the dictionary itself must change"
    assert set_level(d, "APP", 1) == 2
    assert d["APP"] == 1, "setting an existing key should replace its value"

def t3():
    assert total_dose({"A": 10, "B": 5.5}) == 15.5
    assert total_dose({}) == 0

def t4():
    e = {"TP53": 2.0, "APP": 8.5, "TREM2": 9.1}
    assert high_expression(e, 8.5) == ["APP", "TREM2"], "boundary: AT LEAST means >="
    assert high_expression(e, 100) == []
    assert high_expression({}, 1) == []

def t5():
    assert distinct_count(["Stroke", "Epilepsy", "Stroke"]) == 2
    assert distinct_count([]) == 0

def t6():
    assert shared_genes(["TP53", "APP", "MAPT"], ["MAPT", "TP53", "SNCA"]) == ["MAPT", "TP53"]
    assert shared_genes(["A"], ["B"]) == []

def t_drill_a():
    assert contains_duplicate(["S01", "S02", "S01"]) is True
    assert contains_duplicate(["S01", "S02"]) is False
    assert contains_duplicate([]) is False

def t_drill_b():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


if __name__ == "__main__":
    results = [
        run_test("Ex1 chrom", t1),
        run_test("Ex2 set_level", t2),
        run_test("Ex3 total_dose", t3),
        run_test("Ex4 high_expression", t4),
        run_test("Ex5 distinct_count", t5),
        run_test("Ex6 shared_genes", t6),
        run_test("DRILL A contains_duplicate (set)", t_drill_a),
        run_test("DRILL B two_sum", t_drill_b),
    ]
    print(f"\n{sum(results)}/{len(results)} passed")


# ===================== HINTS (try first, then read) =====================
# Ex1: d.get(key, default) never crashes; d[key] raises KeyError when the key is missing.
# Ex2: d[key] = value adds OR replaces. Do NOT write return d.update(...) style tricks; set, then return len(d).
# Ex3: for mg in doses.values():  -> COUNTER pattern but adding the value instead of 1.
# Ex4: for gene, level in expr.items():  (two names, like zip/enumerate). Collect names, THEN sort after the loop.
# Ex5: set(list) removes duplicates; len() counts what is left.
# Ex6: set(a) & set(b) = in both. Sets have no order, so sorted() at the end.
# Drill A: same as Tuesday but seen = set() and seen.add(x). `x in seen` on a set is O(1).
# Drill B: for each number ask "have I already seen the number I NEED (target - n)?" The dictionary remembers value -> position.







# ===========================================================================
# SEALED SOLUTIONS — open only after your 13 minutes are up
# ===========================================================================
# DRILL A (LC 217, O(n)):
#   seen = set()
#   for sample_id in ids:
#       if sample_id in seen: return True
#       seen.add(sample_id)
#   return False
#   Pattern: "seen so far" with a SET. Big-O: O(n) time, O(n) space. Tuesday's list version was O(n^2).
#   Common wrong answer: len(set(ids)) == len(ids) reversed (== instead of !=) -> returns the opposite.
#
# DRILL B (LC 1 Two Sum, O(n)):
#   seen = {}                           # value -> position
#   for i, n in enumerate(nums):
#       need = target - n
#       if need in seen: return [seen[need], i]
#       seen[n] = i
#   Pattern: "complement lookup" with a dictionary. Big-O: O(n) time, O(n) space.
#   Brute force (two nested loops) is O(n^2): say it out loud in an interview, then improve it.
#   Common wrong answers: storing seen[n] = i BEFORE checking (matches a number with itself: [3] target 6),
#   and returning the values instead of the positions.
