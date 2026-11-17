-- UPSKILLER · DAY 4 · SQL MICRO-TRACK #2: calculated columns + LIMIT
--
-- SETUP (terminal, inside ~/upskiller/day04):
--     sqlite3 day04.db < day04_sql.sql
--     sqlite3 day04.db
--     .headers on
--     .mode column
-- (If you made ~/.sqliterc on Friday, the two dot-lines happen automatically.)

DROP TABLE IF EXISTS samples;

CREATE TABLE samples (
    sample_id     TEXT,
    patient_id    TEXT,
    tissue        TEXT,
    conc_ng_ul    REAL,      -- DNA concentration, ng per microlitre
    volume_ul     REAL       -- volume left in the tube, microlitres
);

INSERT INTO samples VALUES ('S01', 'P001', 'Blood',  45.2, 50);
INSERT INTO samples VALUES ('S02', 'P001', 'CSF',     8.7, 20);
INSERT INTO samples VALUES ('S03', 'P002', 'Blood',  61.0, 40);
INSERT INTO samples VALUES ('S04', 'P003', 'Tissue', 120.5, 15);
INSERT INTO samples VALUES ('S05', 'P004', 'Blood',  33.3, 60);
INSERT INTO samples VALUES ('S06', 'P005', 'CSF',     5.1, 25);

-- ============================================================
-- MINI-LESSON (3 min)
-- SELECT can CALCULATE, not just show columns:
--     SELECT sample_id, conc_ng_ul * 2 AS doubled FROM samples;
-- + - * / work like Python. Give every calculated column a name with AS,
-- otherwise the header is the ugly formula itself.
-- LIMIT n shows only the first n rows (useful to peek at a huge table):
--     SELECT * FROM samples LIMIT 2;
--
-- DAILY DRILL — SQL (12 min, timed)
-- Q1. Show sample_id and the TOTAL DNA in each tube in nanograms
--     (concentration × volume). Call the column total_dna_ng.
SELECT sample_id, conc_ng_ul * volume_ul AS total_dna_ng FROM samples;
-- Q2. Show sample_id, tissue, and the volume in millilitres
--     (1 ml = 1000 µl). Call it volume_ml.
SELECT sample_id, tissue, volume_ul / 1000 AS volume_ml FROM samples;
-- Q3. Show the first 3 rows of the table, all columns.
SELECT * FROM samples LIMIT 3;  
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
-- ============================================================
-- SEALED SOLUTIONS
-- ============================================================
-- Q1: SELECT sample_id, conc_ng_ul * volume_ul AS total_dna_ng FROM samples;
--     S01 -> 45.2 × 50 = 2260.0. Multiplying two columns works row by row,
--     like NumPy arrays: each row is calculated separately.
-- Q2: SELECT sample_id, tissue, volume_ul / 1000 AS volume_ml FROM samples;
--     S01 -> 0.05. CAREFUL: in SQLite, INTEGER / INTEGER does integer division
--     (like Python's //): 50 / 1000 would give 0! It works here because
--     volume_ul is REAL. Safe habit: divide by 1000.0
-- Q3: SELECT * FROM samples LIMIT 3;
--     Note: without ORDER BY (Week 2) the database does not promise WHICH rows
--     come first. On a small table it's insertion order, but don't rely on it.
--
-- Common wrong answers:
--   SELECT conc_ng_ul * volume_ul FROM samples;   -> works, but header is the formula
--   SELECT sample_id, total_dna_ng = conc_ng_ul * volume_ul ...  -> that's Python
--     thinking; SQL names columns with AS after the expression.
