#include "stringOperations.h"

vector<string> splitString(string stringToSplit, char delimiter)
{
    vector<string> tokens;
    std::stringstream splitStream{ stringToSplit };
    string currentToken;

    while (std::getline(splitStream, currentToken, delimiter))
        tokens.push_back(stripString(currentToken));

    return tokens;
}

string stripString(string stringToStrip)
{
    int firstNonSpace = 0, lastNonSpace = stringToStrip.size() - 1;

    while (stringToStrip[firstNonSpace] == ' ')
        firstNonSpace++;

    while (stringToStrip[lastNonSpace] == ' ')
        lastNonSpace--;

    return stringToStrip.substr(firstNonSpace, lastNonSpace - firstNonSpace + 1);
}
