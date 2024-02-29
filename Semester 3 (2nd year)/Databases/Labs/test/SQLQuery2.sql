CREATE DATABASE CFF
USE CFF

CREATE TABLE Countries (
	cid INT PRIMARY KEY,
	cname VARCHAR(55) UNIQUE
);

CREATE TABLE Genres (
	gid INT PRIMARY KEY,
	gname VARCHAR(55) UNIQUE
);

CREATE TABLE Movies (
	mid INT PRIMARY KEY,
	title VARCHAR(55),
	duration INT,
	premiere_date DATE
);

CREATE TABLE Actors (
	aid INT PRIMARY KEY,
	aname VARCHAR(55) UNIQUE,
	date_of_birth DATE
);

CREATE TABLE Awards(
	awid INT PRIMARY KEY,
	awname VARCHAR(55) UNIQUE,
	category VARCHAR(55) -- Movie or Actor
	);

CREATE TABLE ActorNominees(
	awid INT,
	aid INT, 
	FOREIGN KEY(awid) REFERENCES Awards(awid),
	FOREIGN KEY(aid) REFERENCES Actors(aid),
	winner VARCHAR(3) -- YES OR NO
	);

CREATE TABLE MoviesNominated(
	awid INT,
	mid INT, 
	FOREIGN KEY(awid) REFERENCES Awards(awid),
	FOREIGN KEY(mid) REFERENCES Movies(mid),
	winner VARCHAR(3) -- YES OR NO
	);

CREATE TABLE Plays_in(
	mid INT,
	aid INT,
	FOREIGN KEY(mid) REFERENCES Movies(mid),
	FOREIGN KEY(aid) REFERENCES Actors(aid)
	);

CREATE TABLE Born_in(
	cid INT,
	aid INT,
	FOREIGN KEY(cid) REFERENCES Countries(cid),
	FOREIGN KEY(aid) REFERENCES Actors(aid)
	);

CREATE TABLE Movie_genre(
	mid INT,
	gid INT,
	FOREIGN KEY(mid) REFERENCES Movies(mid),
	FOREIGN KEY(gid) REFERENCES Genres(gid)
	);

CREATE TABLE Movie_country(
	mid INT,
	cid INT,
	FOREIGN KEY(mid) REFERENCES Movies(mid),
	FOREIGN KEY(cid) REFERENCES Countries(cid)
	);

	--works