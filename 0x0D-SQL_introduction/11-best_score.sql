-- script that lists score >= 10 in descending order
-- best score from second_table
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
