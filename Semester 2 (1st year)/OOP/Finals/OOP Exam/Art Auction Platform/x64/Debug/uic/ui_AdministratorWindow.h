/********************************************************************************
** Form generated from reading UI file 'AdministratorWindow.ui'
**
** Created by: Qt User Interface Compiler version 6.5.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_ADMINISTRATORWINDOW_H
#define UI_ADMINISTRATORWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_AdministratorWindowClass
{
public:
    QHBoxLayout *horizontalLayout_2;
    QVBoxLayout *verticalLayout_3;
    QVBoxLayout *verticalLayout;
    QListWidget *itemsList;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QComboBox *categoriesComboBox;
    QVBoxLayout *verticalLayout_2;
    QFormLayout *formLayout;
    QLabel *label_2;
    QLineEdit *nameInput;
    QLabel *label_3;
    QLineEdit *categoryInput;
    QLabel *label_4;
    QLineEdit *priceInput;
    QPushButton *addItemButton;
    QVBoxLayout *verticalLayout_4;
    QLabel *label_5;
    QListWidget *offersList;

    void setupUi(QWidget *AdministratorWindowClass)
    {
        if (AdministratorWindowClass->objectName().isEmpty())
            AdministratorWindowClass->setObjectName("AdministratorWindowClass");
        AdministratorWindowClass->resize(600, 400);
        horizontalLayout_2 = new QHBoxLayout(AdministratorWindowClass);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setObjectName("verticalLayout_3");
        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName("verticalLayout");
        itemsList = new QListWidget(AdministratorWindowClass);
        itemsList->setObjectName("itemsList");

        verticalLayout->addWidget(itemsList);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName("horizontalLayout");
        label = new QLabel(AdministratorWindowClass);
        label->setObjectName("label");

        horizontalLayout->addWidget(label);

        categoriesComboBox = new QComboBox(AdministratorWindowClass);
        categoriesComboBox->setObjectName("categoriesComboBox");

        horizontalLayout->addWidget(categoriesComboBox);


        verticalLayout->addLayout(horizontalLayout);


        verticalLayout_3->addLayout(verticalLayout);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setObjectName("verticalLayout_2");
        formLayout = new QFormLayout();
        formLayout->setSpacing(6);
        formLayout->setObjectName("formLayout");
        label_2 = new QLabel(AdministratorWindowClass);
        label_2->setObjectName("label_2");

        formLayout->setWidget(0, QFormLayout::LabelRole, label_2);

        nameInput = new QLineEdit(AdministratorWindowClass);
        nameInput->setObjectName("nameInput");

        formLayout->setWidget(0, QFormLayout::FieldRole, nameInput);

        label_3 = new QLabel(AdministratorWindowClass);
        label_3->setObjectName("label_3");

        formLayout->setWidget(1, QFormLayout::LabelRole, label_3);

        categoryInput = new QLineEdit(AdministratorWindowClass);
        categoryInput->setObjectName("categoryInput");

        formLayout->setWidget(1, QFormLayout::FieldRole, categoryInput);

        label_4 = new QLabel(AdministratorWindowClass);
        label_4->setObjectName("label_4");

        formLayout->setWidget(2, QFormLayout::LabelRole, label_4);

        priceInput = new QLineEdit(AdministratorWindowClass);
        priceInput->setObjectName("priceInput");

        formLayout->setWidget(2, QFormLayout::FieldRole, priceInput);


        verticalLayout_2->addLayout(formLayout);

        addItemButton = new QPushButton(AdministratorWindowClass);
        addItemButton->setObjectName("addItemButton");

        verticalLayout_2->addWidget(addItemButton);


        verticalLayout_3->addLayout(verticalLayout_2);


        horizontalLayout_2->addLayout(verticalLayout_3);

        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setSpacing(6);
        verticalLayout_4->setObjectName("verticalLayout_4");
        label_5 = new QLabel(AdministratorWindowClass);
        label_5->setObjectName("label_5");

        verticalLayout_4->addWidget(label_5);

        offersList = new QListWidget(AdministratorWindowClass);
        offersList->setObjectName("offersList");

        verticalLayout_4->addWidget(offersList);


        horizontalLayout_2->addLayout(verticalLayout_4);


        retranslateUi(AdministratorWindowClass);

        QMetaObject::connectSlotsByName(AdministratorWindowClass);
    } // setupUi

    void retranslateUi(QWidget *AdministratorWindowClass)
    {
        AdministratorWindowClass->setWindowTitle(QCoreApplication::translate("AdministratorWindowClass", "AdministratorWindow", nullptr));
        label->setText(QCoreApplication::translate("AdministratorWindowClass", "Filter:", nullptr));
        label_2->setText(QCoreApplication::translate("AdministratorWindowClass", "Name:", nullptr));
        nameInput->setText(QString());
        label_3->setText(QCoreApplication::translate("AdministratorWindowClass", "Category:", nullptr));
        categoryInput->setText(QString());
        label_4->setText(QCoreApplication::translate("AdministratorWindowClass", "Current price:", nullptr));
        priceInput->setText(QString());
        addItemButton->setText(QCoreApplication::translate("AdministratorWindowClass", "Add", nullptr));
        label_5->setText(QCoreApplication::translate("AdministratorWindowClass", "Offers:", nullptr));
    } // retranslateUi

};

namespace Ui {
    class AdministratorWindowClass: public Ui_AdministratorWindowClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_ADMINISTRATORWINDOW_H
