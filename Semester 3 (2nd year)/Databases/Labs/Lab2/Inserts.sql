-- Developers
INSERT INTO Developers (developer_id, name)
VALUES
    (1, 'Valve Corporation'),
    (2, 'CD Projekt Red'),
    (3, 'Bethesda Game Studios'),
    (4, 'Ubisoft'),
    (5, 'Epic Games'),
    (6, 'Rockstar Games'),
    (7, 'Devolver Digital'),
    (8, 'Klei Entertainment'),
    (9, 'Supergiant Games'),
    (10, 'Paradox Interactive');

--Games
INSERT INTO Games (game_id, name, developer_id, date_of_release, price)
VALUES
	(1, 'Far Cry 6', 4, '2022-12-10', 50),
	(2, 'Watch Dogs: Legions', 4, '2022-2-5', 40),
	(3, 'Trackmania', 4, '2020-05-16', 20),
	(4, 'Cyberpunk', 2, '2022-11-5', 70),
	(5, 'The Witcher', 2, '2016-05-27', 15),
	(6, 'Half-life', 1, '1998-03-05', 20),
	(7, 'Portal 2', 1, '2011-07-13', 15),
	(8, 'Counter-Strike 2', 1, '2023-10-05', 20);

--Users
INSERT INTO Users(user_id, username)
VALUES
	(1, 'Goblinu'),
	(2, 'Maxon'),
	(3, 'ULTIMATEKNIGHT69'),
	(4, 'KingSlayer'),
	(5, 'sbbogdy'),
	(6, 'deinocheirus'),
	(7, 'gulin27'),
	(8, 'yokai'),
	(9, 'CATALIN21FEB'),
	(10, 'Keratin'),
	(11, 'KERATIN REFORMED');

INSERT INTO Library(user_id, game_id)
VALUES
	(1,3),
	(2,5),
	(6,7),
	(3,4),
	(3,8),
	(4,1),
	(5,2),
	(6,3),
	(7,5),
	(7,4),
	(8,8),
	(9,7),
	(10,6),
	(7,2),
	(10,5),
	(6,6),
	(5,1);

INSERT INTO DLCs(dlc_id, game_id, name, price)
VALUES
	(1, 1, 'Ultimate', 15),
	(2, 2, 'Power', 5),
	(3, 3, 'DLC PowerHouse', 10),
	(4, 4, 'DLC 1', 5),
	(5, 5, 'Final Battle', 5);

INSERT INTO Genres(genre_id, name)
VALUES
	(1, 'Action'),
	(2, 'Rogue-like'),
	(3, 'RPG'),
	(4, 'Adventure'),
	(5, 'FPS'),
	(6, 'Multiplayer'),
	(7, 'Singleplayer'),
	(8, 'Co-op'),
	(9, 'Strategy');

INSERT INTO GamesGenre(genre_id, game_id)
VALUES
	(1, 1),
	(1, 2),
	(1, 5),
	(1, 6),
	(1, 8),
	(5, 1),
	(5, 6),
	(5,8),
	(6, 8),
	(6, 7),
	(7, 6),
	(7, 7),
	(7, 5),
	(7, 4),
	(7, 3),
	(7, 2),
	(7, 1);

INSERT INTO Sales(sale_id, game_id, percentage, start_date, end_date)
VALUES
	(1, 1, 0.10, '2022-12-01','2022-12-28'),
	(2, 2, 0.15, '2022-12-01','2022-12-28'),
	(3, 3, 0.50, '2023-06-01','2023-06-30'),
	(4, 6, 0.40, '2023-06-01','2023-06-30'),
	(5, 8, 0.20, '2023-12-01','2023-12-28');

INSERT INTO MarketItems(item_id, name, value, game_id)
VALUES
	(1, 'AK-47 Legion of Anubis', 100, 8),
	(2, 'AWP Neo-Noir', 420, 8),
	(3, 'AK-47 Frontside Misty', 69, 8),
	(4, 'M4A1-S Decimator', 40, 8),
	(5, 'AWP Chromatic Aberration', 25, 8);

INSERT INTO WorkshopItems(item_id, name, creator_id, game_id)
VALUES
	(1, 'Dust2 Reforged', 2, 8),
	(2, 'AWP 1V1', 3, 8);

UPDATE WorkshopItems
Set name = 'Dust 2 Reforged'
where item_id = 1;

UPDATE DLCs
Set name ='DLC GOLDEN POWER ULTIMATE'
where dlc_id =4;

UPDATE MarketItems
Set value = 30
where name = 'M4A1-S Decimator';

UPDATE Sales
Set percentage = 0.20
where sale_id = 1;

DELETE FROM DLCs 
where dlc_id = 5;

DELETE FROM Library
where user_id = 11;

DELETE FROM Users
where user_id = 11;

INSERT INTO GamesGenre(genre_id, game_id)
VALUES
	(9,3);