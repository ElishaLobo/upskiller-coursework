-- UPSKILLER · DAY 1 · SQL MICRO-TRACK #1: tables and SELECT
--
-- SETUP (in the terminal, inside ~/upskiller/day01):
--     sqlite3 day01.db < day01_sql.sql      <- builds the table from this file
--     sqlite3 day01.db                      <- opens the database
-- Then type these two settings so results look like a table:
--     .headers on
--     .mode column
-- To leave SQLite:  .quit
--
-- THE TABLE: one row = one patient, one column = one fact about them.

DROP TABLE IF EXISTS patients;

CREATE TABLE patients (
    patient_id  TEXT,
    age         INTEGER,
    sex         TEXT,
    diagnosis   TEXT,
    ward        TEXT
);

INSERT INTO patients VALUES ('P001', 67, 'F', 'Alzheimer''s disease', 'Neuro');
INSERT INTO patients VALUES ('P002', 54, 'M', 'Epilepsy',            'Neuro');
INSERT INTO patients VALUES ('P003', 71, 'M', 'Parkinson''s disease','Neuro');
INSERT INTO patients VALUES ('P004', 45, 'F', 'Migraine',            'Outpatient');
INSERT INTO patients VALUES ('P005', 38, 'F', 'Multiple sclerosis',  'Neuro');
INSERT INTO patients VALUES ('P006', 59, 'M', 'Stroke',              'Stroke unit');
INSERT INTO patients VALUES ('P007', 82, 'F', 'Stroke',              'Stroke unit');
INSERT INTO patients VALUES ('P008', 29, 'M', 'Epilepsy',            'Outpatient');

-- ============================================================
-- DAILY DRILL — SQL (12 minutes, timed). Type your answers in the
-- sqlite3 prompt. Every SQL statement ends with a semicolon ;
--
-- Q1. Show every column of every patient.
-- Q2. Show only the patient_id and diagnosis columns.
-- Q3. Show diagnosis first, then age, and rename the age column so the
--     header reads  age_years
--
-- Paste your three queries into your hand-in message.
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
--
--
--
--
--
--
-- ============================================================
-- SEALED SOLUTIONS (open ONLY after your timed attempt)
-- ============================================================
-- Q1:  SELECT * FROM patients;
--      SELECT = "show me", * = "every column", FROM patients = "from this table".
--      Returns 8 rows x 5 columns.
--
-- Q2:  SELECT patient_id, diagnosis FROM patients;
--      List the columns you want, separated by commas. Order in the list =
--      order on screen. Still 8 rows, now 2 columns.
--
-- Q3:  SELECT diagnosis, age AS age_years FROM patients;
--      AS gives a column a new name in the RESULT only. The table itself
--      is unchanged.
--
-- Pattern: projection (choosing columns). Next lessons add filtering (WHERE)
--   = choosing rows.
-- Common wrong answers:
--   SELECT patient_id diagnosis FROM patients;   <- missing comma: SQLite
--     treats "diagnosis" as an alias for patient_id! No error, wrong result.
--   Forgetting the ; -> the prompt shows  ...>  and waits. Type ; and Enter.
--   SELECT * FROM Patients;  works in SQLite (names aren't case-sensitive)
--     but write table names exactly as created: good habit for other databases.
