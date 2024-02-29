#include "DoctorWindow.h"
#include "Controller.h"
#include "Observer.h"
#include "Doctor.h"

DoctorWindow::DoctorWindow(Controller& controller, Doctor doc, QWidget *parent)
	: controller(controller), doctor(doc), QMainWindow(parent)
{
	ui.setupUi(this);

	setWindowTitle(QString::fromStdString(this->doctor.getName()+" | Specialisation: " + this->doctor.getSpecialisation()));

	this->populateList();
}

DoctorWindow::~DoctorWindow()
{}

void DoctorWindow::update()
{
	this->populateList();
}

void DoctorWindow::populateList()
{
	ui.patientlistWidget->clear();

	for (auto& pat : controller.getAllPatientsForPopulate(doctor.getSpecialisation())) {
		QListWidgetItem* item = new QListWidgetItem(QString::fromStdString(pat.toString()));
		item->setData(Qt::UserRole, QString::fromStdString(pat.getName()));
		if (pat.getDoctor() == doctor.getName()) {
			QBrush brush(Qt::green);
			item->setBackground(brush);
		}
		ui.patientlistWidget->addItem(item);
	}
}

void DoctorWindow::addPatient() {
	string name = ui.namelineEdit->text().toStdString();
	string diagnosis = ui.diagnosislineEdit->text().toStdString();
	string specialisation = ui.specialisationlineEdit->text().toStdString();
	string doctor = ui.doctorlineEdit->text().toStdString();
	string date = ui.datelineEdit->text().toStdString();

	if (name == "" || date == "") {
		QMessageBox::warning(this, "Warning", QString::fromStdString("Invalid data or name! They cannot be empty, you dummy :p"));
		return;
	}
	
	Date ourDate;

	if(ourDate.fromString(date)==false) {
		QMessageBox::warning(this, "Warning", QString::fromStdString("Invalid data!"));
		return;
	}

	if (ourDate.year < 2023 || ourDate.year==2023 && ourDate.month<6 || ourDate.year == 2023 && ourDate.month == 6 && ourDate.day < 16) {
		QMessageBox::warning(this, "Warning", QString::fromStdString("Data in the past!"));
		return;
	}

	Patient pat(name, diagnosis, specialisation, doctor, ourDate);
	QMessageBox::warning(this, "good", QString::fromStdString(pat.toString()));

	controller.addPatient(pat);
	controller.notify();
	controller.savePatientFile();
}

void DoctorWindow::updatePatient()
{
	string name = ui.patientlistWidget->currentItem()->data(Qt::UserRole).toString().toStdString();
	Patient patient = controller.getPatientByName(name);
	if (patient.getDiagonis() != "undiagnosed" && patient.getDoctor() != doctor.getName())
	{
		QMessageBox::warning(this, "Warning", QString::fromStdString("Can't update that patient!"));
		return;
	}
	string diagnosis = ui.updateDiagnosislineEdit->text().toStdString();
	string specialisation = ui.updateSpecialisationlineEdit->text().toStdString();

	if (diagnosis == "" || diagnosis == "undiagnosed") {
		QMessageBox::warning(this, "Warning", QString::fromStdString("Invalid diagnose!"));
		return;
	}
	string doctor = controller.getDoctorSpecialisation(specialisation);
	this->controller.updatePatient(name, diagnosis, specialisation, doctor);
	this->controller.notify();
	controller.savePatientFile();

}

void DoctorWindow::showCurrentPatients(){
	bool value = ui.patientcheckBox->isChecked();

	if(value){
		ui.patientlistWidget->clear();

		for (auto& pat : controller.getAllPatientsForDoctor(doctor.getName())) {
			QListWidgetItem* item = new QListWidgetItem(QString::fromStdString(pat.toString()));
			item->setData(Qt::UserRole, QString::fromStdString(pat.getName()));
			if (pat.getDoctor() == doctor.getName()) {
				QBrush brush(Qt::green);
				item->setBackground(brush);
			}
			ui.patientlistWidget->addItem(item);
		}
	}
	else {
		this->populateList();
	}
	controller.savePatientFile();
}
