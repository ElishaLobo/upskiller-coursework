# UPSKILLER · DAY 1 · broken_2.py
# Run it:   python broken_2.py
# There are 2 problems. Fix them one at a time, running after each fix.
# When it works it prints:
#     Mean firing rate: 12.5 Hz
#     Standard error of counts: 4.41

from scipy.stats import sem

def mean_rate(spike_counts, seconds):
    total = sum(spike_counts)
    return total / seconds

counts = [10, 15, 25]
print("Mean firing rate:", mean_rate(counts, 4), "Hz")
print("Standard error of counts:", round(sem(counts), 2))

# ERROR DIARY (broken_2.py)
# Problem 1  error name:          line:        what it means:          fix:
# Problem 2  error name:          line:        what it means:          fix:
# (Hint for problem 2, only once you see it: is the package installed in your
#  `ds` environment? The fix is a terminal command, not a code change:
#  conda install <package name> -y )
