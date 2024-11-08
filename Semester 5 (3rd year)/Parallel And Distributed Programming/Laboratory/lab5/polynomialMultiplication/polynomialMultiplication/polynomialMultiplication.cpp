#include <iostream>
#include <vector>
#include <ctime>
#include <thread>
#include <mutex>

using namespace std;

const int NAIVE_SEQUENTIAL = 1;
const int NAIVE_PARALLEL = 2;
const int KARATSUBA_SEQUENTIAL = 3;
const int KARATSUBA_PARALLEL = 4;

int n, numberOfThreads, algorithm;

mutex mtx;

vector<int> firstPolynomial, secondPolynomial, resultPolynomial;
vector<thread> threads;

vector<int> polynomialMultiplication(const vector<int> &firstPoly,const vector<int> &secondPoly)
{
    vector<int> resultPoly(firstPoly.size() + secondPoly.size() - 1, 0);
    for (int i = 0; i < firstPoly.size(); i++)
    {
        for (int j = 0; j < secondPoly.size(); j++)
        {
            resultPoly[i+j] += firstPoly[i] * secondPoly[j];
		}
    }
    return resultPoly;
}

void polynomialMultiplicationWithThreads(int startIndex)
{
    int currDegree = startIndex;
    for (; currDegree < n; currDegree += numberOfThreads)
    {
        // solve for position currDegree
        for (int x = 0; x <= currDegree; x++)
        {
            int y = currDegree - x;
            resultPolynomial[currDegree] += firstPolynomial[x] * secondPolynomial[y];
        }
    }
    for (; currDegree < 2 * n - 1; currDegree += numberOfThreads)
    {
        // solve for position currDegree
        for (int x = currDegree - n + 1; x < n; x++)
        {
            int y = currDegree - x;
            resultPolynomial[currDegree] += firstPolynomial[x] * secondPolynomial[y];
        }
    }
}

// Function to addPolynomials two polynomials
vector<int> addPolynomials(const vector<int>& firstPoly, const vector<int>& secondPoly)
{
    int maxSize = max(firstPoly.size(), secondPoly.size());
    vector<int> resultPoly(maxSize, 0);
    for (int i = 0; i < maxSize; ++i)
    {
        if (i < firstPoly.size())
        {
            resultPoly[i] += firstPoly[i];
        }
        if (i < secondPoly.size())
        {
            resultPoly[i] += secondPoly[i];
        }
    }
    return resultPoly;
}

// Function to subtractPolynomials two polynomials
vector<int> subtractPolynomials(const vector<int>& firstPoly, const vector<int>& secondPoly)
{
    int maxSize = max(firstPoly.size(), secondPoly.size());
    vector<int> resultPoly(maxSize, 0);
    for (int i = 0; i < maxSize; ++i)
    {
        if (i < firstPoly.size())
        {
            resultPoly[i] += firstPoly[i];
        }
        if (i < secondPoly.size())
        {
            resultPoly[i] -= secondPoly[i];
        }
    }
    return resultPoly;
}

// Karatsuba algorithm for polynomial multiplication
vector<int> karatsubaSequential(const vector<int>& firstPoly, const vector<int>& secondPoly)
{
    size_t size = max(firstPoly.size(), secondPoly.size());

    // Base case for recursion
    if (size <= 100)
    {
        return polynomialMultiplication(firstPoly, secondPoly);
    }

    // Making the degree of polynomials even
    size_t halfSize = (size + 1) / 2;

    vector<int> firstLow(firstPoly.begin(), firstPoly.begin() + min(halfSize, firstPoly.size()));
    vector<int> firstHigh(firstPoly.begin() + min(halfSize, firstPoly.size()), firstPoly.end());
    vector<int> secondLow(secondPoly.begin(), secondPoly.begin() + min(halfSize, secondPoly.size()));
    vector<int> secondHigh(secondPoly.begin() + min(halfSize, secondPoly.size()), secondPoly.end());

    vector<int> firstLowHigh = addPolynomials(firstHigh, firstLow);
    vector<int> secondLowHigh = addPolynomials(secondHigh, secondLow);

    // Recursive calls
    vector<int> z0 = karatsubaSequential(firstLow, secondLow);
    vector<int> z1 = karatsubaSequential(firstLowHigh, secondLowHigh);
    vector<int> z2 = karatsubaSequential(firstHigh, secondHigh);

    // Combining the results
    vector<int> temp = subtractPolynomials(z1, z0);
    temp = subtractPolynomials(temp, z2);

    vector<int> resultPoly(firstPoly.size() + secondPoly.size() - 1, 0);
    for (int i = 0; i < z0.size(); i++)
    {
        resultPoly[i] += z0[i];
    }
    for (int i = 0; i < temp.size(); i++)
    {
        resultPoly[i + halfSize] += temp[i];
    }
    for (int i = 0; i < z2.size(); i++)
    {
        resultPoly[i + 2 * halfSize] += z2[i];
    }
    return resultPoly;
}

