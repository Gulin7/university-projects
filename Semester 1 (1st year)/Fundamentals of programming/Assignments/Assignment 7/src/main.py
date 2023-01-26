# IMPORT MODULES
import json
import pickle
from jproperties import Properties
import mysql.connector
# IMPORT FROM FILES
from src.testing.tests import run_all_tests
from src.ui.ui import *
from src.services.expenses_services import ExpensesService
from src.infrastructure.MemoryRepo import MemoryRepo
from src.infrastructure.BinaryFileRepo import BinaryFileRepo
from src.infrastructure.TextFileRepo import TextFileRepo
from src.infrastructure.JsonRepo import JsonRepo
from src.infrastructure.SQLRepo import SqlRepository


def save_expenses_to_files(all_services):
    """
        WRITE TO TEXT FILE
    """
    with open('TextFileRepo.txt', "w") as file:
        for expense in all_services._repo.get_all_expenses():
            file.write(
                str(expense.get_day()) + ", " + str(expense.get_amount()) + ", " + str(
                    expense.get_type()) + "\n")
    file.close()
    """
        WRITE TO BINARY FILE
    """
    pickle.dump(all_services._repo.get_all_expenses(), open('BinaryFileRepo.pickle', "wb"))
    """
        WRITE TO JSON FILE
    """
    expenses_json = {}
    expenses_list = copy.deepcopy(all_services.get_all_expenses_in_service())
    for index in range(len(list(expenses_list))):
        expenses_json[index] = expenses_list[index].to_dict()
    write_to_json = json.dumps(expenses_json)
    with open('JsonRepo.json', "w") as file:
        file.write(write_to_json)
    file.close()
    """
        STORE TO DATABASE
    """

    expenses_list = all_services.get_all_expenses_in_service()
    database = mysql.connector.connect(host="localhost", user="root", password="Mamaluinacho232#", database="expenses_schema",
                                       port=3306)
    cursor = database.cursor()
    cursor.execute("DELETE FROM expenses")
    for expense in list(expenses_list):
        cursor.execute("INSERT INTO expenses(`day`,`amount`,`type`) VALUES (%s, %s, %s)",
                       (expense.get_day(), expense.get_amount(), expense.get_type()))
    database.commit()
    database.close()


def main():
    configuration = Properties()
    with open('settings.properties', 'rb') as config_file:
        configuration.load(config_file)
    repository_type = configuration.get('repository_type').data

    print(f'The repository type is: {repository_type}')

    if repository_type == 'memory':
        all_expenses_repo = MemoryRepo()
    elif repository_type == 'text':
        all_expenses_repo = TextFileRepo('TextFileRepo.txt')
    elif repository_type == 'binary':
        all_expenses_repo = BinaryFileRepo('BinaryFileRepo.pickle')
    elif repository_type == 'json':
        all_expenses_repo = JsonRepo('JsonRepo.json')
    else:
        all_expenses_repo = SqlRepository()

    run_all_tests()
    all_services = ExpensesService(all_expenses_repo)
    ui = Ui(all_services)

    if repository_type == 'memory':
        all_services._repo.set_expenses([])
        all_services.generate_random_expenses()

    ui.start_ui()

    """if repository_type == 'memory':
        save_expenses_to_files(all_services)"""


if __name__ == '__main__':
    main()
