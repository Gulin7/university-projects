#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>
#include <thread>
#include <mutex>
#include <random>
#include <chrono>

using namespace std;

typedef struct
{
    int serial_number;
    int amount;
    int source_id;
    int dest_id;
} Operation;

typedef struct
{
    int account_id;
    int initial_balance;
    int current_balance;
    mutex* account_mutex;
    vector<Operation> log;
} Account;

int curr_serial_number = 0;
int no_threads;
unordered_map<int, Account> account_list;
vector<int> account_id_list;
// vector of operations to be executed
vector<Operation> operations;

bool consistency_check_passed = true;

/*
 * Reads the account_list from the file and stores them in the account_list map
 */
void read_accounts_from_file(string file_path)
{
    ifstream input_file(file_path);

    if (!input_file.is_open())
    {
        cerr << "Error opening file: " << file_path << '\n';
        return;
    }

    while (input_file)
    {
        int account_id, balance;
        input_file >> account_id >> balance;

        if (!input_file.fail())
        {
            Account account;
            account.account_id = account_id;
            account.initial_balance = balance;
            account.current_balance = balance;
            account.account_mutex = new mutex;
            account_list[account_id] = account;

            account_id_list.push_back(account_id);
        }
    }

    input_file.close();
}

/*
 * Generates a random number in the range [min, max]
 */
int generate_random_number_in_range(int min, int max)
{
    random_device rd;
    mt19937 mt(rd());
    uniform_int_distribution<int> dist(min, max);
    return dist(mt);
}


/*
 * Returns a random account ID from the list of account_list
 */
int get_random_account()
{
    return account_id_list[generate_random_number_in_range(0, account_list.size() - 1)];
}

/*
 * Gets two random account ids
 */
void get_two_random_account_ids(int *source_id, int *destination_id)
{
    *source_id = get_random_account();
    *destination_id = get_random_account();
    while (source_id == destination_id)
    {
        *destination_id = get_random_account();
    }
}

/*
 * Generates a random amount between 1 and 50
 */
int get_random_amount(int min, int max)
{
    return generate_random_number_in_range(min, max);
}

/*
 * Generate a list of random operations between
 * 2 randomly generated accounts,
 * with a randomly generated amount
 */
void generate_random_operations(int size)
{
    for (int i = 0; i < size; i++)
    {
        Operation operation;

        // get two random account IDs
        int source_id, destination_id;
        get_two_random_account_ids(&source_id, &destination_id);
        while (source_id == destination_id)
        {
            destination_id = get_random_account();
        }
        // set the source and destination IDs of the operation
        operation.source_id = source_id;
        operation.dest_id = destination_id;

        // get a random amount between 1 and 50
        int amount = get_random_amount(1, 50);
        operation.amount = amount;

        // increment the serial number
        operation.serial_number = ++curr_serial_number;

        // add the operation to the list of operations
        operations.push_back(operation);
    }
}

void check_consistency()
{
    // iterate over all account_list
    for (auto& entry : account_list)
    {
        // lock the account
        entry.second.account_mutex->lock();

        // get the account
        Account& account = entry.second;
        int computed_balance = account.initial_balance;

        // iterate over all operations in the log
        for (const auto& operation : account.log)
        {
            // if the operation is a deposit, add the amount to the balance
            if (operation.source_id == account.account_id)
            {
                computed_balance -= operation.amount;
            }
            // if the operation is a withdrawal, subtract the amount from the balance
            else if (operation.dest_id == account.account_id)
            {
                computed_balance += operation.amount;
            }
        }

        // if the calculated balance is different from the current balance, set the consistency_check_passed flag to false
        if (computed_balance != account.current_balance)
        {
            consistency_check_passed = false;
        }

        entry.second.account_mutex->unlock();
    }
}

void handle_threads(int thread_id)
{
    int size = operations.size() / no_threads;
    int start = thread_id * size;
    int end = (thread_id == no_threads - 1) ? operations.size() : start + size;

    for (int i = start; i < end; i++)
    {
        // get the lock for the first account
        account_list[operations[i].source_id].account_mutex->lock();

        // if balance is 0, skip the operation
        if (account_list[operations[i].source_id].current_balance - operations[i].amount < 0)
        {
            // unlock the first account before continuing to the next operation
            account_list[operations[i].source_id].account_mutex->unlock();
            continue;
        }

        // update first account balance
        account_list[operations[i].source_id].current_balance -= operations[i].amount;
        // log the operation
        account_list[operations[i].source_id].log.push_back(operations[i]);
        // unlock the first account
        account_list[operations[i].source_id].account_mutex->unlock();

        // get a lock on the 2nd account
        account_list[operations[i].dest_id].account_mutex->lock();
        // update the 2nd account balance
        account_list[operations[i].dest_id].current_balance += operations[i].amount;
        // log the operation
        account_list[operations[i].dest_id].log.push_back(operations[i]);
        // unlock the 2nd account
        account_list[operations[i].dest_id].account_mutex->unlock();
    }
}

int main()
{
    // get the accounts from the file
    char accounts_file[100];
    cout << "Enter the path to the accounts file: ";
    cin.getline(accounts_file, 100);
    // read the accounts from the given file
    read_accounts_from_file(accounts_file);

    // Get the number of threads
    cout << "Enter the number of threads: ";
    cin >> no_threads;

    // get the number of operations
    int number_of_operations;
    cout << "Enter the number of operations: ";
    cin >> number_of_operations;
    // generate all operations
    generate_random_operations(number_of_operations);
    
    // get the start time
    auto start = clock();

    vector<thread> thread_list;
    for (int i = 0; i < no_threads; i++)
    {
        thread_list.push_back(thread(handle_threads, i));
    }

    // join threads
    for (auto& th : thread_list)
    {
        th.join();
    }

    check_consistency();

    // get the end time, including the check for consistency
    auto end = clock();
    // compute the total duration
    double total_duration = static_cast<double>(end - start) / CLOCKS_PER_SEC;

    for (auto& account : account_list)
    {
        cout << "Account: " << account.first << ", Balance: " << account.second.current_balance << '\n';
        cout << "Operations: " << account.second.log.size() << '\n';
        delete account.second.account_mutex;
    }

    if (consistency_check_passed)
    {
        cout << '\n' << "Checks passed :P" << '\n';;
    }
    else
    {
        cout << "Checks didn't pass :(" << '\n';;
    }

    cout << '\n' << "Total time: " << total_duration << " seconds" << '\n';

    return 0;
}