#pragma once
#include "HospitalDepartment.h"

class Surgery:
	public HospitalDepartment
{
private:
	int numberOfPatients;
public:
	Surgery(std::string newName, int newNumberOfDoctors, int newNumberOfPatients) :
		HospitalDepartment{ newName, newNumberOfDoctors }, numberOfPatients{ newNumberOfPatients } {};
	int getNumberOfPatients();
	void setNumberOfPatients(int newNumberOfPatients);
	bool isEfficient() override;
	std::string toString() override;
};

