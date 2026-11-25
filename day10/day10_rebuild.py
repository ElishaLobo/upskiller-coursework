"""
UPSKILLER · DAY 10 · REBUILD (Block 2, 20 min) — the pipeline pattern on NEW data, from a blank page
Run:  python day10_rebuild.py      Goal: 2/2
On Sunday your cleaner passed 9/9, but steps 4, 7, 8, 9 matched the sealed solutions. Today the same two patterns come back on
lab samples with different names, so there is nothing to copy. Do NOT open day09_cleaner.py. Write both functions yourself.
Story: expression samples from a lab. Each sample is a dictionary: "sample" (an id typed by hand), "gene", "level" (a number or None),
"group" ("case" or "control").
Rules: RETURN, don't print. Never edit the tests. ERROR DIARY the minute a test goes red.
"""
import sys
import traceback

# GIVEN (works, do not change): remove_duplicates keeps the FIRST record for each "sample" id.
def remove_duplicates(records):
    seen = set()
    result = []
    for record in records:
        if record["sample"] not in seen:
            seen.add(record["sample"])
            result.append(record)
    return result
# GIVEN (works, do not change): clean ONE raw sample into a NEW dictionary.
def clean_sample(raw):
    return {
        "sample": raw["sample"].strip().upper(),
        "gene": raw["gene"].strip().upper(),
        "level": raw["level"],
        "group": raw["group"].strip().lower(),
    }

# R1 — clean_all_samples(raw_samples): clean every sample with clean_sample, THEN remove duplicates, return the list.
# " s1" and "S1" are the same sample, but only after cleaning. That is why the ORDER matters. Never change raw_samples.
def clean_all_samples(raw_samples):
    cleaned = []
    for raw in raw_samples:
        cleaned.append(clean_sample(raw))
    return remove_duplicates(cleaned)
# ERROR DIARY R1:


# R2 — summarise_samples(samples): samples are ALREADY clean. Return ONE dictionary with:
#   "n"              how many samples
#   "missing_level"  how many have level None
#   "by_group"       a counting dictionary, e.g. {"case": 2, "control": 1}
#   "mean_level"     the mean of the KNOWN levels, rounded to 1 decimal; None if there are none
#   "genes"          the different genes as a SORTED list
# One loop, four accumulators: a counter, a counting dict, a total + a count, a set. Say before / inside / after out loud.
def summarise_samples(samples):
    n = 0
    missing_level = 0
    by_group = {}
    mean_level = 0
    total_level = 0
    count_level = 0
    genes = set()

    for sample in samples:
        n += 1
        genes.add(sample["gene"])

        if sample["level"] is None:
            missing_level += 1
        else:
            total_level += sample["level"]
            count_level += 1

        group = sample["group"] # assign value from sample["group"] to variable group
        by_group[group] = by_group.get(group, 0) + 1

    if count_level > 0:
        mean_level = round(total_level / count_level, 1)
    else:
        mean_level = None

    return {
        "n": n,
        "missing_level": missing_level,
        "by_group": by_group,
        "mean_level": mean_level,
        "genes": sorted(genes)
    }
# ERROR DIARY R2:


# ===================== TESTS — do not edit =====================
RAW = [
    {"sample": " s1", "gene": "app ",  "level": 8.5,  "group": "Case"},
    {"sample": "S2",  "gene": "TP53",  "level": 2.0,  "group": "control "},
    {"sample": "s1",  "gene": "APP",   "level": 8.5,  "group": "case"},
    {"sample": "S3",  "gene": "MAPT",  "level": None, "group": "CASE"},
    {"sample": "s4 ", "gene": "app",   "level": 3.0,  "group": "Control"},
]

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
    import copy
    before = copy.deepcopy(RAW)
    out = clean_all_samples(RAW)
    assert RAW == before, "never change the raw data"
    assert [s["sample"] for s in out] == ["S1", "S2", "S3", "S4"], "clean FIRST, then remove duplicates"
    assert out[0] == {"sample": "S1", "gene": "APP", "level": 8.5, "group": "case"}
    assert clean_all_samples([]) == []

def t_r2():
    out = summarise_samples(clean_all_samples(RAW))
    assert out == {"n": 4, "missing_level": 1, "by_group": {"case": 2, "control": 2},
                   "mean_level": 4.5, "genes": ["APP", "MAPT", "TP53"]}, out
    empty = summarise_samples([])
    assert empty == {"n": 0, "missing_level": 0, "by_group": {}, "mean_level": None, "genes": []}, empty
    only_none = summarise_samples([{"sample": "S1", "gene": "X", "level": None, "group": "case"}])
    assert only_none["mean_level"] is None and only_none["missing_level"] == 1


if __name__ == "__main__":
    results = [
        run_test("R1 clean_all_samples", t_r1),
        run_test("R2 summarise_samples", t_r2),
    ]
    print(f"\n{sum(results)}/{len(results)} passed")


# ===================== HINTS (only after 10 honest minutes) =====================
# R1: before the loop: cleaned = []   inside: cleaned.append(clean_sample(raw))   after: return remove_duplicates(cleaned)
# R2: before: counter, empty dict, total = 0, known = 0, empty set.  inside: one if/else for level, one .get line, one .add.
#     after: the ternary  round(total / known, 1) if known else None  -- why is the "if known" needed? (division by zero)
