-- script that lists the number of records with the same score in the table
SELECT score, COUNT(*) as NUMBER 
FROM second_table GROUP BY score