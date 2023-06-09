-- this script demonstrates a list of records with the same score on a table
SELECT score, COUNT(score)
AS number
FROM second_table GROUP BY score DESC;
