#include "UserWindow.h"
#include <QtWidgets/QApplication>
#include <QSortFilterProxyModel>

#include "IssueRepository.h"
#include "UserRepository.h"
#include "Service.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    UserRepository users{ "users.txt" };
    IssueRepository issues{ "issues.txt" };

    Service service{ users, issues };

    QSortFilterProxyModel* model = new QSortFilterProxyModel{};
    model->setSourceModel(&service);
    model->setFilterRegularExpression(QRegularExpression("open"));
    model->setFilterKeyColumn(1);

    QSortFilterProxyModel* sortedModel = new QSortFilterProxyModel{};
    sortedModel->setSourceModel(&service);
    sortedModel->sort(3, Qt::DescendingOrder);
    sortedModel->setDynamicSortFilter(true);

    UserWindow wnd{ model, service, "Marry" }, wndSorted{ sortedModel, service, "Marry" };
    wnd.show();

    wndSorted.setWindowTitle("Marry sorted");
    wndSorted.show();

    vector<UserWindow*> windows;

    for (auto& user : users.getAll())
    {
        UserWindow* currentWindow = new UserWindow{ &service, service, user.getName() };

        currentWindow->show();

        windows.push_back(currentWindow);
    }

    return a.exec();
}
