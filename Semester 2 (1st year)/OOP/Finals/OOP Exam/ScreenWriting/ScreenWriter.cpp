#include "ScreenWriter.h"

ScreenWriter::ScreenWriter(string name, string expertise) :
    name{ name }, expertise{ expertise }
{
}

string ScreenWriter::getName()
{
    return this->name;
}

string ScreenWriter::getExpertise()
{
    return this->expertise;
}
