USE [Photography Chain]
GO

CREATE OR ALTER VIEW ViewEmployees
AS
	SELECT*
	FROM Employee
	Go

CREATE OR ALTER VIEW ViewEmployeesOnEvents
AS
	SELECT em.EMPLOYEE_ID, em.EMPLOYEE_NAME, ev.EVENT_ID
	FROM Employee em
	INNER JOIN Works_at wt ON wt.EMPLOYEE_ID = em.EMPLOYEE_ID
	INNER JOIN Event ev ON ev.EVENT_ID = wt.EVENT_ID
	GO

CREATE OR ALTER VIEW ViewEmployeeGroupByManager
AS
	SELECT ma.MANAGER_ID, em.EMPLOYEE_ID, em.EMPLOYEE_NAME
	FROM Employee em
	INNER JOIN Manager ma ON ma.MANAGER_ID = em.MANAGER_ID
	GROUP BY ma.MANAGER_ID, em.EMPLOYEE_ID, em.EMPLOYEE_NAME
	GO	
DELETE FROM [Works_at]
DELETE FROM [Employee]
DELETE FROM [Event]
DELETE FROM [Manager]
DELETE FROM [TestViews]
DELETE FROM [TestTables]

DELETE FROM [Views]
DBCC CHECKIDENT ('[Views]', RESEED, 1);

DELETE FROM [Tables]
DBCC CHECKIDENT ('[Tables]', RESEED, 1);

DELETE FROM [TestRunViews]
--DBCC CHECKIDENT ('[TestRunViews]', RESEED, 1);
DELETE FROM [TestRunTables]
--DBCC CHECKIDENT ('[TestRunTables]', RESEED, 1);


--SELECT* FROM TestRunTables
--SELECT* FROM TestRunViews


INSERT INTO Tables VALUES ('Event');
INSERT INTO Tables VALUES('Works_at');
INSERT INTO Tables VALUES('Employee');
--INSERT INTO Tables VALUES('Manager');
--Select* From Tables


INSERT INTO Views VALUES('ViewEmployees');
INSERT INTO Views VALUES('ViewEmployeesOnEvents');
INSERT INTO Views VALUES('ViewEmployeeGroupByManager');
--Select* From Views

--DELETE FROM Tests
--WHERE TestID >0
-------------------------------
-- Reset the identity value to 1
DELETE FROM [Tests];
DBCC CHECKIDENT ('[Tests]', RESEED, 1);
----------------------------------
INSERT INTO Tests VALUES('insertEmployee');
INSERT INTO Tests VALUES('insertEvent');
INSERT INTO Tests VALUES('insertWorksAt');
INSERT INTO Tests VALUES('deleteWorksAt');
INSERT INTO Tests VALUES('deleteEmployee');
INSERT INTO Tests VALUES('deleteEvent');
INSERT INTO Tests VALUES('insertEmployeeAndView');

--Select* From Tests

INSERT INTO TestViews VALUES(3, 2);
INSERT INTO TestViews VALUES(3, 3);
INSERT INTO TestViews VALUES(3, 4);
--SELECT* FROM TestViews

INSERT INTO TestTables VALUES(3, 2, 10000, 1);
INSERT INTO TestTables VALUES(2, 4, 10000, 2);
INSERT INTO TestTables VALUES(4, 3, 10000, 4);
INSERT INTO TestTables VALUES(5, 3, 10000, 5);
INSERT INTO TestTables VALUES(6, 4, 10000, 6);
INSERT INTO TestTables VALUES(7, 2, 10000, 7);
--SELECT* FROM TestTables

--UPDATE TestTables Set Position = 8 WHERE TestID = 9 AND TableID = 4
--INSERT INTO TestViews VALUES(3, 1);
--INSERT INTO TestViews VALUES(3, 2);
--INSERT INTO TestViews VALUES(3, 3);

--SELECT* FROM Views
--SELECT* FROM TestViews
--SELECT* FROM TestTables
--Select* From Tests
--Select* From Tables
GO

-----EMployee------
--Select* from Employee
--Go

