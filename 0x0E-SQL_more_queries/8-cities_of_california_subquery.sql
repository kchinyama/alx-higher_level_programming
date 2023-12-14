-- listing from 2 tables without the use of joins
SELECT id, name FROM cities
    WHERE state_id IN (SELECT id
    FROM states
    WHERE name = 'california') ORDER BY id;
