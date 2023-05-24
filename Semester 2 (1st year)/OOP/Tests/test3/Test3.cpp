#include "Test3.h"
#include <QMessageBox>

Test3::Test3(Service service, QWidget *parent)
    : QMainWindow(parent), service(service)
{
    ui.setupUi(this);

    populateList();
}

Test3::~Test3()
{}

void Test3::populateList()
{
    ui.itemslistWidget->clear();
    for (auto& item : service.getAllItems()) {
        QListWidgetItem* qitem = new QListWidgetItem;
        qitem->setText(QString::fromStdString(item.itemToString()));
        ui.itemslistWidget->addItem(qitem);
    }
}

void Test3::showByCategory() {
    std::string category = ui.categorylineEdit->text().toStdString();
    ui.categorylistWidget->clear();
    if (category == "")
        return;
    if (service.getAllItemsCategory(category).size() == 0)
        QMessageBox::warning(this, QString::fromStdString("CATEGORY ERROR!"), QString::fromStdString("There are no items in the given category!"));
    else
        for (auto& item : service.getAllItemsCategory(category)) {
            QListWidgetItem* qitem = new QListWidgetItem;
            qitem->setText(QString::fromStdString(item.itemToString()));
            ui.categorylistWidget->addItem(qitem);
        }
}

void Test3::showByNameOrCategory()
{
    std::string toMatch = ui.searchlineEdit->text().toStdString();
    if (toMatch == "") {
        populateList();
        return;
    }
    ui.itemslistWidget->clear();
    for (auto& item : service.getAllItems()) {
        QListWidgetItem* qitem = new QListWidgetItem;
        qitem->setText(QString::fromStdString(item.itemToString()));
        if(item.getCategory().find(toMatch)!=std::string::npos || item.getName().find(toMatch) != std::string::npos)
            ui.itemslistWidget->addItem(qitem);
    }
}
