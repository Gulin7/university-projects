--Union and All
-- 
SELECT G.name,  G.price
FROM Games G
UNION
SELECT D.name, G.price
FROM DLCs D
INNER JOIN Games G ON D.game_id = G.game_id;

-- 
SELECT name, creator_id
FROM WorkshopItems
WHERE game_id = 8
UNION
SELECT name, value
FROM MarketItems
WHERE game_id = 8;

-- INTERSECT AND IN
SELECT game_id
FROM Games
INTERSECT
SELECT game_id
FROM DLCs;

SELECT name
FROM Games
WHERE developer_id IN (1,2,3);

--EXCEPT AND NOT IN
SELECT name, price
FROM Games
WHERE price NOT IN (40,60,420);

SELECT game_id
FROM Games G
EXCEPT
SELECT  game_id
FROM DLCs D
where game_id IS NOT NULL; -- games that have no dlc

-------
--4 queries with INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN
SELECT G.name, G.game_id
FROM Games G
RIGHT JOIN DLCs D ON G.game_id = D.game_id; -- games w dlc

SELECT G.name, G.game_id
FROM Games G
LEFT JOIN DLCs D ON G.game_id = D.game_id
LEFT JOIN MarketItems M ON G.game_id = M.game_id
WHERE D.game_id IS NULL AND M.game_id IS NULL; -- games w no market items and no dlc

SELECT G.name AS GameName
FROM Games G
INNER JOIN GamesGenre GN ON G.game_id = GN.game_id
WHERE GN.genre_id = 1; -- all action games (genre 1)

SELECT G.name AS GameName
FROM Games G
FULL JOIN GamesGenre GN ON G.game_id = GN.game_id
where GN.genre_id = 9; -- games that have genre id 9

--
-- Query 2: Using IN with nested subqueries
SELECT name
FROM DLCs
WHERE game_id IN (
    SELECT game_id
    FROM Games
    WHERE developer_id IN (
        SELECT developer_id
        FROM Developers
        WHERE developer_id = 2
    )
); -- dlcs from games made by developer 2

SELECT name
FROM Games
WHERE game_id IN (
    SELECT game_id
    FROM DLCs
    WHERE price > 10
); -- games with pricey dlcs

----f queries with the EXISTS operator and a subquery in the WHERE clause;
SELECT name
FROM Games G
WHERE EXISTS (
    SELECT 1
    FROM DLCs D
    WHERE D.game_id = G.game_id
    AND D.price > 10
); -- games with a pricey dlcs

SELECT name
FROM Games G
WHERE EXISTS (
    SELECT 1
    FROM DLCs D
    WHERE D.game_id = G.game_id
    AND EXISTS (
        SELECT 1
        FROM Developers Dev
        WHERE Dev.developer_id = 3
    )
); -- games w developer 3 and dlcs

--2 queries with a subquery in the FROM clause; 
SELECT AVG(a.avg_price)
FROM (
    SELECT game_id, AVG(price) as avg_price
    FROM DLCs
    GROUP BY game_id
) AS a; -- average dlc price

SELECT G.name, D.total_dlc_count
FROM Games G
INNER JOIN (
    SELECT game_id, COUNT(*) as total_dlc_count
    FROM DLCs
    GROUP BY game_id
) AS D ON G.game_id = D.game_id; -- dlc count for each game
--h. 4 queries with the GROUP BY clause, 3 of which also contain the HAVING clause; 2 of the latter 
-- will also have a subquery in the HAVING clause; use the aggregation operators: COUNT, SUM, AVG, MIN, MAX;

SELECT developer_id, COUNT(*) AS game_count
FROM Games
GROUP BY developer_id; -- games count by developer

SELECT developer_id, AVG(price) AS avg_price
FROM Games
GROUP BY developer_id
HAVING COUNT(*) >= 3; -- avg price by dlc with more than3 games

SELECT developer_id, AVG(price) AS avg_price
FROM Games
GROUP BY developer_id
HAVING AVG(price) > (SELECT AVG(price) FROM Games); -- developers with games above average (price-wise)

SELECT developer_id, COUNT(*) AS game_count, AVG(price) AS avg_price, SUM(price) AS total_price, MIN(price) AS min_price, MAX(price) AS max_price
FROM Games
GROUP BY developer_id; -- min, max, total, average prices for each developer and how many games they have

-- ANY AND ALL
SELECT name, price
FROM Games G
WHERE G.price >= ALL (SELECT price FROM Games); -- find most expensive games

SELECT name, price
FROM Games
WHERE price >= (SELECT max(price) FROM Games); -- rewritten with aggregation

SELECT name
FROM Games
WHERE price <= ANY (Select price FROM DLCs) -- games less expensive than some dlcs

SELECT name
FROM Games
where price <= (Select max(price) from DLCs) -- rewritten with aggregations

SELECT name
from Games
where price > (Select avg(price) from Games)

SELECT * FROM DLCs
SELECT * FROM Games




