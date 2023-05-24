#include "Surgery.h"

int Surgery::getNumberOfPatients()
{
    return this->numberOfPatients;
}

void Surgery::setNumberOfPatients(int newNumberOfPatients)
{
    this->numberOfPatients = newNumberOfPatients;
}

bool Surgery::isEfficient()
{
    if (this->numberOfDoctors <= this->numberOfPatients / 2)
        return true;
    return false;
}

std::string Surgery::toString()
{
    std::string surgery=this->hospitalName+" "+std::to_string(this->numberOfDoctors)+" "+std::to_string(this->numberOfPatients) + "\n";
    return surgery;
}