vector<int> karatsubaParallel(const vector<int>& firstPoly, const vector<int>& secondPoly)
{
    size_t size = max(firstPoly.size(), secondPoly.size());

    // Base case for recursion
    if (size <= 100)
    {
        return polynomialMultiplication(firstPoly, secondPoly);
    }

    // Making the degree of polynomials even
    size_t halfSize = (size + 1) / 2;

    vector<int> firstLow(firstPoly.begin(), firstPoly.begin() + min(halfSize, firstPoly.size()));
    vector<int> firstHigh(firstPoly.begin() + min(halfSize, firstPoly.size()), firstPoly.end());
    vector<int> secondLow(secondPoly.begin(), secondPoly.begin() + min(halfSize, secondPoly.size()));
    vector<int> secondHigh(secondPoly.begin() + min(halfSize, secondPoly.size()), secondPoly.end());

    vector<int> z0, z1, z2, resultPoly(firstPoly.size() + secondPoly.size() - 1, 0);
    
    vector<int> firstLowHigh = addPolynomials(firstHigh, firstLow);
    vector<int> secondLowHigh = addPolynomials(secondHigh, secondLow);

    thread t0([&]
        {
            z0 = karatsubaParallel(firstLow, secondLow);
            mtx.lock();
            for (int i = 0; i < z0.size(); i++)
            {
                resultPoly[i] += z0[i];
            }
            mtx.unlock();
        });
    thread t2([&]
        {
			z2 = karatsubaParallel(firstHigh, secondHigh);
            mtx.lock();
            for (int i = 0; i < z2.size(); i++)
            {
                resultPoly[i + 2 * halfSize] += z2[i];
            }
            mtx.unlock();
		});
    thread t1([&]
        {
            z1 = karatsubaParallel(firstLowHigh, secondLowHigh);
		});
    
    t0.join();
	t1.join();
	t2.join();

	vector<int> temp = subtractPolynomials(z1, z0);
	temp = subtractPolynomials(temp, z2);
    
    for (int i = 0; i < temp.size(); i++)
    {
		resultPoly[i + halfSize] += temp[i];
	}
    
	return resultPoly;
}

void printVector(vector<int> v)
{
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << ' ';
    }
    cout << '\n';
}

void initialiseData()
{
    cout << "Enter size: ";
    cin >> n;
    if (algorithm == NAIVE_PARALLEL)
    {
        cout << "Enter number of threads: ";
        cin >> numberOfThreads;
    }
    for (int i = 0; i < n; ++i)
    {
        firstPolynomial.push_back(1);
        secondPolynomial.push_back(1);
    }

    resultPolynomial.resize(2 * n - 1, 0);
}

void solve()
{
    clock_t time = clock();

    initialiseData();

    if (algorithm == NAIVE_SEQUENTIAL)
    {
       	polynomialMultiplication(firstPolynomial, secondPolynomial);
    }
    else if (algorithm == NAIVE_PARALLEL)
    {
        for (int i = 0; i < min(n, numberOfThreads); i++)
        {
            threads.push_back(thread(polynomialMultiplicationWithThreads, i));
        }
        // join threads
        for (int i = 0; i < threads.size(); i++)
        {
            threads[i].join();
        }
    }
    else if (algorithm == KARATSUBA_SEQUENTIAL)
    {
		resultPolynomial = karatsubaSequential(firstPolynomial, secondPolynomial);
	}
    else if (algorithm == KARATSUBA_PARALLEL)
    {
		resultPolynomial = karatsubaParallel(firstPolynomial, secondPolynomial);
	}

    time = clock() - time;
    cout << "Total time: " << static_cast<float>(time) / CLOCKS_PER_SEC << " seconds\n";
}

void printMenu()
{
    cout << "Choose algorithm:\n";
    cout << "1. Naive\n";
    cout << "2. Naive with threads\n";
    cout << "3. Karatsuba\n";
    cout << "4. Karatsuba with threads\n";
}

void getAlgorithm()
{
	cout << "Enter algorithm: ";
	cin >> algorithm;
    if (algorithm < 1 || algorithm > 5)
    {
		cout << "Invalid algorithm\n";
		getAlgorithm();
	}
}

bool getPrintVector()
{
	cout<< "Do you want to print the result vector? 1 - Yes, 0 - No\n";
    bool print;
    cin >> print;
    return print;
}

void mainApp()
{
    printMenu();
    getAlgorithm();
    solve();
    if (getPrintVector())
    {
        printVector(resultPolynomial);
    }
}

int main()
{
    mainApp();
}
