#include <mpi.h>
#include <vector>
#include <iostream>
#include <chrono>
#include <fstream>
#include "utils.h"
#include "globals.h"
#include "multiplications.h"
#include "poly_ops.h"
#include "mpi_comms.h"
#include <string>

using namespace std;

// Define a global output file stream
ofstream output_file;

// Helper function to print the polynomial result as a string
template<typename T>
void print_polynomial(const vector<T>& poly) {
    for (size_t i = 0; i < poly.size(); ++i) {
        output_file << poly[i];
        if (i != poly.size() - 1) {
            output_file << ' ';
        }
    }
    output_file << '\n';    
}

template<typename T>
void actual_main(char **argv)
{
    // Open the output file (append mode)
    output_file.open("output.txt", ios::app);

    if (id == 0) {
        vector<T> poly1 = generate_poly<T>((int) strtol(argv[1], nullptr, 10));
        vector<T> poly2 = generate_poly<T>((int) strtol(argv[2], nullptr, 10));

        output_file << "poly1:\n";
        print_polynomial(poly1);
        output_file << "poly2\n";
        print_polynomial(poly2);

        chrono::high_resolution_clock::time_point beginTime = chrono::high_resolution_clock::now();
        vector<T> mpi_ans = which_mpi == 0 ? mpi_karatsuba(poly1, poly2) : mpi_naive(poly1, poly2);
        chrono::high_resolution_clock::time_point endTime = chrono::high_resolution_clock::now();
        string title;
        if (which_mpi == 0)
            title = "MPI Karatsuba";
        else title = "MPI Naive";
        
        // Print results to the file
        output_file << title + " - " + to_string(chrono::duration_cast<chrono::milliseconds>(endTime-beginTime).count()) + " ms" << endl;

        // Output the result of the MPI multiplication
        print_polynomial(mpi_ans);

        // Run and time simple Karatsuba
        beginTime = chrono::high_resolution_clock::now();
        vector<T> simple_karatsuba_ans = karatsuba(poly1, poly2);
        endTime = chrono::high_resolution_clock::now();
        output_file << "Simple Karatsuba - " + to_string(chrono::duration_cast<chrono::milliseconds>(endTime-beginTime).count()) + " ms" << endl;
        
        // Output the result of the Simple Karatsuba multiplication
        print_polynomial(simple_karatsuba_ans);

        // Run and time simple Naive multiplication
        beginTime = chrono::high_resolution_clock::now();
        vector<T> simple_ans = naive(poly1, poly2);
        endTime = chrono::high_resolution_clock::now();
        output_file << "Simple Naive - " + to_string(chrono::duration_cast<chrono::milliseconds>(endTime-beginTime).count()) + " ms" << endl;
        
        // Output the result of the Simple Naive multiplication
        print_polynomial(simple_ans);

        // Check if the results match and output any discrepancies
        if (different(mpi_ans, simple_ans))
            output_file << "wrong mpi karatsuba" << endl;
        if (different(simple_karatsuba_ans, simple_ans))
            output_file << "wrong simple karatsuba" << endl;
    } else {
        vector<T> x;
        vector<T> y;
        get_parameters(x, y);
        vector<T> ans = which_mpi == 0 ? mpi_karatsuba(x, y) : mpi_naive(x, y);
        send_to_parent(ans);
    }

    // Close the output file at the end
    output_file.close();
}

int main(int argc, char** argv)
{
    if (argc < 3 || argc > 5) {
        cerr << "Invalid params\n";
        exit(1);
    }
    bool bigint = false;
    for (int i = 3; i < argc; ++i)
        if (strcmp(argv[i], "bigint") == 0)
            bigint = true;
        else if (strcmp(argv[i], "simple") == 0)
            set_which_mpi(1);
        else {
            cerr << "Invalid params\n";
            exit(1);
        }
    init();
    if (bigint)
        actual_main<Int>(argv);
    else
        actual_main<int>(argv);
    MPI_Finalize();
}
