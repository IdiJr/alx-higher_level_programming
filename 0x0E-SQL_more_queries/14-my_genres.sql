-- lists all genres of the show DEXTER using the hbtn_0d_tvshows db
-- each record displays tv_genres.name sorted in ascending order of
-- genre name
SELECT tv_genres.name
  FROM tv_genres AS tv_genres
	 INNER JOIN tv_show_genres AS tv_show_genres
	     ON tv_genres.id = tv_show_genres.genre_id
	     INNER JOIN tv_shows AS tv_shows
	     ON tv_shows.id = tv_show_genres.show_id
	     WHERE tv_shows.title = 'Dexter'
 ORDER BY tv_genres.name;
