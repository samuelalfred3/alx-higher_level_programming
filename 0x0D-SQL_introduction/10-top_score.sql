-- 10-top_score.sql

-- List all records of the second_table, displaying score and name, ordered by score (top first)
SELECT score, name
FROM second_table
ORDER BY score DESC;