CREATE OR ALTER PROCEDURE insertEmployeeAndView
AS
	EXEC insertEmployee
	--Select* From ViewEmployees
	Go
	
Go
CREATE OR ALTER PROCEDURE deleteEmployee
AS
	DELETE FROM Employee WHERE Employee.EMPLOYEE_ID > 0;

GO

CREATE OR Alter PROCEDURE insertEmployee
AS
	DECLARE @counter INT = 1
	DECLARE @row INT
	SELECT @row = NoOfRows FROM TestTables WHERE TestID = 3
	print(@row)
	WHILE @counter < @row
	BEGIN
		INSERT INTO Employee(EMPLOYEE_ID, MANAGER_ID) VALUES(@counter, @counter)
		SET @counter = @counter + 1
	END

Go


-----Event------
--Select* From Event
--Go

CREATE OR ALTER PROCEDURE deleteEvent
AS
	DELETE FROM Event WHERE EVENT_ID > 0;
Go

CREATE OR ALTER PROCEDURE insertEvent
AS
	DECLARE @counter INT = 1
	DECLARE @row INT
	SELECT @row = NoOfRows FROM TestTables WHERE TestID = 4
	print(@row)
	WHILE @counter < @row
	BEGIN
		INSERT INTO Event(EVENT_ID) VALUES(@counter)
		SET @counter = @counter + 1
	END	
GO

-----manager-------
--Select* from Manager
--go

CREATE OR ALTER PROCEDURE deleteManager
AS
	DELETE FROM Manager WHERE MANAGER_ID > 0
Go

CREATE OR ALTER PROCEDURE insertManager
AS
	DECLARE @counter INT = 1
	DECLARE @row INT
	print(@row)
	WHILE @counter < 10000
	BEGIN
		INSERT INTO Manager(MANAGER_ID) VALUES(@counter)
		SET @counter = @counter + 1
	END	
GO

----works at------
CREATE OR ALTER PROCEDURE deleteWorksAt
AS
	DELETE FROM Works_at WHERE Works_at.EMPLOYEE_ID > 0 OR Works_at.EVENT_ID > 0
	Go


	
CREATE OR ALTER PROCEDURE insertWorksAt
AS
	DECLARE @counter INT = 1
	DECLARE @row INT
	SELECT @row = NoOfRows FROM TestTables WHERE TestID = 4
	print(@row)
	WHILE @counter < @row
	BEGIN
		INSERT INTO Works_at VALUES(@counter, @counter)
		SET @counter = @counter + 1
	END	
GO

--SELECT* FROM Views
--SELECT* FROM TestRunViews
--SELECT* FROM TestRuns
--Go

CREATE OR ALTER PROC TestRunViewProc
AS
	DECLARE @start1 DATETIME;
	DECLARE @start2 DATETIME;
	DECLARE @start3 DATETIME;
	DECLARE @end1 DATETIME;
	DECLARE @end2 DATETIME;
	DECLARE @end3 DATETIME;
	
	
	SET @start1 = GETDATE();
	PRINT ('executing ViewEmployees')
	EXEC ('SELECT * FROM ViewEmployees');
	SET @end1 = GETDATE();
	INSERT INTO TestRuns VALUES ('test_view', @start1, @end1)
    INSERT INTO TestRunViews VALUES (@@IDENTITY, 2, @start1, @end1);

	
	SET @start2 = GETDATE();
	PRINT ('executing ViewEmployeesOnEvents')
	EXEC ('SELECT * FROM ViewEmployeesOnEvents');
	SET @end2 = GETDATE();
	INSERT INTO TestRuns VALUES ('test_view2', @start2, @end2)
    INSERT INTO TestRunViews VALUES (@@IDENTITY, 3, @start2, @end2);


	SET @start3 = GETDATE();
	PRINT ('executing ViewEmployeeGroupByManager')
	EXEC ('SELECT * FROM ViewEmployeeGroupByManager');
	SET @end3 = GETDATE();
	INSERT INTO TestRuns VALUES ('test_view3', @start3, @end3)
    INSERT INTO TestRunViews VALUES (@@IDENTITY, 4, @start3, @end3);

	Go



	----------------------------------------------------
	--Select* from Tests
	--SELECT* FROM TestRunTables
	Go
	----------------------------------------------
