#pragma once
#include <exception>
#include <string>

class Exception : public std::exception
{
protected:
	std::string error;
public:
	Exception(const std::string& throwError);
	virtual const char* what();
};

class ExceptionGUI : public std::exception {
protected:
	std::string errors;
public:
	ExceptionGUI(const std::string& errors);
	virtual const char* what();
};