USE PracticalExam

-- 2nd transaction
BEGIN TRAN
SET DEADLOCK_PRIORITY HIGH --solution
UPDATE Cities SET name='Arasda' WHERE cityId = 2
-- this transaction has exclusively lock on table Cities
WAITFOR DELAY '00:00:10'
UPDATE Brokerage SET name='asdas asda' WHERE brokerId = 3
-- this transaction will be blocked because transaction 1 has exclusively lock on table Brokerage, so, both of the transactions are blocked
COMMIT TRAN

SELECT * FROM Brokerage

SELECT * FROM Cities

-- deadlock prevent
-- each transaction is given a timestamp
-- if Ti waits for Tj then WAIT-DIE => Ti higher priority -> waits else Ti dies
-- WOUND-Wait - if Ti has higher priority => Tj dies, else Ti waits

