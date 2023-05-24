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
