-- UPSKILLER · DAY 10 · SQL MICRO-TRACK #9 (GROUP BY) + #10 (HAVING)
--
-- SETUP (terminal, in ~/upskiller/day10):
--     sqlite3 day10.db < day10_sql.sql
--     sqlite3 day10.db
--     .headers on
--     .mode column
-- Then paste each of YOUR queries at the sqlite3 prompt, one at a time, and PASTE THE OUTPUT into your tab.
-- (Same patients table as Sunday.)

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
-- MINI-LESSON #9 — GROUP BY (5 min): one result row PER GROUP. It is Python's counting dictionary, written in SQL.
--     SELECT ward, COUNT(*) AS n FROM patients GROUP BY ward;
--   Read it as: "put the rows into one pile per ward, then run COUNT on each pile".
--     SELECT sex, ROUND(AVG(age), 1) AS avg_age FROM patients GROUP BY sex;
--   RULE: every column in SELECT must be either in GROUP BY or inside an aggregate function (COUNT, AVG, ...).
--   Order of a query now:  SELECT ... FROM ... WHERE ... GROUP BY ... ORDER BY ... LIMIT ...
--   WHERE filters the ROWS BEFORE they are put in piles.
--
-- MINI-LESSON #10 — HAVING (4 min): filter the PILES after the aggregate has run. WHERE cannot do this, because the count does not exist yet.
--     SELECT ward, COUNT(*) AS n FROM patients GROUP BY ward HAVING COUNT(*) > 2;
--   Order of a query with everything:  SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT ...
--   Quick test: "filter on a column of the row" -> WHERE.   "filter on a number I calculated per group" -> HAVING.
--
-- DAILY DRILL — SQL (12 min, timed; 5 short questions)
-- Q1. How many patients are on each ward? Columns: ward, n.
-- Q2. The average age per sex, rounded to 1 decimal. Columns: sex, avg_age.
-- Q3. How many patients per diagnosis, the most common first; ties in alphabetical order of diagnosis. Columns: diagnosis, n.
-- Q4. Only the wards that have MORE THAN 2 patients. Columns: ward, n.
-- Q5. The average weight_kg per ward, rounded to 1 decimal, only for wards whose average weight is above 70, highest average first. Columns: ward, avg_weight.
-- ============================================================
-- Write your queries below the question number, then paste the sqlite3 OUTPUT in the tab.

-- Q1 Select ward, COUNT(*) AS n FROM patients GROUP BY ward;


-- Q2 SELECT sex, ROUND(AVG(age), 1) AS avg_age FROM patients GROUP BY sex;


-- Q3 SELECT diagnosis, COUNT(*) AS n FROM patients GROUP BY diagnosis ORDER BY n DESC, diagnosis ASC;


-- Q4 SELECT ward, COUNT(*) AS n FROM patients GROUP BY ward HAVING COUNT(*) > 2;  


-- Q5 SELECT ward, ROUND(AVG(weight_kg), 1) AS avg_weight FROM patients GROUP BY ward HAVING AVG(weight_kg) > 70 ORDER BY avg_weight DESC;

