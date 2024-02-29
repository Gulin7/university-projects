#pragma once
#include "Subject.h"
#include "Patient.h"
#include "Doctor.h"

class Controller:
	public Subject
{
private:
	vector<Doctor> doctors;
	vector<Patient> patients;
	string doctorFile, patientFile;
public:
	Controller(string docF, string patF) : doctorFile(docF), patientFile(patF) {
		this->readFromFileDoctor();
		this->readFromFilePatient();
		//std::sort(patients.begin(), patients.end(), []( Patient& p1,  Patient& p2) { return p1.getDate().compareWithOtherDate(p2.getDate()); });
	}

	vector<Doctor> getAllDoctors() { return this->doctors; }
	vector<Patient> getAllPatients() { return this->patients; }

	vector<Patient> getAllPatientsForDoctor(string doctorName);

	vector<Patient> getAllPatientsForPopulate(string doctorName);

	void sortPatients() {
		return;
	}

	Patient getPatientByName(string name) {
		for (auto& pat : this->patients)
			if (pat.getName() == name)
				return pat;
		Date mydate;
		mydate.year = 2023;
		mydate.month = 6;
		mydate.day = 16;

		return Patient{ "","","","",mydate};
	}

	string getDoctorSpecialisation(string spec) {
		for (auto& doc : doctors) {
			if (doc.getSpecialisation() == spec)
				return doc.getName();
		}
		return "";
	}
	void updatePatient(string name, string diagnosis, string specialisation, string doc) {
		for (auto& pat : patients) {
			if (pat.getName() == name) {
				pat.setDiagnosis(diagnosis);
				pat.setSpecialisationNeeded(specialisation);
				pat.setDoctor(doc);
				return;
			}
		}
		this->sortPatients();
		
	}

	void addPatient(Patient pat);

	void readFromFileDoctor();
	void readFromFilePatient();
	void savePatientFile();
};
