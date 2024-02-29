#include "Controller.h"

vector<Patient> Controller::getAllPatientsForDoctor(string doctorName)
{
    vector<Patient> patientsDoctor;
    for (auto& pat : this->patients) {
        if (pat.getDoctor() == doctorName)
            patientsDoctor.push_back(pat);
    }
    return patientsDoctor;
}

vector<Patient> Controller::getAllPatientsForPopulate(string spec)
{
    vector<Patient> patientsDoctor;
    for (auto& pat : this->patients) {
        if (pat.getSpecialisationNeeded() == spec || pat.getDiagonis()=="undiagnosed" )
            patientsDoctor.push_back(pat);
    }
    return patientsDoctor;
}

void Controller::addPatient(Patient pat)
{
    this->patients.push_back(pat);
    this->sortPatients();
}

void Controller::readFromFileDoctor()
{
    std::ifstream inputFile(this->doctorFile);
    string line;
    while (std::getline(inputFile, line)) {
        string token;
        vector<string>data;
        std::stringstream ss(line);
        while(std::getline(ss,token,';'))
			data.push_back(token);
        Doctor doc(data[0], data[1]);   
        this->doctors.push_back(doc);
    }
}

void Controller::readFromFilePatient()
{
    std::ifstream inputFile(this->patientFile);
    string line;
    while (std::getline(inputFile, line)) {
        string token;
        vector<string>data;
        std::stringstream ss(line);
        while (std::getline(ss, token, ';')) {
            data.push_back(token);
        }
        string date = data[4];
        string tokenDate;
        Date patientDate;
        vector<string> dateData;
        std::stringstream ssDate(date);
        while (std::getline(ssDate, tokenDate, '.'))
            dateData.push_back(tokenDate);
        if (data[1] == "") {
            data[1] = "undiagnosed";
        }
        if (data[1] == "undiagnosed") {
            data[2] = "";
            data[3] = "";
        }
        patientDate.day = std::stoi(dateData[0]);
        patientDate.month = std::stoi(dateData[1]);
        patientDate.year = std::stoi(dateData[2]);
        Patient patient{ data[0],data[1],data[2],data[3],patientDate };
        this->patients.push_back(patient);
    }
}

void Controller::savePatientFile()
{
    std::ofstream outputFile(this->patientFile);
    for(auto& pat : this->patients)
		outputFile << pat.toStringFile() << "\n";
}
