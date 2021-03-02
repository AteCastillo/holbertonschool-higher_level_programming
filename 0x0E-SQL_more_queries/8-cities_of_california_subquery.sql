-- list all cities

SELECT * FROM cities WHERE state_id in (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
