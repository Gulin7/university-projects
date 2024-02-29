#include "CsvEventlist.h"
#include <fstream>
#include <exception>
#include <Windows.h>
#include <shellapi.h>
#include <iostream>

void CsvEventlist::writeToFile()
{
	std::ofstream outputFile{ filename };
	if (!outputFile.is_open())
		throw std::runtime_error{ "File not opened!" };
	for (const auto& currentEvent : events)
		outputFile << currentEvent;
	outputFile.close();
}

void CsvEventlist::displayEvents()
{
	ShellExecuteA(NULL,
		"open",
		"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
		filename.c_str(),
		NULL,
		SW_MAXIMIZE
	);
}
