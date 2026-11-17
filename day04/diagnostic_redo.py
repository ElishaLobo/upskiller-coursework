"""
UPSKILLER · Sunday 15 Nov · 11:00–12:00 · Diagnostic redo (Part B)

Rewrite B1–B4 FROM SCRATCH. Don't copy the model answers from the chat:
close the chat, write each function, then run:
    python diagnostic_redo.py
Every function must PASS. Keep an error diary under each function like on Day 1.
"""
import sys
import traceback


# B1 — return True if age is 18 or more, else False. One line inside is enough.
def is_adult(age):
  if age > 18:
    return True
  else:
    return False        
# ERROR DIARY B1:


# B2 — how many lengths are GREATER THAN 1000 (1000 itself does NOT count)
def count_long_genes(lengths):
    count = 0
    if len(lengths) > 1000:
        count = count + 1
    return count
# ERROR DIARY B2:


# B3 — highest temperature WITHOUT max(). Must also work for negative numbers.
def highest(temps):
    highest_temp = temps[0]
    for temp in temps:
        if temp > highest_temp:
            highest_temp = temp
    return highest_temp
# ERROR DIARY B3:


# B4 — dictionary of how many times each letter appears: "AAG" -> {"A": 2, "G": 1}
def base_counts(seq):
    counts = {}
    for base in seq:
        if base in counts:
            counts[base] += 1
        else:
            counts[base] = 1
    return counts
# ERROR DIARY B4: additional solution using .get() method
#def base_counts(seq):
    counts = {}                                   # 1. empty dictionary
    for letter in seq:                            # 2. visit each letter
        counts[letter] = counts.get(letter, 0) + 1  # 3. add 1 to that letter's count
    return counts                                 # 4. hand back the dictionary


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
    assert is_adult(20) is True
    assert is_adult(18) is True
    assert is_adult(17) is False

def t2():
    assert count_long_genes([1, 200, 300, 46, 17]) == 0
    assert count_long_genes([81189, 1000, 19149, 3612, 999]) == 3
    assert count_long_genes([]) == 0

def t3():
    assert highest([36.6, 37.2, 39.1, 38.4]) == 39.1
    assert highest([-5.0, -2.5, -9.1]) == -2.5
    assert highest([40.0]) == 40.0

def t4():
    assert base_counts("AAG") == {"A": 2, "G": 1}
    assert base_counts("AATC") == {"A": 2, "T": 1, "C": 1}
    assert base_counts("") == {}

if __name__ == "__main__":
    tests = [("B1 is_adult", t1), ("B2 count_long_genes", t2),
             ("B3 highest", t3), ("B4 base_counts", t4)]
    passed = sum(run_test(n, f) for n, f in tests)
    print(f"\n{passed}/{len(tests)} passed")
