#pragma once
#include <string>
#include <vector>

class HospitalDepartment
{
protected:
	std::string hospitalName;
	int numberOfDoctors;
public:
	HospitalDepartment(std::string newName, int newNumber) : hospitalName{ newName }, numberOfDoctors{ newNumber } {};
	std::string getHospitalName();
	int getNumberOfDoctors();
	virtual bool isEfficient() = 0;
	virtual std::string toString() = 0;
};

