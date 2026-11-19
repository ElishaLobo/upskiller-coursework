"""
UPSKILLER · DAY 05 · Block 1b · The three patterns, NEW problems
(Do diagnostic_redo.py B1/B2/B4 FIRST, from memory, until 4/4.)

These are the same three patterns in new situations, so memorising Monday's
answers won't help. Close the chat and the notebook before you start.

    COUNTER            count = 0          ... if condition: count = count + 1
    BEST SO FAR        best = items[0]    ... if item < best: best = item
    COUNTING DICT      counts = {}        ... counts[x] = counts.get(x, 0) + 1

Run:  python day05_patterns.py      Goal: 3/3.  Fill every ERROR DIARY (4 parts).
A hand-in without diaries counts as incomplete from today.
"""
import sys
import traceback


# P1 — COUNTER: how many temperatures are fevers (38.0 or more)?
# count_fevers([36.6, 38.0, 39.2, 37.9]) -> 2
def count_fevers(temps):
    hightemp = 0
    for temp in temps:
        if temp >= 38.0:
            hightemp += 1
    return hightemp 
# ERROR DIARY P1 (error / line / meaning / fix):


# P2 — BEST SO FAR: lowest concentration, WITHOUT min().
# lowest_conc([45.2, 8.7, 61.0, 5.1]) -> 5.1
def lowest_conc(concs):
    lowest = concs[0]
    for conc in concs:
        if conc < lowest:
            lowest = conc
    return lowest
# ERROR DIARY P2:


# P3 — COUNTING DICT: how many patients per diagnosis.
# diagnosis_counts(["Stroke", "Epilepsy", "Stroke"]) -> {"Stroke": 2, "Epilepsy": 1}
def diagnosis_counts(diagnoses):
    counts = {}
    for diagnosis in diagnoses:
        counts[diagnosis] = counts.get(diagnosis, 0) + 1
    return counts
# ERROR DIARY P3:


# ===================== TESTS — do not edit =====================
def run_test(name, fn):
    try:
        fn()
        print(f"PASS  {name}")
        return True
    except Exception:
        print(f"FAIL  {name}")
        traceback.print_exc(file=sys.stdout)
        print()
        return False

def t1():
    assert count_fevers([36.6, 38.0, 39.2, 37.9]) == 2
    assert count_fevers([]) == 0
    assert count_fevers([40.1, 40.1]) == 2

def t2():
    assert lowest_conc([45.2, 8.7, 61.0, 5.1]) == 5.1
    assert lowest_conc([3.0]) == 3.0
    assert lowest_conc([-1.0, -4.5, 2.0]) == -4.5

def t3():
    assert diagnosis_counts(["Stroke", "Epilepsy", "Stroke"]) == {"Stroke": 2, "Epilepsy": 1}
    assert diagnosis_counts([]) == {}
    assert diagnosis_counts(["Migraine"]) == {"Migraine": 1}

if __name__ == "__main__":
    tests = [("P1 count_fevers", t1), ("P2 lowest_conc", t2), ("P3 diagnosis_counts", t3)]
    passed = sum(run_test(n, f) for n, f in tests)
    print(f"\n{passed}/{len(tests)} passed")
