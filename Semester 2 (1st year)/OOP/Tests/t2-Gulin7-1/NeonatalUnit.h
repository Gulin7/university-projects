#pragma once
#include "HospitalDepartment.h"

class NeonatalUnit:
	public HospitalDepartment
{
private:
	double averageGrade;
public:
	NeonatalUnit(std::string newName, int newNumberOfDoctors, double newAverageGrade) :
		HospitalDepartment{ newName, newNumberOfDoctors }, averageGrade{ newAverageGrade } {};
	double getAverageGrade();
	void setAverageGrade(double newAverageGrade);
	bool isEfficient() override;
	std::string toString() override;
};

