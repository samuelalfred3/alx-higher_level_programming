-- Selecting genres that are not linked to the show "Dexter"
-- Subquery to get the ID of the show "Dexter"

SELECT name
FROM tv_genres
-- Using NOT IN to filter out genres that are linked to "Dexter"
WHERE name NOT IN
(SELECT name
	FROM tv_genres
	LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = 'Dexter')
GROUP BY name
ORDER BY name ASC;

