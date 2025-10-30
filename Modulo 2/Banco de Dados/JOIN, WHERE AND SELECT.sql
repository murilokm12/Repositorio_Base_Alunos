SELECT * FROM Track

INNER JOIN  Genre ON Genre.GenreId = Track.GenreId

WHERE Genre.Name = 'Rock'
