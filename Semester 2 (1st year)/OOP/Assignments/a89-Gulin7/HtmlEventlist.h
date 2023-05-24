#pragma once
#include <iostream>
#include <fstream>
#include "FileEventlist.h"

class HtmlEventlist :
	public FileEventlist
{
private:
	void writeEventToHTMl(std::ostream& outputFile, Event& eventToWrite);
public:
	HtmlEventlist(const std::string& filename) : FileEventlist{ filename } {};
	void writeToFile() override;
	void displayEvents() override;
};

