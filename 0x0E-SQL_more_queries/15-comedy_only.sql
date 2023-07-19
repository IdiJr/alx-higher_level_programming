-- lists all Comedy shows in the hbtn_0d_tvshows db
-- displays the tv_shows.title
SELECT shows.title
  FROM tv_shows AS shows
	 INNER JOIN tv_show_genres AS show_genres
	     ON shows.id = show_genres.show_id
	     INNER JOIN tv_genres
	     ON tv_genres.id = show_genres.genre_id
	     WHERE tv_genres.name = 'Comedy'
 ORDER BY shows.title;
