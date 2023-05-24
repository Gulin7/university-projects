#pragma once
#include "FileEventlist.h"
#include <string>

class CsvEventlist :
	public FileEventlist
{
public:
	CsvEventlist(const std::string& filename) : FileEventlist{ filename } {};
	void writeToFile() override;
	void displayEvents() override;
};
