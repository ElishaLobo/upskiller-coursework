"""
UPSKILLER · DAY 10 · MODULE 2 · STRINGS IN DEPTH — exercises 1 (60 min)
Run:  python day10_strings.py      Goal: 8/8
Rules: RETURN, don't print. Never edit the tests. Read the tab lesson first. Type every function yourself.
ERROR DIARY under every function the moment a test goes red: error message / which line / what it means in plain words / the fix.
Reminder: a string can NOT be changed. text.upper() gives you a NEW string; if you do not keep it (a variable or return), it is lost.
"""
import sys
import traceback

# S1 — first_codon(dna): the first three letters. Use SLICING, not a loop.   first_codon("ATGCCC") -> "ATG"
def first_codon(dna):
    return dna[:3]
# ERROR DIARY S1: no


# S2 — last_n(text, n): the last n characters (n is from 0 up to len(text)). last_n("TP53-APP", 3) -> "APP"   last_n("abc", 0) -> ""
# TRAP: text[-0:] is NOT empty. Think about what -0 means, then build the start position from len(text).
def last_n(text, n):
    if n == 0:
        return ""
    else:
        return text[-n:]
# ERROR DIARY S2:


# S3 — reverse_complement(dna): the DNA strand that pairs with this one, read the other way round.
# A<->T and C<->G, then REVERSE the whole thing.   reverse_complement("ATGC") -> "GCAT"   reverse_complement("AAAC") -> "GTTT"
# Use a dictionary for the pairs (like clean_sex) and build the result letter by letter.
def reverse_complement(dna):
    rev = {"A": "T", "T": "A", "C": "G", "G": "C"}
    result = ""
    for letter in dna:
        result+= rev[letter]
    return result[::-1]
# ERROR DIARY S3: forgot to reverse it


# S4 — parse_pair(text): "TP53:2.0" -> ("TP53", 2.0). Spaces around either part must go: " TP53 : 2.0 " -> ("TP53", 2.0).
# Tools: .split(":") gives a list of pieces; .strip() removes spaces; float() converts. Return a TUPLE (gene, level).
def parse_pair(text):
    gene, level = text.split(":")
    gene = gene.strip()
    level = float(level.strip())
    return (gene, level)
    pass  # your code here
# ERROR DIARY S4: simple


# S5 — parse_fasta_header(header): UniProt headers look like
#   ">sp|P05067|A4_HUMAN Amyloid-beta precursor protein OS=Homo sapiens OX=9606 GN=APP PE=1 SV=3"
# Return a dictionary {"accession": "P05067", "entry": "A4_HUMAN", "description": "Amyloid-beta precursor protein"}.
# Plan: split on "|" (3 pieces), then split the last piece ONCE on the first space  .split(" ", 1)  , then cut the description at " OS=".
def parse_fasta_header(header):
    parts = header.split("|")
    accession = parts[1]
    entry = parts[2].split(" ", 1)[0]
    description = parts[2].split(" ", 1)[1].split(" OS=")[0]
    return {"accession": accession, "entry": entry, "description": description}

# ERROR DIARY S5: understood it


# S6 — gc_content(dna): the percentage of letters that are G or C, rounded to 1 decimal. Upper or lower case both count.
# gc_content("ATGC") -> 50.0    gc_content("gggg") -> 100.0    gc_content("") -> 0.0   (careful: dividing by len("") crashes)
def gc_content(dna):
    dna= dna.upper()
    if len(dna)==0:
        return 0.0
    count=0
    for l in dna:
        if l in "GC":
            count += 1
    return round((count / len(dna)) * 100, 1)
# ERROR DIARY S6: if theres an easier way tell me/ if len(dna)==0: return 0.0; else: return round((dna.upper().count("G") + dna.upper().count("C")) / len(dna) * 100, 1)


# S7 — report_line(name, age, weight): one table row built with an f-string and format specs.
# report_line("P001", 67, 61.5) -> "P001  | age  67 | 61.5 kg"      name padded to 5 wide (left), age padded to 3 wide (right), weight 1 decimal
# If weight is None the end of the line is "weight unknown":  report_line("P002", 5, None) -> "P002  | age   5 | weight unknown"
# Format specs: {name:<5}  left-align in 5 characters,  {age:>3}  right-align in 3,  {weight:.1f}  one decimal.
def report_line(name, age, weight):
    report = f"{name:<5} | age {age:>3} | "
    if weight is None:
        report += "weight unknown"
    else:
        report += f"{weight:.1f} kg"
    return report 
# ERROR DIARY S7:


