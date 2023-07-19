-- lists all genres in the db hbtn_0d_tvshows_rate by their rating
SELECT name, SUM(rate) AS rating
  FROM tv_genres
       INNER JOIN tv_show_genres
	   ON tv_genres.id = tv_show_genres.genre_id
	   INNER JOIN tv_show_ratings AS ratings
	   ON tv_show_genres.show_id = ratings.show_id
 GROUP BY name ORDER BY rating DESC;
