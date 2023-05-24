#include "Exception.h"

Exception::Exception(const std::string& throwError) : error(throwError)
{
}

const char* Exception::what()
{
	return error.c_str();
}