# S8 — split_codons(dna): cut the string into pieces of exactly 3 letters; drop a leftover of 1 or 2 letters at the end.
# split_codons("ATGCCCTAAG") -> ["ATG", "CCC", "TAA"]      split_codons("AT") -> []      split_codons("") -> []
# Idea: range(0, stop, 3) gives the start positions 0, 3, 6, ...; each piece is dna[start:start + 3]. What must stop be?
def split_codons(dna):
    x = []
    for i in range(0, len(dna) - len(dna) % 3, 3): # learn this formula for stop: len(dna) - len(dna) % 3
        x.append(dna[i:i + 3])
    return x
# ERROR DIARY S8:


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
    assert first_codon("ATGCCC") == "ATG"
    assert first_codon("AT") == "AT", "slicing never crashes on a short string"
    assert first_codon("") == ""

def t2():
    assert last_n("TP53-APP", 3) == "APP"
    assert last_n("abc", 0) == "", "n = 0 must give an empty string"
    assert last_n("abc", 3) == "abc"
    assert last_n("abc", 1) == "c"

def t3():
    assert reverse_complement("ATGC") == "GCAT"
    assert reverse_complement("AAAC") == "GTTT"
    assert reverse_complement("") == ""
    s = "ATTG"
    reverse_complement(s)
    assert s == "ATTG"

def t4():
    assert parse_pair("TP53:2.0") == ("TP53", 2.0)
    assert parse_pair(" TP53 : 2.0 ") == ("TP53", 2.0)
    assert parse_pair("APP:8") == ("APP", 8.0)
    assert isinstance(parse_pair("APP:8")[1], float)

def t5():
    h = ">sp|P05067|A4_HUMAN Amyloid-beta precursor protein OS=Homo sapiens OX=9606 GN=APP PE=1 SV=3"
    assert parse_fasta_header(h) == {"accession": "P05067", "entry": "A4_HUMAN", "description": "Amyloid-beta precursor protein"}
    h2 = ">sp|P04637|P53_HUMAN Cellular tumor antigen p53 OS=Homo sapiens OX=9606 GN=TP53 PE=1 SV=4"
    assert parse_fasta_header(h2) == {"accession": "P04637", "entry": "P53_HUMAN", "description": "Cellular tumor antigen p53"}

def t6():
    assert gc_content("ATGC") == 50.0
    assert gc_content("gggg") == 100.0
    assert gc_content("") == 0.0
    assert gc_content("ATAT") == 0.0
    assert gc_content("GCAtt") == 40.0
    assert gc_content("ATG") == 33.3

def t7():
    assert report_line("P001", 67, 61.5) == "P001  | age  67 | 61.5 kg"
    assert report_line("P002", 5, None) == "P002  | age   5 | weight unknown"
    assert report_line("P003", 100, 77.26) == "P003  | age 100 | 77.3 kg"
    assert report_line("AB", 9, 80) == "AB    | age   9 | 80.0 kg"

def t8():
    assert split_codons("ATGCCCTAAG") == ["ATG", "CCC", "TAA"]
    assert split_codons("AT") == []
    assert split_codons("") == []
    assert split_codons("ATG") == ["ATG"]
    assert split_codons("ATGCC") == ["ATG"]
    assert split_codons("ATGCCCT") == ["ATG", "CCC"]


if __name__ == "__main__":
    results = [
        run_test("S1 first_codon", t1),
        run_test("S2 last_n", t2),
        run_test("S3 reverse_complement", t3),
        run_test("S4 parse_pair", t4),
        run_test("S5 parse_fasta_header", t5),
        run_test("S6 gc_content", t6),
        run_test("S7 report_line", t7),
        run_test("S8 split_codons", t8),
    ]
    print(f"\n{sum(results)}/{len(results)} passed")


# ===================== HINTS (try first, then read) =====================
# S1: dna[:3] means "from the start up to, not including, position 3".
# S2: the start position is len(text) - n. Then slice from there to the end.
# S3: loop over dna; for each letter look up its partner in the dictionary and put it at the FRONT of the result:  result = partner + result
# S4: text.split(":") returns a list of two strings; unpack with  gene, level = ...  ; strip each; float() the level.
# S5: header.split("|") -> 3 pieces; the first piece (">sp") is not needed, name it _ .
# S6: .upper() first so "g" counts; .count("G") counts one letter. Empty string -> return before dividing.
# S7: f"{name:<5} | age {age:>3} | {end}"  -- build `end` first with an if/else.
# S8: stop = len(dna) - len(dna) % 3  (% is the remainder). range(0, stop, 3).
