-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT name
FROM genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
