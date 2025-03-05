--  script that lists all records of the table
SELECT score, COUNT(name) as name
FROM second_table
GROUP BY score
ORDER BY score DESC;