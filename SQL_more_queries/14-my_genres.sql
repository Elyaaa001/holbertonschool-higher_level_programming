-- import dump 
SELECT genre.name AS name
FROM genre
JOIN tv_show_genre ON genre.id = tv_show_genre.genre_id
JOIN tv_shows ON tv_show_genre.tv_show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genre.name ASC;
