#pragma once
#include "Event.h"
#include "Repository.h"
#include <vector>
#include <string>
#include <iostream>
#include "Eventlist.h"
#include "Event.h"

class FileEventlist :
	public Eventlist
{
protected:
	std::string filename;
public:
	FileEventlist(const std::string& filename) : filename{ filename } {};
	virtual void writeToFile() = 0;
	virtual void displayEvents() = 0;
	std::string getFilename() {
		return this->filename;
	}
	void setFilename(std::string newFilename) {
		this->filename = newFilename;
	}
	virtual ~FileEventlist() {};
};