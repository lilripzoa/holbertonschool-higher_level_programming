-- print the description of the table first_table from the database
SELECT *
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA ='hbtn_0c_0' AND TABLE_NAME = 'first_table';