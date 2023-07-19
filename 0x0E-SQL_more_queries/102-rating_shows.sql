-- list all shows in hbtn_0d_tvshows_rate,
-- displays tv_shows.title - rating sum in descending
-- order of rating sum
SELECT title, SUM(rate) AS rating
  FROM tv_shows
       INNER JOIN tv_show_ratings AS ratings
	   ON tv_shows.id = ratings.show_id
 GROUP BY title ORDER BY rating DESC;
