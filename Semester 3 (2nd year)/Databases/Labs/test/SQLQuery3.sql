USE CFF
GO

CREATE OR ALTER PROCEDURE assignNominee (@awardID INT, @nomineeID INT) as
BEGIN
	DECLARE @category VARCHAR(55);
	SET @category=''

	SELECT @category = A.category
	FROM Awards a
	WHERE A.awid = @awardID

	-- found category	
	IF @category = 'Movie' 
		BEGIN
		DECLARE @count INT;
		SELECT @count = COUNT(*) FROM MoviesNominated MN WHERE MN.awid = @awardID AND MN.mid = @nomineeID
		IF @count = 0
			BEGIN
				INSERT INTO MoviesNominated
				VALUES (@awardID, @nomineeID, 'No');
			END;
		END;
	ELSE
		BEGIN
		DECLARE @count2 INT;
		SELECT @count2 = COUNT(*) FROM ActorNominees MN WHERE MN.awid = @awardID AND MN.aid = @nomineeID
		IF @count = 0
			BEGIN
				INSERT INTO ActorNominees
				VALUES (@awardID, @nomineeID, 'No');
			END;
		END;
END;
GO

--works