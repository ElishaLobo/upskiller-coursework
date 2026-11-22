"""
UPSKILLER · DAY 09 · PROJECT LAB 1 · THE CLINICAL DATA CLEANER   (3 hours, your first portfolio piece)
Run:  python day09_cleaner.py      Goal: 9/9
Story: a ward gives you a messy patient list typed by hand: stray spaces, "male" and "M" and "?", weights written as
"61.5 kg" or "64,8", ages that are empty or impossible, and the same patient entered twice. Real hospital data looks
like this. Build small functions that each do ONE job, then chain them into a pipeline and a summary report.
Rules: RETURN, don't print. Never edit the tests or the RAW data. One function, one job. ERROR DIARY under every
function you had to fix. Write the functions in the order they appear: each one is tested alone before the next.
"""
import sys
import traceback

# The messy input. A list of dictionaries, one per patient. Do not change it.
RAW = [
    {"id": " p001", "age": "67",  "sex": "F",      "diagnosis": "alzheimer's disease", "weight": "61.5 kg"},
    {"id": "P002",  "age": "54 ", "sex": "male",   "diagnosis": "EPILEPSY",            "weight": "82"},
    {"id": "P003",  "age": "",    "sex": "M",      "diagnosis": "Parkinson's disease", "weight": "77.25kg"},
    {"id": "p001",  "age": "67",  "sex": "f",      "diagnosis": "Alzheimer's Disease", "weight": "61.5"},
    {"id": "P004",  "age": "abc", "sex": "Female", "diagnosis": "Migraine",            "weight": "58"},
    {"id": "P005",  "age": "38",  "sex": "?",      "diagnosis": "  multiple sclerosis", "weight": "64,8"},
    {"id": "P006",  "age": "59",  "sex": "M ",     "diagnosis": "Stroke",              "weight": ""},
    {"id": "P007",  "age": "250", "sex": "F",      "diagnosis": "stroke",              "weight": "55.1"},
]

# STEP 1 — clean_id(raw): remove spaces at both ends and make it UPPER CASE.   " p001" -> "P001"
def clean_id(raw):
    return raw.strip().upper()
# ERROR DIARY 1:


# STEP 2 — clean_sex(raw): return "F", "M" or "unknown". Accept f / female / m / male in any case and with stray spaces.
# Use a DICTIONARY lookup with .get() and a default, not a chain of ifs.   "female " -> "F"   " Male" -> "M"   "?" -> "unknown"   "" -> "unknown"
def clean_sex(raw):
    sex_map = {
        "f": "F",
        "female": "F",
        "m": "M",
        "male": "M"
    }
    return sex_map.get(raw.strip().lower(), "unknown")
# ERROR DIARY 2:


# STEP 3 — clean_age(raw): return the age as an int, or None if it is empty, not a whole number, or outside 1 to 120.
# "54 " -> 54     "" -> None     "abc" -> None     "250" -> None     "-5" -> None
def clean_age(raw):
    cleaned = raw.strip()
    if not cleaned:
        return None
    try:
        age = int(cleaned)
        if 1 <= age <= 120:
            return age
    except ValueError:
        pass
    return None
# ERROR DIARY 3:


# STEP 4 — clean_weight(raw): return the weight in kg as a float, or None if there is no usable number.
# Remove "kg" (any case), turn a decimal comma into a point, strip spaces.   "61.5 kg" -> 61.5   "64,8" -> 64.8   "82" -> 82.0   "" -> None   "heavy" -> None
# Hint for "is this a number?":  text.replace(".", "", 1).isdigit()   (the replace lets ONE decimal point through)
def clean_weight(raw):
    text = raw.lower().replace("kg", "").replace(",", ".").strip()
    if text.replace(".", "", 1).isdigit(): # explain this line.
        return float(text)
    return None
# ERROR DIARY 4:


# STEP 5 — clean_diagnosis(raw): strip spaces, first letter capital, the rest lower case.   "  multiple sclerosis" -> "Multiple sclerosis"   "EPILEPSY" -> "Epilepsy"
def clean_diagnosis(raw):
    return raw.strip().capitalize()
# ERROR DIARY 5:


# STEP 6 — clean_record(raw_record): return a NEW dictionary with the keys "id", "age", "sex", "diagnosis", "weight_kg",
# each made by the matching clean_ function. Do NOT change raw_record (the raw key is "weight", the new key is "weight_kg").
def clean_record(raw_record):
    new_record = {}
    new_record["id"] = clean_id(raw_record["id"])
    new_record["age"] = clean_age(raw_record["age"])
    new_record["sex"] = clean_sex(raw_record["sex"])
    new_record["diagnosis"] = clean_diagnosis(raw_record["diagnosis"])
    new_record["weight_kg"] = clean_weight(raw_record["weight"])
    return new_record 

# ERROR DIARY 6:


