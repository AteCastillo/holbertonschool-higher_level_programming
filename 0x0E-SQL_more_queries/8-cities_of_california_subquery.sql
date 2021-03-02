-- list all cities
USE hbtn_0d_usa;
SELECT * FROM cities WHERE state_id in (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
