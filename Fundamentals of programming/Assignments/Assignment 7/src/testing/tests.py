from src.domain.Expense import Expense
from src.infrastructure.MemoryRepo import MemoryRepo
from src.services.expenses_services import ExpensesService


def run_domain_tests():
    day = 1
    amount = 2
    type = 3
    expense = Expense(day, amount, type)
    assert (expense.get_day() == day)
    assert (expense.get_amount() == amount)
    assert (expense.get_type() == type)
    another_expense = Expense(day, amount, type)
    assert (expense.equal_expenses(another_expense))


def run_infrastructure_tests():
    repo = MemoryRepo()
    assert (repo.number_of_expenses() == 0)
    day = 1
    amount = 2
    type = 3
    expense = Expense(day, amount, type)
    repo.add_expense_to_repo(expense)
    assert (repo.number_of_expenses() == 1)
    found_entity = repo.search_expense_in_repo(expense)
    assert (found_entity.equal_expenses(expense))
    try:
        repo.add_expense_to_repo(expense)
        assert False
    except ValueError as ve:
        assert (str(ve) == "existing entity!")
    another_day = 2
    another_amount = 3
    another_type = 4
    another_entity = Expense(another_day, another_amount, another_type)
    repo.add_expense_to_repo(another_entity)
    assert (repo.number_of_expenses() == 2)
    all_entities_from_repo = repo.get_all_expenses()
    assert (len(all_entities_from_repo) == 2)
    repo.remove_expense(expense)
    assert (repo.number_of_expenses() == 1)
    try:
        repo.remove_expense(expense)
        assert False
    except ValueError as ve:
        assert (str(ve) == "inexisting entity!")


def run_service_tests():
    repo = MemoryRepo()
    service = ExpensesService(repo)
    try:
        service.undo()
    except ValueError as ve:
        assert str(ve) == 'nothing to undo!'
    assert (service.no_of_expenses_in_service() == 0)
    day = 1
    amount = 2
    type = 3
    service.add_expenses_to_service(day, amount, type)
    assert (service.no_of_expenses_in_service() == 1)
    assert (repo.get_all_expenses()[0].get_day() == 1)
    assert (repo.get_all_expenses()[0].get_amount() == 2)
    assert (repo.get_all_expenses()[0].get_type() == 3)
    try:
        service.add_expenses_to_service(day, amount, type)
        assert False
    except ValueError as ve:
        assert (str(ve) == "existing expense!")


def run_all_tests():
    print("Starting domain tests...")
    run_domain_tests()
    print("Finished domain tests...")
    print("Starting infrastructure tests...")
    run_infrastructure_tests()
    print("Finished infrastrcuture tests...")
    print("Starting service tests...")
    run_service_tests()
    print("Finished service tests...")
