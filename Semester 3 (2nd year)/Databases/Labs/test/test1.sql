CREATE TABLE MultipleChoiceTable (
	FK1 INT,
	FK2 INT, 
	C1 VARCHAR(69),
	C2 VARCHAR(420),
	C3 CHAR(2),
	C4 VARCHAR(69),
	C5 FLOAT,
	C6 INT, 
	PRIMARY KEY (FK1, FK2) );

INSERT INTO MultipleChoiceTable	VALUES 
		(1,1,'Umberto Tozzi','Gente di Mare','A1' ,'Music', 8.8, 10),
		(1,2, 'Metallica', 'Whiskey in the Jar', 'A2', 'Music', 8.9, 250),
		(1,3, 'UEFA', 'Chealsea vs Manchester City', 'A2', 'Sport', 7.1, 140),
		(1,4, 'UEFA', 'Real Madrid vs PSG', 'B3', 'Sport', 8.4, 100),
		(2,2, 'WTA', 'Roland Garros 2022 Final', 'B4', 'Sport', 9, 120),
		(2,3, 'Umberto Tozzi', 'Tu', 'A2', 'Music', 7, 135),
		(2,4, 'Peteson Craft', 'Minecraft Experiences', 'A1', 'Games', 5, 90),
		(2,5, 'WTA', 'US Open 2020 Final', 'C1', 'Sport', 7.6, 140),
		(3,3, 'CNN', 'Latest News 01.01.2024', 'A2', 'News', 6.8, 110),
		(3,4, 'CNN', 'Latest News 02.01.2024', 'D3', 'News', 6.2, 10),
		(4,2, 'Sting', 'Fields of Gold', 'D2', 'Music', 8.4, 30),
		(4,3, 'Metallica', 'Unforgiven', 'D1', 'Music', 5.3, 50),
		(4,4, 'ATP', 'Miami 2021 Semi-Final Highlights', 'A2', 'Sport', 8.8, 180);

SELECT * FROM MultipleChoiceTable;

DROP TABLE MultipleChoiceTable;

SELECT C4, AVG(C5) AvgC5, COUNT(C3) C3
FROM MultipleChoiceTable
WHERE C3 LIKE '%A_' OR C5<=7
GROUP BY C4
HAVING SUM(C6) >=350
--c) d)

SELECT *
FROM 
	( SELECT FK1, FK2, C5*10 C5
		FROM MultipleChoiceTable
		WHERE FK1>=FK2) r1
	LEFT JOIN (SELECT FK1, FK2, C5
		FROM MultipleChoiceTable
		WHERE C6 % 2 - 1 <0) r2 on r1.FK1 = r2.FK1 AND r1.FK2 = R2.FK2;
--		--b)

CREATE TRIGGER TrOnUpdate
ON MultipleChoiceTable
FOR UPDATE
AS
DECLARE @total INT = 0
SELECT @total = @total + SUM(i.C6-d.C6)
FROM deleted d INNER JOIN inserted i ON d.FK1=i.FK1 AND d.FK2 = i.FK2 
WHERE d.C6 <= i.C6
PRINT @total

UPDATE MultipleChoiceTable
SET C6 = 50
WHERE FK1 != FK2;
