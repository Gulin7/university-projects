#include "Exception.h"

Exception::Exception(const std::string& throwError) : error(throwError)
{
}

const char* Exception::what()
{
	return error.c_str();
}

ExceptionGUI::ExceptionGUI(const std::string& errors):errors{errors}
{
}

const char* ExceptionGUI::what()
{
	return errors.c_str();
}
