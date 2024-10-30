-- list all genres
SELECT genre.name AS genre, COUNT(tv_show_genre.tv_show_id) AS number_of_shows
FROM genre
JOIN tv_show_genre ON genre.id = tv_show_genre.genre_id
GROUP BY genre.name
HAVING COUNT(tv_show_genre.tv_show_id) > 0
ORDER BY number_of_shows DESC;
