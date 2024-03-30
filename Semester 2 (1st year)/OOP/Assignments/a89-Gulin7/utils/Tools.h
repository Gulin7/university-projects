#pragma once
#include <string>
#include <vector>

/*
	Trims leading and trailing spaces from a string.
*/
std::string trim(const std::string& stringToTrim);

/*
	Tokenizes a string.
*/
std::vector<std::string> tokenize(const std::string& stringToTokenize, char delimiter);
