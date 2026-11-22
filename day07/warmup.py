# 1. count_over_65(ages): how many ages are above 65 (counter)
# 2. heaviest(weights): the largest weight without max() (best so far)
# 3. letter_counts(seq): a dictionary letter → how many (counting dict)

def count_over_65(ages):
    count = 0
    for age in ages:
        if age > 65:
            count += 1
    return count

def heaviest(weights):
    if not weights:
        return None
    max_weight = weights[0]
    for weight in weights:
        if weight > max_weight:
            max_weight = weight
    return max_weight

def letter_counts(seq):
    counts = {}
    for letter in seq:
        counts[letter] = counts.get(letter, 0) + 1
    return counts

assert count_over_65([70, 40, 66, 65]) == 2
assert heaviest([61.5, 90.3, 55.1]) == 90.3
assert letter_counts("GATTACA") == {"G": 1, "A": 3, "T": 2, "C": 1}