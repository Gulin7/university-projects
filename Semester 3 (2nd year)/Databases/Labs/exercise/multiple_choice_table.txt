CREATE TABLE MultipleChoiceTable (
	FK1 INT,
	FK2 INT, 
	C1 VARCHAR(69),
	C2 VARCHAR(420),
	C3 INT,
	C4 INT,
	C5 CHAR(2),
	PRIMARY KEY (FK1, FK2) );

INSERT INTO MultipleChoiceTable
VALUES (1,1,'a','b',1,1,'cc');

SELECT * FROM MultipleChoiceTable;

DROP TABLE MultipleChoiceTable;
