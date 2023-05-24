#pragma once
#include "HospitalDepartment.h"
#include "NeonatalUnit.h"
#include "Surgery.h"
#include <fstream>
#include <exception>

class Controller
{
private:
	std::vector<HospitalDepartment*> departments;
public:
	Controller();
	bool addDepartment(HospitalDepartment* deparmentToAdd);
	std::vector<HospitalDepartment*> getAllDepartments();
	std::vector<HospitalDepartment*> getAllEfficientDepartments();
	void writeToFile(std::string filename);
};

