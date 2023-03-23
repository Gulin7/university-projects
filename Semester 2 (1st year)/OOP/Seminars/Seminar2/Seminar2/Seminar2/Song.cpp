#include "Song.h";

Song::Song(const std::string _artist, const std::string _title, const int _duration)
{
	this->artist = _artist;
	this->title = _title;
	this->duration = _duration;
}

std::string Song::getTitle() const
{
	return this->title;
}

std::string Song::getArtist() const
{
	return this->artist;
}

int Song::getDuration() const
{
	return this->duration;
}

void Song::setTitle(const std::string& title)
{
	this->title = title;
}

void Song::setArtist(const std::string& artist)
{
	this->artist = artist;
}

void Song::setDuration(const int& duration)
{
	this->duration = duration;
}
