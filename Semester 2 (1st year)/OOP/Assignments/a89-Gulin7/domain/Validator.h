#pragma once
#include <string>
#include <vector>

class Validator
{
public:
	bool checkStringIsInt(std::string givenString) {
		if (givenString.empty())
			return false;
        size_t currentIndex = 0;

        // Check for optional sign
        if (givenString[currentIndex] == '+' || givenString[currentIndex] == '-') {
            currentIndex++;
        }

        // Check each character to ensure it is a digit
        for (; currentIndex < givenString.length(); currentIndex++) {
            if (!isdigit(givenString[currentIndex])) {
                return false;
            }
        }

        return true;
	}

    std::string convertIntToString(int givenNumber) {
        return std::to_string(givenNumber);
    }
};

