-- List all genres from 'hbtn_0d_tvshows' and display number of shows linked to each
-- Each record should display tv_genres.name, number of shows
-- Don't display a genre that doesn't have any shows linked
-- Results must be sorted descending order by number of shows linked
-- Can only use one SELECT statement
SELECT name AS genre, COUNT(id) AS number_of_shows
FROM tv_genres INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name
ORDER BY number_of_shows DESC;
