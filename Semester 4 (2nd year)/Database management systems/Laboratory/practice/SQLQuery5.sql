USE PracticalExam

-- 1st transaction
BEGIN TRAN
UPDATE Brokerage SET name='Deadlock Broker' WHERE brokerId = 3

-- this transaction has exclusively lock on table Brokerage
WAITFOR DELAY '00:00:10'
UPDATE Cities SET name='Deadlock City' WHERE cityId = 2
-- this transaction will be blocked because transaction 2 has already blocked our lock on table Cities
COMMIT TRAN

SELECT * FROM Brokerage

SELECT * FROM Cities

