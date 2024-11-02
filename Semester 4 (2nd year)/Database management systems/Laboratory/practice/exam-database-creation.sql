CREATE DATABASE PracticalExam

USE PracticalExam

CREATE TABLE Cities(
	cityId INT PRIMARY KEY,
	name VARCHAR(255),
	country VARCHAR(255)
);

CREATE TABLE Brokerage(
	brokerId INT PRIMARY KEY,
	name VARCHAR(255),
	numberEmployees INT
);

CREATE TABLE CitiesBrokerage(
	cityId INT,
	brokerId INT,
	FOREIGN KEY (cityId) REFERENCES Cities(cityId),
	FOREIGN KEY (brokerId) REFERENCES Brokerage(brokerId),
	PRIMARY KEY (cityId, brokerId),
)

CREATE TABLE Clients(
	clientId INT PRIMARY KEY,
	name VARCHAR(255),
	birthDate DATE,
	registrationDate DATE,
	country VARCHAR(255),
	brokerId INT
	FOREIGN KEY (brokerId) REFERENCES Brokerage(brokerId)
);

CREATE TABLE Products(
	productId INT PRIMARY KEY,
	name VARCHAR(255),
	price float, 
	marketRelease DATE,
	brokerId INT,
	FOREIGN KEY (brokerId) REFERENCES Brokerage(brokerId),
)

create table ProductsClients(
	brokerId int foreign key REFERENCES Brokerage(brokerId),
	productId int foreign key references Products(productId),
	clientId int foreign key references Clients(clientId),

)

SELECT * FROM Clients

SELECT * FROM Cities

INSERT INTO Cities(cityId, name, country) VALUES
(1, 'BaiaMare', 'Romania'),
(2, 'Cluj-Napoca', 'Romania'),
(3, 'Berlin', 'Germany')

SELECT * FROM Brokerage

INSERT INTO Brokerage(brokerId, name, numberEmployees) VALUES
(3, 'Broker3', 8),
(4, 'Broker4', 2)

INSERT INTO CitiesBrokerage(cityId, brokerId) VALUES
(3, 3),
(2, 4)

SELECT * FROM CitiesBrokerage

SELECT * FROM Clients

INSERT INTO Clients(clientId, name, birthDate, registrationDate, country, brokerId) VALUES
(1, 'Gulin Tudor', '1980-04-15', '2023-01-10', 'Romania', 1),
(2, 'Rares Dan', '1990-07-22', '2023-02-20', 'Romania', 2),
(3, 'Maxonescu', '1975-11-30', '2023-03-05', 'Germania', 3),
(4, 'Armin', '1977-11-30', '2022-03-05', 'Romania', 4)


INSERT INTO Products (productId, name, price, marketRelease, brokerId)
VALUES 
(1, 'Product A', 100.0, '2022-01-15', 1),
(2, 'Product B', 150.0, '2022-05-20', 2),
(3, 'Product C', 200.0, '2022-08-30', 3);


-- Dirty Read -> reading uncommited data = T1 writes A and then T2 reads A, before T1 has time to commit
-- Dirty Read Solution -> SET TRANSACTION ISOLATION LEVEL READ COMMITED (READ UNCOMMITED IS THE LOWEST ISO LVL)

-- Update Conflict/Unrepeatable Reads -> one transaction updates and the other reads BEFORE & AFTER the update, seeing different data
-- Update Conflict Solution -> SET TRANSACTION ISOLATION LEVEL REPEATABLE READ (serializable would work too)

-- Blind Writes -> T1 writes A and then T2 overwrites A before T1 commits
-- Blind Writes Solution -> obtain an xlock and release it uppon commit idk (?)

-- Phantom Read -> T1 reads then T2 insets then T1 reads again, and now there's a new value
-- Phantom Read Solution -> SET TRANSACTION ISOLATION LEVEL SERIALIZABLE 

-- Deadlock -> T1 has an lock on object O1 and waits for object O2; T2 has the lock on object O2 and waits for object O1;
