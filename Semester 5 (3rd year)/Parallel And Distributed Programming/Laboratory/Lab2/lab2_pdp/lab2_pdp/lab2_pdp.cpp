#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

vector<int> firstVector, secondVector;
vector<int> vectorProducts;

int vectorSize;

bool producerDone = false;
condition_variable conditionVariable;
mutex mtx;

void producer()
{
    for (int i = 0; i < vectorSize; i++)
    {
        int product = firstVector[i] * secondVector[i];
        {
            unique_lock<mutex> lock(mtx);
            vectorProducts.push_back(product);
            cout << "Producer " << i << ": " << product << '\n';
        }

        conditionVariable.notify_one();
    }

    {
        unique_lock<mutex> lock(mtx);
        producerDone = true;
    }
    // Notify consumer that production is done
    conditionVariable.notify_one();
}

void consumer()
{
    int scalarProduct = 0;

    for(int i = 0; i < vectorSize; i++)
    {
        int product;

        {
            unique_lock<mutex> lock(mtx);
            conditionVariable.wait(lock, [] { return !vectorProducts.empty() || producerDone; });

            // If the producer is done and there are no more products, exit the loop
            if (vectorProducts.empty() && producerDone)
            {
                break;
            }

            // Get the last product
            product = vectorProducts.back();
            vectorProducts.pop_back();
            scalarProduct += product;
            cout << "Consumer: " << i << ": " << product << '\n';
        }
    }

    cout << "Scalar product: " << scalarProduct << '\n';
}

int main()
{
    // Read the size of the vectors
    cout << "Enter the size of the vectors: ";
    cin >> vectorSize;

    firstVector.resize(vectorSize);
    secondVector.resize(vectorSize);

    // Read the values for the first vector
    for (int i = 0; i < vectorSize; i++)
    {
        cout << "Enter the value for the first vector: ";
        cin >> firstVector[i];
    }

    // Read the values for the second vector
    for (int i = 0; i < vectorSize; i++)
    {
        cout << "Enter the value for the second vector: ";
        cin >> secondVector[i];
    }

    // Create the producer and consumer threads
    thread producerThread(producer);
    thread consumerThread(consumer);

    // Wait for the threads to finish
    producerThread.join();
    consumerThread.join();

    return 0;
}