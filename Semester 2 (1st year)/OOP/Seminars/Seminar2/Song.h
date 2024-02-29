#pragma once
#include <string>

class Song {
private:
	std::string artist;
	std::string title;
	int duration;

public:
	Song(const std::string _artist, 
		const std::string _title, 
		const int _duration);

	std::string getTitle() const;
	std::string getArtist() const;
	int getDuration() const;

	void setTitle(const std::string& title);
	void setArtist(const std::string& artist);
	void setDuration(const int& duration);
};