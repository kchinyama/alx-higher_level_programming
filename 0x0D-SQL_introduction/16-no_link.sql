-- demo command that lists all records without a null entry
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
