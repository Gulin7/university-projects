USE CFF
GO

UPDATE MoviesNominated
SET winner = 'Yes'
WHERE mid = 3

SELECT * FROM MoviesNominated 
-- let N = 2 so only country 

SELECT * FROM Movies

SELECT * FROM Movie_country

SELECT * FROM Countries

INSERT INTO Countries VALUES ( 1, 'Romania'), (2,'Ungaria');
INSERT INTO Movie_country VALUES (4, 1), (3,1), (2,2), (1,2); --country with cid 1 should appear

CREATE OR ALTER FUNCTION numberOfCountries (@total INT)
RETURNS INT 
BEGIN
	DECLARE @no INT
	SET @no=0
    SELECT C.cid, @no = COUNT(*) AS Wins
    FROM Countries C
    JOIN Movie_country MC ON C.cid = MC.cid
    JOIN MoviesNominated MN ON MC.mid = MN.mid
    WHERE MN.winner = 'Yes'
    GROUP BY C.cid
    HAVING COUNT(*) >= @total
	RETURN @no
END 
GO

CREATE OR ALTER FUNCTION numberOfCountries (@total INT)
RETURNS TABLE AS
RETURN
(
    SELECT C.cid, C.cname, COUNT(*) AS Wins
    FROM Countries C
    JOIN Movie_country MC ON C.cid = MC.cid
    JOIN MoviesNominated MN ON MC.mid = MN.mid
    WHERE MN.winner = 'Yes'
    GROUP BY C.cid, C.cname
    HAVING COUNT(*) >= @total
);

SELECT * FROM numberOfCountries(2);
