#pragma once

#include <QWidget>
#include "ui_SearchWindow.h"
#include "Observer.h"
#include "Service.h"

class SearchWindow : public QWidget, public Observer
{
	Q_OBJECT

public:
	SearchWindow(Service& service, QWidget *parent = nullptr);
	~SearchWindow();

public slots:
	void update() override;

private:
	Ui::SearchWindowClass ui;

	Service& service;
};
