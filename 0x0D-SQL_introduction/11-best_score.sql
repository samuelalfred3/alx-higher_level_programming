-- 11-best_score.sql

-- List all records with a score >= 10, displaying score and name, ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

