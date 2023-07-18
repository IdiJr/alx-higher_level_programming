-- lists all records of the table second_list
-- excluding rows without name value
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;
