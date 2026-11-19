-- UPSKILLER · DAY 05 · SQL MICRO-TRACK #3 (DISTINCT) + #4 (text and number functions)
--
-- SETUP (terminal, in ~/upskiller/day05):
--     sqlite3 day05.db < day05_sql.sql
--     sqlite3 day05.db
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
-- MINI-LESSON #3 — DISTINCT (3 min)
-- SELECT DISTINCT column FROM table;  -> each different value ONCE.
-- Like turning a column into a Python set: duplicates collapse.
-- With two columns, DISTINCT applies to the PAIR:
--     SELECT DISTINCT ward, sex FROM patients;  -> each different (ward, sex) combination
--
-- MINI-LESSON #4 — functions in SELECT (3 min)
--   UPPER(text) / LOWER(text)      change case
--   LENGTH(text)                   number of characters
--   ROUND(number, 1)               round to 1 decimal place
--   a || ' - ' || b                glue text together (|| = Python's + for strings)
--
-- DAILY DRILL — SQL (12 min, timed; 4 short questions today)
-- Q1. List each ward once.
SELECT DISTINCT ward FROM patients;

-- Q2. List each different (diagnosis, ward) combination once.
SELECT DISTINCT diagnosis, ward FROM patients;

-- Q3. Show patient_id and a label like  'P001 - ALZHEIMER''S DISEASE'
--     (id, then " - ", then the diagnosis in capitals). Call it label.
SELECT patient_id, patient_id || ' - ' || UPPER(diagnosis) AS label FROM patients;
-- Q4. Show patient_id and the weight rounded to the nearest whole kg
--     AND the number of letters in the diagnosis. Name the columns weight_rounded
--     and diagnosis_length.
SELECT patient_id, ROUND(weight_kg) AS weight_rounded,
       LENGTH(diagnosis) AS diagnosis_length FROM patients;
-- ============================================================
--
--
--
--
--
--
--
--
--
--
--
--
-- ============================================================
-- SEALED SOLUTIONS
-- ============================================================
-- Q1: SELECT DISTINCT ward FROM patients;               -> 3 rows: Neuro, Outpatient, Stroke unit
-- Q2: SELECT DISTINCT diagnosis, ward FROM patients;    -> 7 rows (Epilepsy appears twice:
--     once in Neuro, once in Outpatient — the PAIR is different, so both stay)
-- Q3: SELECT patient_id, patient_id || ' - ' || UPPER(diagnosis) AS label FROM patients;
-- Q4: SELECT patient_id, ROUND(weight_kg) AS weight_rounded,
--            LENGTH(diagnosis) AS diagnosis_length FROM patients;
--     ROUND(x) with no second number rounds to 0 decimals (SQLite returns 62.0 for 61.5).
--
-- Common wrong answers:
--   SELECT ward DISTINCT FROM patients;   -> DISTINCT goes right after SELECT.
--   patient_id + ' - ' + diagnosis        -> + is maths in SQL; text glue is ||.
--   Writing 'Alzheimer's' inside SQL      -> a single ' ends the text. Inside SQL text,
--     write it twice: 'Alzheimer''s'. (That's why the INSERTs above look odd.)
