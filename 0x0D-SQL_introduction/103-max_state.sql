-- displays max temperature of state ordered by the state name
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
