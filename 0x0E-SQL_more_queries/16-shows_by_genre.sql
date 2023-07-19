-- list all shows in hbtn_0d_tvshows db and linked genres
-- shows without genre display NULL
SELECT shows.title, tv_genres.name
  FROM tv_shows AS shows
	 LEFT JOIN tv_show_genres AS show_genres
	     ON shows.id = show_genres.show_id
	     LEFT JOIN tv_genres
	     ON show_genres.genre_id = tv_genres.id
ORDER BY shows.title, tv_genres.name;
