-- list tv shows
SELECT gen.name AS genre, COUNT(s.show_id) As number_of_shows
FROM tv_genres gen
INNER JOIN  tv_show_genres s
ON s.genre_id = gen.id
GROUP BY gen.name
HAVING
COUNT(s.show_id) > 0
ORDER BY number_of_shows DESC;