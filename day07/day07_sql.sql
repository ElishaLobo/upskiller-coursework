-- UPSKILLER · DAY 07 · SQL MICRO-TRACK #5 (WHERE) + #6 (AND / OR / IN / BETWEEN / LIKE)
--
-- SETUP (terminal, in ~/upskiller/day07):
--     sqlite3 day07.db < day07_sql.sql
--     sqlite3 day07.db
--     .headers on
--     .mode column

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
-- MINI-LESSON #5 — WHERE (4 min): keep only the rows that pass a test, like an `if` inside a loop.
--     SELECT patient_id, age FROM patients WHERE age >= 60;
--   Comparisons: =  !=  <  <=  >  >=      (ONE equals sign, not two)
--   Text goes in SINGLE quotes: WHERE ward = 'Neuro'
--   Order of a query:  SELECT ... FROM ... WHERE ...   (WHERE comes after FROM)
--
-- MINI-LESSON #6 — combining tests (4 min)
--   AND  both true          WHERE age >= 60 AND sex = 'F'
--   OR   at least one true  WHERE ward = 'Neuro' OR ward = 'Outpatient'
--   IN   shorter OR         WHERE ward IN ('Neuro', 'Outpatient')
--   BETWEEN a AND b         INCLUDES both ends: WHERE age BETWEEN 40 AND 60
--   LIKE with %             % = any characters: WHERE diagnosis LIKE '%disease'
--   Use brackets when mixing AND with OR:  WHERE (a OR b) AND c
--
-- DAILY DRILL — SQL (12 min, timed; 5 short questions today)
-- Q1. Patient IDs and ages of everyone aged 60 or older.
SELECT patient_id, age FROM patients WHERE age >= 60;
-- Q2. All columns for patients on the 'Neuro' ward who weigh more than 70 kg.
SELECT * FROM patients WHERE ward = 'Neuro' AND weight_kg > 70;
-- Q3. patient_id and diagnosis for patients on the 'Stroke unit' OR 'Outpatient' ward. Write it ONCE with IN.
SELECT patient_id, diagnosis FROM patients WHERE ward IN ('Stroke unit', 'Outpatient');
-- Q4. patient_id and age for patients aged 40 to 60 INCLUDING both ends.
SELECT patient_id, age FROM patients WHERE age BETWEEN 40 AND 60;
-- Q5. Diagnoses that end in the word 'disease' (use LIKE), each diagnosis once.
SELECT DISTINCT diagnosis FROM patients WHERE diagnosis LIKE '%disease';
-- ============================================================
--
--   (write your 5 queries below, one per question)
--
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
-- Q1: SELECT patient_id, age FROM patients WHERE age >= 60;                       -- P001 P003 P007 (3 rows)
-- Q2: SELECT * FROM patients WHERE ward = 'Neuro' AND weight_kg > 70;              -- P002 P003 (2 rows)
-- Q3: SELECT patient_id, diagnosis FROM patients WHERE ward IN ('Stroke unit', 'Outpatient');   -- 4 rows
-- Q4: SELECT patient_id, age FROM patients WHERE age BETWEEN 40 AND 60;            -- P002 P004 P006 (3 rows)
-- Q5: SELECT DISTINCT diagnosis FROM patients WHERE diagnosis LIKE '%disease';     -- 2 rows
-- Common wrong answers: WHERE age == 60 (two equals); "Neuro" in double quotes; writing WHERE before FROM;
--   weight_kg >= 70 when the question says "more than"; forgetting brackets when mixing AND with OR.
