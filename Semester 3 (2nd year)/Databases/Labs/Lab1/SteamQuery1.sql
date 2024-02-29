CREATE TABLE Users(
	user_id int PRIMARY KEY,
	username varchar(30)
	);

CREATE TABLE Developers(
	developer_id int PRIMARY KEY,
	name varchar(30)
	);

CREATE TABLE Genres(
	genre_id int PRIMARY KEY,
	name varchar(30)
	);

CREATE TABLE Games(
	game_id int PRIMARY KEY,
	name varchar(30),
	developer_id int not null,
	FOREIGN KEY(developer_id) References Developers(developer_id),
	date_of_release date,
	price int
	);

CREATE TABLE GamesGenre(
	genre_id int not null,
	FOREIGN KEY(genre_id) References Genres(genre_id),
	game_id int not null,
	FOREIGN KEY(game_id) References Games(game_id),
	PRIMARY KEY(game_id, genre_id)
	);

CREATE TABLE MarketItems(
	item_id int PRIMARY KEY,
	name varchar(30),
	value int not null,
	game_id int not null,
	FOREIGN KEY(game_id) References Games(game_id)
	);

CREATE TABLE WorkshopItems(
	item_id int PRIMARY KEY,
	name varchar(30),
	game_id int not null,
	FOREIGN KEY(game_id) References Games(game_id),
	creator_id int not null,
	FOREIGN KEY(creator_id) References Users(user_id)
	);

CREATE TABLE Library(
	user_id int not null,
	FOREIGN KEY(user_id) References Users(user_id),
	game_id int not null,
	FOREIGN KEY(game_id) References Games(game_id),
	PRIMARY KEY(user_id, game_id)
	);

CREATE TABLE DLCs(
	dlc_id int PRIMARY KEY,
	game_id int not null,
	FOREIGN KEY(game_id) References Games(game_id),
	name varchar(30),
	price int
	);

CREATE TABLE Sales(
	sale_id int PRIMARY KEY,
	game_id int not null,
	FOREIGN KEY(game_id) References Games(game_id),
	percentage DECIMAL(3,2),
	start_date date,
	end_date date
	);