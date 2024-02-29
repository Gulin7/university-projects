#pragma once
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <exception>

using std::string;
using std::vector;
using std::exception;

struct Date {
	int day, month, year;
	string dateToString() {
		return std::to_string(day) + "." + std::to_string(month) + "." + std::to_string(year);
	}
	bool operator<(Date& compareDate) {
		if (this->year < compareDate.year)
			return true;
		if (this->month < compareDate.month)
			return true;
		if (this->day < compareDate.day)
			return true;
		return false;
	}
	bool fromString(string date) {
		std::stringstream ss(date);
		string token;
		vector<string> fields;
		while (std::getline(ss, token, '.')) {
			fields.push_back(token);
		}
		if (fields.size() != 3)
			return false;
		if (fields[0].empty() || fields[1].empty() || fields[2].empty())
			return false;
		try {
			this->day = std::stoi(fields[0]);
			this->month = std::stoi(fields[1]);
			this->year = std::stoi(fields[2]);
			return true;
		}
		catch (exception& e) {
			return false;
		}
	}
	bool compareWithOtherDate(Date date) {
		if (this->year < date.year)
			return true;
		if (this->month < date.month)
			return true;
		if (this->day < date.day)
			return true;
		return false;
	}
};

class Patient
{
private:
	string name, diagnosis, specialisationNeeded, doctor;
	Date date;
public:
	Patient(string name, string diagnosis, string spec, string doc, Date date):
		name(name), diagnosis(diagnosis), specialisationNeeded(spec), doctor(doc), date(date){}
	string getName() { return this->name; }
	string getDiagonis() { return this->diagnosis; }
	string getSpecialisationNeeded() { return this->specialisationNeeded; }
	string getDoctor(){ return this->doctor; }
	Date getDate(){ return this->date; }

	void setDiagnosis(string diag) {
		this->diagnosis = diag;
	}
	void setSpecialisationNeeded(string spec) {
		this->specialisationNeeded = spec;
	}

	void setDoctor(string doc) {
		this->doctor = doc;
	}

	string toString() { return "Name " + this->name + " Diag " + this->diagnosis + " Spec " + this->specialisationNeeded + " Doc: " + this->doctor + " Date" + this->date.dateToString(); }
	string toStringFile() { return this->name + ";" + this->diagnosis + ";" + this->specialisationNeeded + ";" + this->doctor + ";" + this->date.dateToString(); }
};

