-- demo that dipslays number of records with id = 89
SELECT id, SUM(id=89) as Total FROM first_table GROUP BY id;
