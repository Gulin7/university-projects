/********************************************************************************
** Form generated from reading UI file 'CollectorWindow.ui'
**
** Created by: Qt User Interface Compiler version 6.5.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_COLLECTORWINDOW_H
#define UI_COLLECTORWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_CollectorWindowClass
{
public:
    QHBoxLayout *horizontalLayout_4;
    QHBoxLayout *horizontalLayout_3;
    QVBoxLayout *verticalLayout_2;
    QListWidget *itemsList;
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QComboBox *categoriesComboBox;
    QVBoxLayout *verticalLayout_3;
    QVBoxLayout *verticalLayout;
    QLabel *label_2;
    QListWidget *offersList;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_3;
    QLineEdit *bidInput;
    QPushButton *bidButton;

    void setupUi(QWidget *CollectorWindowClass)
    {
        if (CollectorWindowClass->objectName().isEmpty())
            CollectorWindowClass->setObjectName("CollectorWindowClass");
        CollectorWindowClass->resize(600, 400);
        horizontalLayout_4 = new QHBoxLayout(CollectorWindowClass);
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_4->setObjectName("horizontalLayout_4");
        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName("horizontalLayout_3");
        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setObjectName("verticalLayout_2");
        itemsList = new QListWidget(CollectorWindowClass);
        itemsList->setObjectName("itemsList");

        verticalLayout_2->addWidget(itemsList);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName("horizontalLayout");
        label = new QLabel(CollectorWindowClass);
        label->setObjectName("label");

        horizontalLayout->addWidget(label);

        categoriesComboBox = new QComboBox(CollectorWindowClass);
        categoriesComboBox->setObjectName("categoriesComboBox");

        horizontalLayout->addWidget(categoriesComboBox);


        verticalLayout_2->addLayout(horizontalLayout);


        horizontalLayout_3->addLayout(verticalLayout_2);

        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setSpacing(6);
        verticalLayout_3->setObjectName("verticalLayout_3");
        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName("verticalLayout");
        label_2 = new QLabel(CollectorWindowClass);
        label_2->setObjectName("label_2");

        verticalLayout->addWidget(label_2);

        offersList = new QListWidget(CollectorWindowClass);
        offersList->setObjectName("offersList");

        verticalLayout->addWidget(offersList);


        verticalLayout_3->addLayout(verticalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        label_3 = new QLabel(CollectorWindowClass);
        label_3->setObjectName("label_3");

        horizontalLayout_2->addWidget(label_3);

        bidInput = new QLineEdit(CollectorWindowClass);
        bidInput->setObjectName("bidInput");

        horizontalLayout_2->addWidget(bidInput);


        verticalLayout_3->addLayout(horizontalLayout_2);

        bidButton = new QPushButton(CollectorWindowClass);
        bidButton->setObjectName("bidButton");

        verticalLayout_3->addWidget(bidButton);


        horizontalLayout_3->addLayout(verticalLayout_3);


        horizontalLayout_4->addLayout(horizontalLayout_3);


        retranslateUi(CollectorWindowClass);

        QMetaObject::connectSlotsByName(CollectorWindowClass);
    } // setupUi

    void retranslateUi(QWidget *CollectorWindowClass)
    {
        CollectorWindowClass->setWindowTitle(QCoreApplication::translate("CollectorWindowClass", "CollectorWindow", nullptr));
        label->setText(QCoreApplication::translate("CollectorWindowClass", "Filter:", nullptr));
        label_2->setText(QCoreApplication::translate("CollectorWindowClass", "Offers:", nullptr));
        label_3->setText(QCoreApplication::translate("CollectorWindowClass", "Your offer:", nullptr));
        bidButton->setText(QCoreApplication::translate("CollectorWindowClass", "Make bid", nullptr));
    } // retranslateUi

};

namespace Ui {
    class CollectorWindowClass: public Ui_CollectorWindowClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_COLLECTORWINDOW_H
