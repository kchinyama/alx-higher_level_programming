-- script lists records in second_table with a non-NUll value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY name DESC;
