# UPSKILLER · LESSON 2 · Diagnostic test

**Time: 45 minutes, timed. No notes, no internet, no running code.** Write your answer under each question. "I don't know" is a useful answer: it tells me where to start. Don't guess wildly; write what you think and how sure you are (sure / unsure).

This isn't graded. It sets the pace of the next 4 weeks.

---

## Part A — Read the code: what does it print? (8 questions)

**A1**
```python
x = 7
y = 2
print(x / y, x // y, x % y)
```
Answer:3 , donno , 1

**A2**
```python
name = "microglia"
print(name[0], name[-1], name[2:5], len(name))
```
Answer:m,a,cro,9

**A3**
```python
values = [4, 8, 15]
values.append(16)
print(values, len(values))
```
Answer:4,8,15,16, 4

**A4**
```python
def double(n):
    print(n * 2)

result = double(5)
print(result)
```
Answer (both lines):nn , 10

**A5**
```python
counts = {"A": 3, "T": 5}
counts["G"] = 2
counts["A"] = counts["A"] + 1
print(counts)
```
Answer:{"A": 4, "T": 5, "G" : 2}

**A6**
```python
total = 0
for i in range(1, 5):
    total = total + i
print(total)
```
Answer:17

**A7**
```python
seq = "ATGC"
print(seq[::-1], seq.lower(), "G" in seq)
```
Answer:"CGTA", atgc , true

**A8**
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```
Answer:1,2,3

---

## Part B — Write code (4 questions). Write it on paper/in this file; don't run it.

**B1.** Write a function `is_adult(age)` that returns `True` if age is 18 or more, otherwise `False`.

**B2.** Write a function `count_long_genes(lengths)` that takes a list of numbers and returns how many are greater than 1000.

**B3.** Given `temps = [36.6, 37.2, 39.1, 38.4]`, write code that finds the highest temperature WITHOUT using `max()`.

**B4.** Write a function `base_counts(seq)` that returns a dictionary with how many times each letter appears, e.g. `base_counts("AAG")` → `{"A": 2, "G": 1}`.

---

## Part C — Maths for data (8 questions)

**C1.** A test is positive in 45 of 300 samples. What percentage is that?

**C2.** The mean of 4, 8, 6, 2 is? The median of 4, 8, 6, 2, 100 is?

**C3.** What is log₁₀(1000)? What is 2⁵? What is 10⁰?

**C4.** A line goes through (0, 2) and (4, 10). What is its slope? Write its equation y = …

**C5.** Vector u = (1, 2, 3), vector v = (4, 0, −1). What is the dot product u · v?

**C6.** A fair coin is flipped twice. What is the probability of getting two heads?

**C7.** In one sentence: what does the derivative of a function tell you?

**C8.** Data: 10, 10, 10, 10 and 0, 10, 20, 10. Which set has the bigger standard deviation, and why (no calculation needed)?

---

## Part D — Thinking like an analyst (3 questions)

**D1.** A hospital says "average length of stay is 9 days", but most patients stay 2–3 days. How can both be true?

**D2.** People who drink more coffee have more heart problems in a dataset. Give one reason this might NOT mean coffee causes heart problems.

**D3.** A model detecting a rare disease (1 in 100 people) is "99% accurate". Why might that be useless?

---

## After the test (not timed)

How did it feel, 1–5, for each part? A: __ B: __ C: __ D: __

Hand in this file with your answers. Don't look anything up before I mark it.
