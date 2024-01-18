-- not my genres
SELECT gen.name
FROM tv_genres gen
WHERE gen.name NOT IN (
      SELECT gen.name
      FROM tv_genres gen
      INNER JOIN tv_show_genres ON gen.id = tv_show_genres.genre_id
      INNER JOIN tv_shows tv_shows ON tv_show_genres.show_id = tv_shows.id
      WHERE tv_shows.title = 'Dexter'
)
ORDER BY gen.name ASC;
