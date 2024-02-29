USE CFF
GO

CREATE OR ALTER VIEW ActorsInNominatedMovies
AS
	SELECT DISTINCT A.aname AS ActorName
	FROM Actors A
	JOIN Plays_in P ON A.aid = P.aid
	JOIN MoviesNominated MN ON P.mid = MN.mid;
GO

SELECT * FROM ActorsInNominatedMovies

INSERT INTO Actors VALUES
(1, 'Tudor Gulin', '2024-01-01'),
(2, 'Florin Salam', '2024-01-01'),
(3, 'Tudor Gulinul', '2024-01-01'),
(4, 'Tudor Gulinescu', '2024-01-01');

INSERT INTO Movies VALUES
( 1, 'Movie 1', 5, '2024-01-02'),
( 2, 'Movie 2', 6, '2024-01-02'),
( 3, 'Movie 3 ', 7, '2024-01-02'),
( 4, 'Movie 4 ', 8, '2024-01-02');

INSERT INTO Awards VALUES
 (1,'Award 1', 'Movie'),
 (2,'Award 2', 'Movie'),
 (3,'Award 3', 'Movie');

 INSERT INTO Plays_in VALUES
 (1,1),
 (3,4),
 (4,1),
 (4,2);

 INSERT INTO Plays_in VALUES
(2,3);

EXEC assignNominee 1, 1
EXEC assignNominee 2, 3
EXEC assignNominee 3, 4 --movie 2 is not nominated so actor 3 = Tudor Gulinul should be the one that doesnt appear
EXEC assignNominee 2, 4
EXEC assignNominee 1, 4

SELECT * FROM MoviesNominated
 
 --works


