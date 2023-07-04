-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres m ON tv_genres.id = m.genre_id
JOIN tv_shows t ON m.show_id = t.id
WHERE t.title = 'Dexter'
ORDER BY tv_genres.name ASC;
