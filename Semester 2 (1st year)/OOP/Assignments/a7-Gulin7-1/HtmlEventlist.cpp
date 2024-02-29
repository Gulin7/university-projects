#include "HtmlEventlist.h"
#include "FileEventlist.h"
#include "Event.h"
#include "Eventlist.h"
#include <iostream>
#include <fstream>
#include <exception>
#include <string>
#include <vector>
#include <Windows.h>
#include "Exception.h"

void HtmlEventlist::writeEventToHTMl(std::ostream& outputFile, Event& eventToWrite)
{
    outputFile
        << "        <tr>\n"
        << "            <td>" << eventToWrite.getTitle() << "</td>" << std::endl
        << "            <td>" << eventToWrite.getDescription() << "</td>" << std::endl
        << "            <td>" << eventToWrite.getDate().day << ":" << eventToWrite.getDate().month << ":"<< eventToWrite.getDate().year << "</td>" << std::endl
        << "            <td>" << eventToWrite.getTime().hour << ":" << eventToWrite.getTime().minute << std::endl
        << "            <td>" << eventToWrite.getNumberOfPeople() << "</td>" << std::endl
        << "            <td>" << "<a href=\"" << eventToWrite.getLink() << "\">" << "Link" << "</a>" << "</td>" << std::endl
        << "        </tr>" << std::endl;
}

void HtmlEventlist::writeToFile()
{
    std::ofstream outputFile{ filename };
    if (!outputFile.is_open())
        throw Exception{ "File not opened!" };
    outputFile << "<!DOCTYPE html>\n"
        << "<html>\n"
        << "    <head>\n"
        << "        <title> Events </title>\n"
        << "    </head>\n"
        << "<body>\n"
        << "    <table border = ""1"">\n"
        << "        <tr>\n"
        << "            <td>" << "Title" << "</td>" << std::endl
        << "            <td>" << "Description" << "</td>" << std::endl
        << "            <td>" << "Date" << "</td>" << std::endl
        << "            <td>" << "Time" << "</td>" << std::endl
        << "            <td>" << "NumberOfPeople" << "</td>" << std::endl
        << "            <td>" << "Link" << "</td>" << std::endl
        << "        </tr>" << std::endl;
    for (auto& currentEvent : events)
        this->writeEventToHTMl(outputFile, currentEvent);
    outputFile << "</table>\n"
        << "</body>\n"
        << "</html>\n";
    outputFile.close();
}

void HtmlEventlist::displayEvents()
{
    char buffer[MAX_PATH];
    GetCurrentDirectoryA(MAX_PATH, buffer);
    std::string path(buffer);
    path += "\\" + filename;
        std::string command = "start \"\" \"" + path + "\"";
    system(command.c_str());
}
