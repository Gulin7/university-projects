#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <shared_mutex>
#include <random>
#include <chrono>
#include <future>
#include <atomic>
#include <algorithm>
#include <functional>
#include <condition_variable>
#include <list>

const int MAX_THREADS = std::thread::hardware_concurrency();

std::vector<std::vector<int>> graph;
std::vector<int> path;
std::mutex mtx;
std::shared_timed_mutex smtx;
bool found = false;
int noVertices;
double edgeProbability;

void generateGraph(int noVertices, double edgeProbability)
{
    graph.resize(noVertices, std::vector<int>(noVertices, 0));
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);

    for (int i = 0; i < noVertices; ++i) {
        for (int j = 0; j < noVertices; ++j) {
            if (i != j && dis(gen) < edgeProbability) {
                graph[i][j] = 1;
            }
        }
    }
}

void printGraph()
{
    for (int i = 0; i < graph.size(); ++i)
    {
        std::cout << "Row " << i << ": ";
        for (int j = 0; j < graph[i].size(); ++j) {
			std::cout << graph[i][j] << " ";
		}
        std::cout << '\n';
	}
}   

void printPath()
{
    std::cout<< '\n' << "Hamiltonian cycle: ";
    for (int i = 0; i < path.size(); ++i) {
		std::cout << path[i] << " ";
	}
	std::cout << '\n';
}

bool edgeCanBeAdded(std::vector<int> path, int position, int vertex)
{
    if (graph[path[position-1]][vertex] == 1)
    {
        for (int i = 0; i < position; ++i)
        {
            if (path[i] == vertex)
            {
				return false;
			}
		}
		return true;
	}
	return false;
}

std::vector<int> findHamiltonianCycle(int position, std::vector<int> path, int noThreads)
{
    {
        // check if the cycle was already found by another thread
        std::shared_lock<std::shared_timed_mutex> lock(smtx);
        if (found)
        {
            return std::vector<int>();
        }
    }
    if (position == noVertices)
    {
        if (graph[path[position - 1]][path[0]] == 1)
        {
            // lock the mutex to write the result
            std::unique_lock<std::mutex> lock(mtx);
            found = true;
            return path;
		}
		return std::vector<int>();
    }

    std::vector<std::future<std::vector<int>>> futures;

    for (int i = 0; i < noVertices; ++i)
    {
        if (edgeCanBeAdded(path, position, i))
        {
            smtx.lock_shared();
            if (noThreads <= 1)
            {
                smtx.unlock_shared();
				path[position] = i;
				std::vector<int> result = findHamiltonianCycle(position + 1, path, 1);
                if (!result.empty())
                {
					return result;
				}   
			}
            else
            {
                std::vector<int> newPath(path);
                newPath[position] = i;
                futures.push_back(std::async(std::launch::async, findHamiltonianCycle, position + 1, newPath, noThreads - 1));
                mtx.lock();
                noThreads--;
                mtx.unlock();
            }
        }
	}

    // Check the results of all async tasks
    for (auto& future : futures) {
        std::vector<int> result = future.get();
        if (!result.empty()) {
            return result;
        }
    }

    return std::vector<int>();
}


int main()
{
    std::cout << "Enter the number of vertices: ";
    std::cin >> noVertices;
    std::cout << "Enter the edge probability: ";
    std::cin >> edgeProbability;

    path.resize(noVertices);

    int noThreads = MAX_THREADS;

    // generate a random graph
    generateGraph(noVertices, edgeProbability);

    //graph = {
	//	{0, 1, 1, 1, 0},
	//	{1, 0, 1, 1, 1},
	//	{1, 1, 0, 1, 0},
	//	{1, 1, 1, 0, 1},
	//	{0, 1, 0, 1, 0}
	//};

    //printGraph();

    std::clock_t timer;
    timer = clock();

    path = findHamiltonianCycle(1, path, noThreads);

    timer = clock() - timer;
    printPath();
    std::cout << "Execution time: " << ((float)timer) / CLOCKS_PER_SEC << " seconds" << std::endl;

    return 0;
}
