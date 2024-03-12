GO
Use Steam
GO


CREATE PROCEDURE addColumn(@TableName VARCHAR(50),@ColName VARCHAR(50), @ColType VARCHAR(50))
AS
	 DECLARE @SqlStatement NVARCHAR(MAX);

    -- Construct the ALTER TABLE statement dynamically
    SET @SqlStatement = 'ALTER TABLE ' + @TableName +
                        ' ADD ' + @ColName + ' ' + @ColType;

    -- Execute the dynamically generated SQL statement
    EXEC sp_executesql @SqlStatement;

	insert into versions values ('removeColumn '''+@TableName  +''', '''+@ColName+''' ');

GO


CREATE PROCEDURE removeColumn(@TableName VARCHAR(50),@ColName VARCHAR(50))
AS
	 DECLARE @SqlStatement NVARCHAR(MAX);
	 DECLARE @dt varchar(50);
	select @dt = DATA_TYPE from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = @TableName and COLUMN_NAME = @ColName;

    -- Construct the ALTER TABLE statement dynamically
    SET @SqlStatement = 'ALTER TABLE ' + @TableName +
                        ' DROP COLUMN ' +@ColName ;

    -- Execute the dynamically generated SQL statement
    EXEC sp_executesql @SqlStatement;
	
	insert into versions values ('addColumn '''+@TableName  +''', '''+@ColName+''', '''+@dt+'''');

GO

CREATE PROCEDURE modifyColumnType(@TableName VARCHAR(50),@ColName VARCHAR(50),@NewColType VARCHAR(50))
AS
	 DECLARE @SqlStatement NVARCHAR(MAX);
	 DECLARE @dt varchar(50);
	select @dt = DATA_TYPE from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = @TableName and COLUMN_NAME = @ColName;

    -- Construct the ALTER TABLE statement dynamically
    SET @SqlStatement = 'ALTER TABLE ' + @TableName +
                        ' ALTER COLUMN ' +@ColName +' '+ @NewColType;

    -- Execute the dynamically generated SQL statement
    EXEC sp_executesql @SqlStatement;
	insert into versions values ('modifyColumnType '''+@TableName  +''', '''+@ColName+''', '+@dt+'');

GO


CREATE PROCEDURE addDefault(@TableName VARCHAR(50),@ColName VARCHAR(50),@DefConsName VARCHAR(50),@DefValue VARCHAR(50))
AS
	 DECLARE @SqlStatement NVARCHAR(MAX);

    -- Construct the ALTER TABLE statement dynamically
    SET @SqlStatement = 'ALTER TABLE ' + @TableName +
                        ' ADD CONSTRAINT '+ @DefConsName +' DEFAULT ' +@DefValue +' FOR '+ @ColName;

    -- Execute the dynamically generated SQL statement
    EXEC sp_executesql @SqlStatement;
	insert into versions values ('removeConstraint '''+@TableName  +''', '''+@DefConsName+'''');
GO

CREATE PROCEDURE addPrimaryKey(@TableName VARCHAR(50),@ColName VARCHAR(50),@DefConsName VARCHAR(50))
AS
	 DECLARE @SqlStatement NVARCHAR(MAX);

    -- Construct the ALTER TABLE statement dynamically
    SET @SqlStatement = 'ALTER TABLE ' + @TableName +
                        ' ADD CONSTRAINT '+ @DefConsName +' PRIMARY KEY (' +@ColName +')';

    -- Execute the dynamically generated SQL statement
    EXEC sp_executesql @SqlStatement;
	insert into versions values ('removeConstraint '''+@TableName  +''', '''+@DefConsName+'''');

GO

CREATE PROCEDURE addCandidateKey(@TableName VARCHAR(50),@ColNames VARCHAR(50),@DefConsName VARCHAR(50))
AS
	 DECLARE @SqlStatement NVARCHAR(MAX);

    -- Construct the ALTER TABLE statement dynamically
    SET @SqlStatement = 'ALTER TABLE ' + @TableName +
                        ' ADD CONSTRAINT '+ @DefConsName +' UNIQUE (' +@ColNames +')';

    -- Execute the dynamically generated SQL statement
    EXEC sp_executesql @SqlStatement;
	insert into versions values ('removeConstraint '''+@TableName  +''', '''+@DefConsName+'''');

GO

CREATE PROCEDURE addForeignKey(@TableName VARCHAR(50),
@FColNames VARCHAR(50),@DefConsName VARCHAR(50),
@RefTableName VARCHAR(50), @RefCols VARCHAR(50))
AS
	 DECLARE @SqlStatement NVARCHAR(MAX);

    -- Construct the ALTER TABLE statement dynamically
    SET @SqlStatement = 'ALTER TABLE ' + @TableName +
                        ' ADD CONSTRAINT '+ @DefConsName +
						' FOREIGN KEY (' +@FColNames +')' + 
						'REFERENCES ' + @RefTableName + '(' + @RefCols + ')';

    -- Execute the dynamically generated SQL statement
    EXEC sp_executesql @SqlStatement;
	insert into versions values ('removeConstraint '''+@TableName  +''', '''+@DefConsName+'''');

GO

-- remove constraint is the opposite of all the constraint procedures
CREATE PROCEDURE removeConstraint(@TableName VARCHAR(50),@DefConsName VARCHAR(50))
AS
	 DECLARE @SqlStatement NVARCHAR(MAX);

    -- Construct the ALTER TABLE statement dynamically
    SET @SqlStatement = 'ALTER TABLE ' + @TableName +
                        ' DROP CONSTRAINT '+ @DefConsName ;

    -- Execute the dynamically generated SQL statement
    EXEC sp_executesql @SqlStatement;
	insert into versions values ('removeConstraint '''+@TableName  +''', '''+@DefConsName+'''');

GO

CREATE PROCEDURE addTable(@TableName VARCHAR(50))
AS
	DECLARE @SqlStatement NVARCHAR(MAX);

    -- Construct the ALTER TABLE statement dynamically
    SET @SqlStatement = 'CREATE TABLE ' + @TableName +
                        ' ( ID INT IDENTITY(1,1) );'

    -- Execute the dynamically generated SQL statement
    EXEC sp_executesql @SqlStatement;
	insert into versions values ('dropTable '''+@TableName  +'''');

GO

CREATE PROCEDURE dropTable(@TableName VARCHAR(50))
AS
	DECLARE @SqlStatement NVARCHAR(MAX);

    -- Construct the ALTER TABLE statement dynamically
    SET @SqlStatement = 'DROP TABLE ' + @TableName;
                        

    -- Execute the dynamically generated SQL statement
    EXEC sp_executesql @SqlStatement;
	insert into versions values ('addTable '''+@TableName  +'''');

GO

--test procedures
addTable 'Test';
select * from Test;
addColumn 'Test', 'price', 'INT';
addDefault 'Test', 'price', 'a', '100';
addColumn 'Test', 'age', 'INT';
removeColumn 'Test', 'price';
modifyColumnType 'Test', 'price', 'INT';
addPrimaryKey 'Test', 'id', 'P';
removeConstraint 'Test', 'P';
removeConstraint 'Test', 'a';
dropTable 'Test';
addColumn 'Test', 'marian', 'int';

delete from versions;
select * from versions;
restoreVersion '8';
select * from Test;

SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Test' and COLUMN_NAME = 'price'
SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Test' and COLUMN_NAME = 'age'
SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'Test' and COLUMN_NAME = 'id' -- check type and blabla
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS WHERE TABLE_NAME = 'Test' -- check for constraints
SELECT -- check if the defaults are ok 
    t.name AS TableName,
    c.name AS ColumnName,
    dc.name AS DefaultConstraintName,
    dc.definition AS DefaultDefinition
FROM
    sys.tables t
JOIN
    sys.default_constraints dc ON t.object_id = dc.parent_object_id
JOIN
    sys.columns c ON dc.parent_column_id = c.column_id AND t.object_id = c.object_id
WHERE
    t.name = 'Test';

drop table versions;
create table versions
(
	nr int PRIMARY KEY IDENTITY(1,1),
	actions nvarchar(255)
);

select * from versions order by nr desc;
--insert into versions values('Start ''a'' ');


create procedure restoreVersion(@v INT)
AS
	DECLARE @nr INT, @action NVARCHAR(255);

	DECLARE VersionCursor CURSOR FOR
		SELECT nr, actions
		From versions
		ORDER BY nr DESC
	OPEN VersionCursor
	
	FETCH VersionCursor INTO @nr, @action;
	IF @nr >= @v
	BEGIN
		EXEC sp_executesql @action;
	END

	WHILE @@FETCH_STATUS = 0
	BEGIN
		FETCH VersionCursor INTO @nr, @action;
		IF @nr >= @v
		BEGIN
			EXEC sp_executesql @action;
		END
	END

	CLOSE VersionCursor
	DEALLOCATE VersionCursor
GO
