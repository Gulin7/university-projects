#include "Controller.h"

Controller::Controller()
{
    Surgery* department1 = new Surgery("Surgery1", 10, 2);
    HospitalDepartment* department2 = new Surgery("Surgery2", 1, 2);
    HospitalDepartment* department3 = new NeonatalUnit("NeonatalUnit1", 5, 10);
    HospitalDepartment* department4 = new NeonatalUnit("NeonatalUnit2", 3, 7.5);

    this->departments.push_back(department1);
    this->departments.push_back(department2);
    this->departments.push_back(department3);
    this->departments.push_back(department4);
}

bool Controller::addDepartment(HospitalDepartment* deparmentToAdd)
{
    for (auto& department : departments) {
        if (deparmentToAdd->getHospitalName() == department->getHospitalName())
            return false;
    }
    this->departments.push_back(deparmentToAdd);
    return true;
}

std::vector<HospitalDepartment*> Controller::getAllDepartments()
{
    return this->departments;
}

std::vector<HospitalDepartment*> Controller::getAllEfficientDepartments()
{
    std::vector<HospitalDepartment*> efficientDepartments;
    for (auto& department : departments) {
        if (department->isEfficient())
            efficientDepartments.push_back(department);
    }
     return efficientDepartments;
}

void Controller::writeToFile(std::string filename)
{
    std::ofstream output{ filename };
    if (!output.is_open())
        throw std::runtime_error("Cannot open file!");
    else {
        for (auto& department : departments) {
            output << department->toString();
        }
    }
}
