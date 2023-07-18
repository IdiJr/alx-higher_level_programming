-- groups score and sort by number of occurance in
-- descending order from second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