# STEP 7 — remove_duplicates(records): keep the FIRST record for each "id", in the original order. Use a set of ids seen so far
# (the pattern from Friday's contains_duplicate).
def remove_duplicates(records):
    seen = set()
    result = []
    for record in records: #itirate through each record(keys) in the input list
        if record["id"] not in seen:
            seen.add(record["id"]) # keep track of ids (values) we've seen
            result.append(record) # add the record to the result list
    return result
# ERROR DIARY 7:


# STEP 8 — clean_all(raw_records): clean every record, THEN remove duplicates, and return the list. Use your own functions from steps 6 and 7.
# (The two P001 rows only look different until they are cleaned. That is why the order matters.)
def clean_all(raw_records):
    cleaned = []
    for raw_record in raw_records:
        cleaned.append(clean_record(raw_record)) # appends entire cleaned record dictionary to the cleaned as list in 0 position
    return remove_duplicates(cleaned)
# ERROR DIARY 8:


# STEP 9 — summary(records): return ONE dictionary with:
#   "n"               how many records
#   "missing_age"     how many have age None
#   "missing_weight"  how many have weight_kg None
#   "by_sex"          a counting dictionary, e.g. {"F": 3, "M": 3, "unknown": 1}
#   "mean_age"        the mean of the KNOWN ages, rounded to 1 decimal; None if there are no known ages
#   "diagnoses"       the different diagnoses as a SORTED list
# One loop, several accumulators (counters, a counting dict, a running total, a set). Say before / inside / after the loop out loud.
def summary(records):
    missing_age = 0
    missing_weight = 0
    by_sex = {}
    age_total = 0
    age_count = 0
    diagnoses = set()

    for record in records:
        if record["age"] is None:
            missing_age += 1
        else:
            age_total += record["age"]
            age_count += 1

        if record["weight_kg"] is None:
            missing_weight += 1

        by_sex[record["sex"]] = by_sex.get(record["sex"], 0) + 1
        diagnoses.add(record["diagnosis"])

    mean_age = round(age_total / age_count, 1) if age_count else None

    return {
        "n": len(records),
        "missing_age": missing_age,
        "missing_weight": missing_weight,
        "by_sex": by_sex,
        "mean_age": mean_age,
        "diagnoses": sorted(diagnoses),
    }
# ERROR DIARY 9:


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
    assert clean_id(" p001") == "P001"
    assert clean_id("P002") == "P002"
    assert clean_id("  p9  ") == "P9"

def t2():
    assert clean_sex("F") == "F"
    assert clean_sex("female ") == "F"
    assert clean_sex(" Male") == "M"
    assert clean_sex("m") == "M"
    assert clean_sex("?") == "unknown"
    assert clean_sex("") == "unknown"

def t3():
    assert clean_age("54 ") == 54
    assert clean_age("67") == 67
    assert clean_age("") is None
    assert clean_age("abc") is None
    assert clean_age("250") is None, "impossible age"
    assert clean_age("-5") is None
    assert clean_age("0") is None, "0 is outside 1 to 120"

def t4():
    assert clean_weight("61.5 kg") == 61.5
    assert clean_weight("77.25kg") == 77.25
    assert clean_weight("64,8") == 64.8
    assert clean_weight("82") == 82.0
    assert clean_weight("82 KG") == 82.0
    assert clean_weight("") is None
    assert clean_weight("heavy") is None

def t5():
    assert clean_diagnosis("  multiple sclerosis") == "Multiple sclerosis"
    assert clean_diagnosis("EPILEPSY") == "Epilepsy"
    assert clean_diagnosis("Parkinson's disease") == "Parkinson's disease"

def t6():
    raw = {"id": " p005", "age": "38", "sex": "?", "diagnosis": "  multiple sclerosis", "weight": "64,8"}
    before = dict(raw)
    assert clean_record(raw) == {"id": "P005", "age": 38, "sex": "unknown",
                                 "diagnosis": "Multiple sclerosis", "weight_kg": 64.8}
    assert raw == before, "you changed the raw record!"

def t7():
    recs = [{"id": "A", "n": 1}, {"id": "B", "n": 2}, {"id": "A", "n": 3}]
    assert remove_duplicates(recs) == [{"id": "A", "n": 1}, {"id": "B", "n": 2}], "keep the FIRST, in order"
    assert remove_duplicates([]) == []

def t8():
    before = [dict(r) for r in RAW]
    out = clean_all(RAW)
    assert [r["id"] for r in out] == ["P001", "P002", "P003", "P004", "P005", "P006", "P007"]
    assert out[0] == {"id": "P001", "age": 67, "sex": "F", "diagnosis": "Alzheimer's disease", "weight_kg": 61.5}
    assert out[5]["weight_kg"] is None
    assert out[6]["age"] is None
    assert RAW == before, "RAW must not change"

