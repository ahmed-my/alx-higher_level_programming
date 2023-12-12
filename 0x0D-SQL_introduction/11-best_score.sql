-- Script that lists all records with a score >= 10 in the 
-- second_table of the database hbtn_0c_0
-- Results should display both the score and name (in this order)
-- Records should be ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score;
