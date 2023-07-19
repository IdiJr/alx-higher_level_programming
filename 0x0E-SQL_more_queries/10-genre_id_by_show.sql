-- lists all shows in db hbtn_0d_tvshows
-- and should tv_shows.title and tv_show_genres.genre_id
-- must be sorted by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows AS tv_shows
	 INNER JOIN tv_show_genres AS tv_show_genres
	     ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