CREATE OR ALTER PROC TestRunTablesProc
AS 
	DECLARE @start1 DATETIME;
	DECLARE @start2 DATETIME;
	DECLARE @start3 DATETIME;
	DECLARE @start4 DATETIME;
	DECLARE @start5 DATETIME;
	DECLARE @start6 DATETIME;
	DECLARE @start7 DATETIME;

	DECLARE @end1 DATETIME;
	DECLARE @end2 DATETIME;
	DECLARE @end3 DATETIME;
	DECLARE @end4 DATETIME;
	DECLARE @end5 DATETIME;
	DECLARE @end6 DATETIME;
	DECLARE @end7 DATETIME;

	SET @start1 = GETDATE();
	PRINT('inserting data into employees ')
	EXEC dbo.insertEmployee;
	SET @end1 = GETDATE();
	INSERT INTO TestRuns VALUES ('test_insert_employees',@start1, @end1);
	INSERT INTO TestRunTables VALUES (@@IDENTITY, 2, @start1, @end1);--check 7

	--SET @start7 = GETDATE();
	--PRINT('running mix test')
	--EXEC dbo.insertEmployeeAndView
	--SET @end7 = GETDATE();
	--INSERT INTO TestRuns VALUES ('mix test',@start7, @end7);
	--INSERT INTO TestRunTables VALUES (@@IDENTITY, 6, @start7, @end7);
	------------------------
	SET @start3 = GETDATE();
	PRINT('inserting data into event')
	EXEC dbo.insertEvent;
	SET @end3 = GETDATE();
	INSERT INTO TestRuns VALUES ('test_insert_event',@start3, @end3);
	INSERT INTO TestRunTables VALUES (@@IDENTITY, 3, @start3, @end3);

	SET @start5 = GETDATE();
	PRINT('inserting data into worksAt')
	EXEC dbo.insertWorksAt;
	SET @end5 = GETDATE();
	INSERT INTO TestRuns VALUES ('test_insert_worksAt',@start5, @end5);
	INSERT INTO TestRunTables VALUES (@@IDENTITY, 4, @start5, @end5);

	SET @start6 = GETDATE();
	PRINT('deleting data from worksAt')
	EXEC dbo.deleteWorksAt;
	SET @end6 = GETDATE();
	INSERT INTO TestRuns VALUES ('test_delete_worksAt',@start6, @end6);
	INSERT INTO TestRunTables VALUES (@@IDENTITY, 5, @start6, @end6);

	SET @start4 = GETDATE();
	PRINT('deleting data from event')
	EXEC dbo.deleteEvent;
	SET @end4 = GETDATE();
	INSERT INTO TestRuns VALUES ('test_delete_event',@start4, @end4);
	INSERT INTO TestRunTables VALUES (@@IDENTITY, 7, @start4, @end4);

	SET @start2 = GETDATE();
	PRINT('deleting data from employees ')
	EXEC dbo.deleteEmployee;
	SET @end2 = GETDATE();
	INSERT INTO TestRuns VALUES ('test_delete_employees ',@start2, @end2);
	INSERT INTO TestRunTables VALUES (@@IDENTITY, 6, @start2, @end2);

	----------------------------------
	SET @start7 = GETDATE();
	PRINT('inserting data into employees ')
	EXEC insertEmployeeAndView
	SET @end7 = GETDATE();
	INSERT INTO TestRuns VALUES ('test_insert_employees',@start7, @end7);
	INSERT INTO TestRunTables VALUES (@@IDENTITY, 2, @start7, @end7);--check 7

Go

exec deleteManager

EXEC insertManager
EXEC TestRunTablesProc
EXEC TestRunViewProc

--DELETE FROM [Event]


SELECT* FROM TestRunTables
SELECT* FROM TestRunViews

SELECT* FROM TestRuns

