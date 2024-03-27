-- alter the table, add an average column then compute average score
ALTER TABLE second_table
ADD (average FLOAT);

SELECT AVG(average)
FROM second_table;
