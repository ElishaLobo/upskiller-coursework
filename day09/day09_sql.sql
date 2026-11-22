-- UPSKILLER · DAY 09 · SQL MICRO-TRACK #7 (ORDER BY / LIMIT) + #8 (COUNT / SUM / AVG / MIN / MAX)
--
-- SETUP (terminal, in ~/upskiller/day09):
--     sqlite3 day09.db < day09_sql.sql
--     sqlite3 day09.db
--     .headers on
--     .mode column
-- Then paste each of YOUR queries at the sqlite3 prompt, one at a time, and PASTE THE OUTPUT into your tab.

DROP TABLE IF EXISTS patients;
CREATE TABLE patients (
    patient_id  TEXT,
    age         INTEGER,
    sex         TEXT,
    diagnosis   TEXT,
    ward        TEXT,
    weight_kg   REAL
);
INSERT INTO patients VALUES ('P001', 67, 'F', 'Alzheimer''s disease', 'Neuro',       61.5);
INSERT INTO patients VALUES ('P002', 54, 'M', 'Epilepsy',            'Neuro',       82.0);
INSERT INTO patients VALUES ('P003', 71, 'M', 'Parkinson''s disease','Neuro',       77.25);
INSERT INTO patients VALUES ('P004', 45, 'F', 'Migraine',            'Outpatient',  58.0);
INSERT INTO patients VALUES ('P005', 38, 'F', 'Multiple sclerosis',  'Neuro',       64.8);
INSERT INTO patients VALUES ('P006', 59, 'M', 'Stroke',              'Stroke unit', 90.3);
INSERT INTO patients VALUES ('P007', 82, 'F', 'Stroke',              'Stroke unit', 55.1);
INSERT INTO patients VALUES ('P008', 29, 'M', 'Epilepsy',            'Outpatient',  71.6);

-- ============================================================
-- MINI-LESSON #7 — ORDER BY and LIMIT (4 min): sort the result, then keep only the first rows.
--     SELECT patient_id, age FROM patients ORDER BY age;          -- smallest first (ASC is the default)
--     SELECT patient_id, age FROM patients ORDER BY age DESC;     -- biggest first
--     SELECT patient_id, age FROM patients ORDER BY age DESC LIMIT 3;   -- the 3 oldest
--   Order of a query so far:  SELECT ... FROM ... WHERE ... ORDER BY ... LIMIT ...
--   Sort by two things: ORDER BY ward, age DESC   (ward first, then age inside each ward)
--
-- MINI-LESSON #8 — aggregate functions (4 min): many rows go in, ONE number comes out.
--     COUNT(*)  how many rows        SUM(x) total        AVG(x) mean        MIN(x) smallest        MAX(x) biggest
--     SELECT COUNT(*) FROM patients;                       -- 8
--     SELECT AVG(weight_kg) FROM patients WHERE sex = 'F'; -- WHERE filters FIRST, then the function runs
--     ROUND(x, 1) rounds to 1 decimal:  SELECT ROUND(AVG(age), 1) FROM patients;
--     Give the result a label with AS:  SELECT COUNT(*) AS n_patients FROM patients;
--   (Next time: GROUP BY, which gives one number PER group, like Python's counting dictionary.)
--
-- DAILY DRILL — SQL (12 min, timed; 5 short questions)
-- Q1. patient_id and age of everyone, oldest first.
SELECT patient_id, age FROM patients ORDER BY age DESC;
-- Q2. patient_id and weight_kg of the THREE heaviest patients, heaviest first.
SELECT patient_id, weight_kg FROM patients ORDER BY weight_kg DESC LIMIT 3;
-- Q3. How many patients are there in total? Label the column n_patients.
SELECT COUNT(*) AS n_patients FROM patients;
-- Q4. The average age of the patients on the 'Neuro' ward, rounded to 1 decimal.
SELECT ROUND(AVG(age), 1) FROM patients WHERE ward = 'Neuro';
-- Q5. The youngest age and the oldest age in the table, in ONE query (two columns: youngest, oldest).
SELECT MIN(age) AS youngest, MAX(age) AS oldest FROM patients;
-- ============================================================
--
--   (write your 5 queries below, one per question, then run them and paste the output)
--
--
--
--
--
--
--
-- ============================================================
-- SEALED SOLUTIONS — open only after your 12 minutes
-- ============================================================
-- Q1: SELECT patient_id, age FROM patients ORDER BY age DESC;                      -- P007 82, P003 71, P001 67, ... P008 29 (8 rows)
-- Q2: SELECT patient_id, weight_kg FROM patients ORDER BY weight_kg DESC LIMIT 3;   -- P006 90.3, P002 82.0, P003 77.25
-- Q3: SELECT COUNT(*) AS n_patients FROM patients;                                  -- 8
-- Q4: SELECT ROUND(AVG(age), 1) FROM patients WHERE ward = 'Neuro';                 -- 57.5
-- Q5: SELECT MIN(age) AS youngest, MAX(age) AS oldest FROM patients;                -- 29, 82
-- Common wrong answers: ORDER BY before WHERE; LIMIT without ORDER BY (you get ANY 3 rows, not the heaviest);
--   writing DESC before the column name; AVG(age) without WHERE (gives all 8 patients); COUNT(age) vs COUNT(*) (COUNT(column) skips NULLs).
