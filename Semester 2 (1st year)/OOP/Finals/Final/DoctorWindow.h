#pragma once

#include <QMainWindow>
#include "ui_DoctorWindow.h"
#include "Controller.h"
#include "Observer.h"
#include "Doctor.h"
#include <QMessageBox>

class DoctorWindow : public QMainWindow, public Observer
{
	Q_OBJECT

public:
	DoctorWindow(Controller& controller, Doctor doc, QWidget *parent = nullptr);
	~DoctorWindow();

	void update() override;

	void populateList();

private:
	Ui::DoctorWindowClass ui;
	Controller& controller;
	Doctor doctor;
	bool boxChecked = false;

public slots:
	void addPatient();
	void updatePatient();
	void showCurrentPatients();
};