def t9():
    s = summary(clean_all(RAW))
    assert s["n"] == 7
    assert s["missing_age"] == 3
    assert s["missing_weight"] == 1
    assert s["by_sex"] == {"F": 3, "M": 3, "unknown": 1}
    assert s["mean_age"] == 54.5, "mean of the KNOWN ages 67, 54, 38, 59"
    assert s["diagnoses"] == ["Alzheimer's disease", "Epilepsy", "Migraine", "Multiple sclerosis",
                              "Parkinson's disease", "Stroke"]
    assert summary([])["mean_age"] is None


if __name__ == "__main__":
    results = [
        run_test("Step 1 clean_id", t1),
        run_test("Step 2 clean_sex", t2),
        run_test("Step 3 clean_age", t3),
        run_test("Step 4 clean_weight", t4),
        run_test("Step 5 clean_diagnosis", t5),
        run_test("Step 6 clean_record", t6),
        run_test("Step 7 remove_duplicates", t7),
        run_test("Step 8 clean_all", t8),
        run_test("Step 9 summary", t9),
    ]
    print(f"\n{sum(results)}/{len(results)} passed")


# ===================== HINTS (try first, then read) =====================
# 1: two string methods chained: raw.strip().upper()
# 2: build the dictionary {"f": "F", "female": "F", "m": "M", "male": "M"}; look up raw.strip().lower() with .get(key, "unknown")
# 3: text = raw.strip(); if text.isdigit(): age = int(text) ... check the range ... otherwise return None AFTER the ifs.
#    "-5".isdigit() is False because of the minus sign, "".isdigit() is False too.
# 4: text = raw.lower().replace("kg", "").replace(",", ".").strip() ; then the isdigit test from the comment; float(text).
# 5: the string method .capitalize() does exactly this.
# 6: return { "id": clean_id(raw_record["id"]), ... }  five keys, five calls.
# 7: seen = set(), result = []. For each record: is its id in seen? skip. Otherwise add the id to seen AND the record to result.
# 8: loop, append clean_record(r) to a new list, then return remove_duplicates(that list).
# 9: before the loop: missing_age = 0, missing_weight = 0, by_sex = {}, age_total = 0, age_count = 0, diagnoses = set().
#    inside: update each one. after: mean = round(age_total / age_count, 1) but guard age_count == 0 BEFORE dividing.
#
#
#
# ===========================================================================
# SEALED SOLUTIONS — open only after you have tried each step for at least 15 minutes
# ===========================================================================
#   def clean_id(raw):
#       return raw.strip().upper()
#
#   def clean_sex(raw):
#       sex_map = {"f": "F", "female": "F", "m": "M", "male": "M"}
#       return sex_map.get(raw.strip().lower(), "unknown")
#
#   def clean_age(raw):
#       text = raw.strip()
#       if text.isdigit():
#           age = int(text)
#           if 0 < age <= 120:
#               return age
#       return None
#
#   def clean_weight(raw):
#       text = raw.lower().replace("kg", "").replace(",", ".").strip()
#       if text.replace(".", "", 1).isdigit():
#           return float(text)
#       return None
#
#   def clean_diagnosis(raw):
#       return raw.strip().capitalize()
#
#   def clean_record(raw_record):
#       return {
#           "id": clean_id(raw_record["id"]),
#           "age": clean_age(raw_record["age"]),
#           "sex": clean_sex(raw_record["sex"]),
#           "diagnosis": clean_diagnosis(raw_record["diagnosis"]),
#           "weight_kg": clean_weight(raw_record["weight"]),
#       }
#
#   def remove_duplicates(records):
#       seen = set()
#       result = []
#       for record in records:
#           if record["id"] not in seen:
#               seen.add(record["id"])
#               result.append(record)
#       return result
#
#   def clean_all(raw_records):
#       cleaned = []
#       for raw_record in raw_records:
#           cleaned.append(clean_record(raw_record))
#       return remove_duplicates(cleaned)
#
#   def summary(records):
#       missing_age = 0
#       missing_weight = 0
#       by_sex = {}
#       age_total = 0
#       age_count = 0
#       diagnoses = set()
#       for record in records:
#           if record["age"] is None:
#               missing_age += 1
#           else:
#               age_total += record["age"]
#               age_count += 1
#           if record["weight_kg"] is None:
#               missing_weight += 1
#           by_sex[record["sex"]] = by_sex.get(record["sex"], 0) + 1
#           diagnoses.add(record["diagnosis"])
#       mean_age = round(age_total / age_count, 1) if age_count else None
#       return {
#           "n": len(records),
#           "missing_age": missing_age,
#           "missing_weight": missing_weight,
#           "by_sex": by_sex,
#           "mean_age": mean_age,
#           "diagnoses": sorted(diagnoses),
#       }
#
