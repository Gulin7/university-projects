#include "NeonatalUnit.h"

double NeonatalUnit::getAverageGrade()
{
    return this->averageGrade;
}

void NeonatalUnit::setAverageGrade(double newAverageGrade)
{
    this->averageGrade = newAverageGrade;
}

bool NeonatalUnit::isEfficient()
{
    return this->averageGrade>8.5;
}

std::string NeonatalUnit::toString()
{
    std::string neonatalUnit = this->hospitalName + " " + std::to_string(this->numberOfDoctors) + " " + std::to_string(this->averageGrade)+"\n";
    return neonatalUnit;
}
