-- lists all genres in hbtn_0d_tvshows and number of shows
-- linked to each other. Displays only genres with links and
-- sorted in descending order of number of linked shows
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
  FROM tv_genres AS tv_genres
	 INNER JOIN tv_show_genres AS tv_show_genres
	     ON tv_genres.id = tv_show_genres.genre_id
 GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
