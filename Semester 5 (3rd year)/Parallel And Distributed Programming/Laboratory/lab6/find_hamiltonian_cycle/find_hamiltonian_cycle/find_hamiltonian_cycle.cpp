#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <shared_mutex>
#include <random>
#include <queue>
#include <condition_variable>
#include <functional>
#include <atomic>
#include <future>
#include <map>
#include <algorithm>
#include <unordered_set>

using namespace std;

// ThreadPool implementation
class ThreadPool {
public:
    ThreadPool(size_t num_threads = thread::hardware_concurrency()) : active_tasks(0) {
        for (size_t i = 0; i < num_threads; ++i) {
            threads_.emplace_back([this] {
                while (true) {
                    function<void()> task;
                    {
                        unique_lock<mutex> lock(queue_mutex_);
                        cv_.wait(lock, [this] { return !tasks_.empty() || stop_; });
                        if (stop_ && tasks_.empty()) return;
                        task = move(tasks_.front());
                        tasks_.pop();
                    }
                    task();
                    decrementTaskCount();
                }
                });
        }
    }

    ~ThreadPool() {
        {
            unique_lock<mutex> lock(queue_mutex_);
            stop_ = true;
        }
        cv_.notify_all();
        for (auto& thread : threads_) {
            thread.join();
        }
    }

    void enqueue(function<void()> task) {
        incrementTaskCount();
        {
            unique_lock<mutex> lock(queue_mutex_);
            tasks_.emplace(move(task));
        }
        cv_.notify_one();
    }

    void wait() {
        unique_lock<mutex> lock(task_count_mutex_);
        cv_done_.wait(lock, [this] { return active_tasks == 0; });
    }

private:
    vector<thread> threads_;
    queue<function<void()>> tasks_;
    mutex queue_mutex_;
    condition_variable cv_;

    atomic<int> active_tasks;
    mutex task_count_mutex_;
    condition_variable cv_done_;
    bool stop_ = false;

    void incrementTaskCount() {
        active_tasks++;
    }

    void decrementTaskCount() {
        if (--active_tasks == 0) {
            lock_guard<mutex> lock(task_count_mutex_);
            cv_done_.notify_all();
        }
    }
};

const int MAX_THREADS = 1;

atomic<int> noThreads = MAX_THREADS;

ThreadPool pool(static_cast<size_t>(MAX_THREADS));

// Graph as an adjacency list using unordered_set for each vertex
vector<unordered_set<int>> graph;
vector<int> path;
mutex mtx;
shared_timed_mutex smtx;
int noVertices;
double edgeProbability;
atomic<bool> found(false);
vector<int> solution_path;
mutex result_mutex;
mutex path_mutex;
mutex solution_mutex;

void generateGraph(int noVertices, double edgeProbability) {
    edgeProbability = edgeProbability / 4;
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0.0, 1.0);

    graph.resize(noVertices);  // Resize the graph for the number of vertices

    for (int i = 0; i < noVertices; ++i) {
        for (int j = 0; j < noVertices; ++j) {
            if (i != j && dis(gen) < edgeProbability) {
                graph[i].insert(j); // Add an edge from i to j
            }
        }
    }
}

void printPath() {
    lock_guard<mutex> lock(solution_mutex);
    cout << "\nHamiltonian cycle: ";
    for (int vertex : solution_path) {
        cout << vertex << " ";
    }
    cout << '\n';
}

bool edgeCanBeAdded(const vector<int>& path, int position, int vertex) {
    // Check if the edge exists in the adjacency list using unordered_set
    if (graph[path[position - 1]].count(vertex) > 0) { // Edge exists
        for (int i = 0; i < position; ++i) {    // Check for duplicates
            if (path[i] == vertex) {
                return false;
            }
        }
        return true;
    }
    return false;
}

void findHamiltonianCycle(int position, vector<int>& path, int noThreads) {
    {
        lock_guard<mutex> lock(solution_mutex);
        if (found) return;  // Protect check for `found`
    }

    if (position == path.size()) {
        // Check if the last vertex connects back to the first to form a cycle
        if (graph[path[position - 1]].count(path[0]) > 0) {
            lock_guard<mutex> lock(solution_mutex);
            if (!found) {
                found = true;
                solution_path = path;
            }
        }
        return;
    }

    for (int i = 0; i < noVertices; ++i) {
        if (edgeCanBeAdded(path, position, i)) {
            {
                lock_guard<mutex> lock(solution_mutex);
                if (found) return;  // Protect check for `found`
            }

            path[position] = i; // Assign the current vertex to the path
            if (noThreads > 1) {
                // Create a copy of the current path for the new thread
                vector<int> new_path = path;
                pool.enqueue([position, new_path, noThreads]() mutable {
                    findHamiltonianCycle(position + 1, new_path, noThreads - 1);
                    });
            }
            else {
                // Continue in the same thread
                findHamiltonianCycle(position + 1, path, noThreads);
            }

            path[position] = -1; // Backtrack
        }
    }
}

int main() {
    cout << "Enter the number of vertices: ";
    cin >> noVertices;
    cout << "Enter the edge probability: ";
    cin >> edgeProbability;

    path.resize(noVertices);

    // Generate a random graph
    generateGraph(noVertices, edgeProbability);

    clock_t timer;
    timer = clock();

    findHamiltonianCycle(1, path, noThreads);
    pool.wait();

    timer = clock() - timer;
    if (path[0] == -1) {
        cout << "No Hamiltonian cycle found\n";
    }
    else {
        printPath();
    }
    cout << "Execution time: " << static_cast<float>(timer) / CLOCKS_PER_SEC << " seconds" << endl;

    return 0;
}
