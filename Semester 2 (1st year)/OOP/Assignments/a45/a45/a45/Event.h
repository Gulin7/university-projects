#pragma once
#include <string>

typedef struct {
	int year, month, day;
}Date;

typedef struct {
	int hour, minute;
}Time;

class Event
{
private:
	std::string title;
	std::string description;
	Date date;
	Time time;
	int numberOfPeople;
	std::string link;

public:
	Event(): title(""), description(""), date({2023,4,5}), time({8,0}),numberOfPeople(0),link(""){}
	Event(std::string title,
		std::string description,
		Date date,
		Time time,
		int numberOfPeople,
		std::string link);
	std::string getTitle();
	std::string getDescription();
	Date getDate();
	Time getTime();
	int getNumberOfPeople();
	std::string getLink();

	void setTitle(std::string newTitle);
	void setDescription(std::string newDescription);
	void setDate(Date newDate);
	void setTime(Time newTime);
	void setNumberOfPeople(int newNumberOfPeople);
	void setLink(std::string newLink);

	bool operator==(const Event& eventToCheck);
	void operator=(const Event& eventToCopy);

	void showEvent();
};