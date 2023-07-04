-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres m ON tv_shows.id = m.show_id
JOIN tv_genres t ON m.genre_id = t.id
WHERE t.name = 'Comedy'
ORDER BY tv_shows.title ASC;
