-- lists all cities contained in db hbtn_0c_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name
  FROM cities AS cities
	 INNER JOIN states AS states ON cities.state_id = states.id
ORDER BY cities.id;
