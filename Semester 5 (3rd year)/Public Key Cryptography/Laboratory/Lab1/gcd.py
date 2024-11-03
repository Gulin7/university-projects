import time
from prettytable import PrettyTable

def timeFunction(function, first, second):
    # We start a counter
    start = time.perf_counter()
    # We run the function
    result = function(first, second)
    # We stop the counter
    end = time.perf_counter()
    # Return the result and the total time it took the function to run
    return result, end - start

def gcdEuclidian(first, second):
    # GCD(0, second) == second; GCD(a, 0) == first,
    # GCD(0, 0) == 0
    if (first == 0):
        return second
    if (second == 0):
        return first

    while second!=0:
        first, second = second, first % second
    return first

def gcdBruteForce(first, second):
    # GCD(0, second) == second; GCD(a, 0) == first,
    # GCD(0, 0) == 0
    if (first == 0):
        return second
    if (second == 0):
        return first

    gcd = 1
    # We find the greatest common divisor by
    # Iterating through the range from the smallest number to 1
    # Returning the first number that divides both numbers
    for i in range(min(first, second), 1, -1):
        if first % i == 0 and second % i == 0:
            return i
    return gcd

def gcdStein(first, second):
    # GCD(0, second) == second; GCD(a, 0) == first,
    # GCD(0, 0) == 0
    if (first == 0):
        return second
    if (second == 0):
        return first

    # Finding K, where K is the
    # greatest power of 2 that
    # divides both first and second.
    k = 0

    while (((first | second) & 1) == 0):
        first = first >> 1
        second = second >> 1
        k = k + 1

    # Dividing a by 2 until first becomes odd
    while ((first & 1) == 0):
        first = first >> 1

    # From here on, 'first' is always odd.
    while (second != 0):

        # If b is even, remove all
        # factor of 2 in b
        while ((second & 1) == 0):
            second = second >> 1

        # Now first and second are both odd. Swap if
        # necessary so first <= second, then set
        # second = second - first (which is even).
        if (first > second):
            # Swap u and v.
            temp = first
            first = second
            second = temp

        second = (second - first)

    # restore common factors of 2
    return (first << k)

def compareTimes():
    # Input values for the analysis
    input_values = [
        (24, 36),
        (101, 103),
        (540, 360),
        (1234, 7890),
        (98765, 12345),
        (111, 222),
        (1234567, 9876543),
        (500000, 1000000),
        (78213, 12345),
        (95878, 87643)
    ]

    # Dictionary for storing times it took
    result_values = {'Euclidian': [], 'BruteForce': [], 'Stein': []}

    for first, second in input_values:
        time_euclidian = timeFunction(gcdEuclidian, first, second)
        result_values['Euclidian'].append(time_euclidian)
        time_brute_force = timeFunction(gcdBruteForce, first, second)
        result_values['BruteForce'].append(time_brute_force)
        time_stein = timeFunction(gcdStein, first, second)
        result_values['Stein'].append(time_stein)

    table = PrettyTable()
    table.field_names = ['Algorithm', 'Input', 'Result', 'Time']
    for algorithm in result_values.keys():
        results = result_values[algorithm]
        for i in range(10):
            table.add_row([algorithm, input_values[i], results[i][0], results[i][1]])

    print(table)

    tableTotals = PrettyTable()
    tableTotals.field_names = ['Algorithm', 'Total Time']
    total_euclidian = sum([result[1] for result in result_values['Euclidian']])
    total_brute_force = sum([result[1] for result in result_values['BruteForce']])
    total_stein = sum([result[1] for result in result_values['Stein']])
    tableTotals.add_row(['Euclidian', total_euclidian])
    tableTotals.add_row(['BruteForce', total_brute_force])
    tableTotals.add_row(['Stein', total_stein])

    print(tableTotals)


if __name__ == '__main__':
    compareTimes()
    # print(gcdEuclidian(123456789456, 987654321654))
    # print(gcdStein(123456789456, 987654321654))
    # print(timeFunction(gcdEuclidian, 123456789456, 987654321654))
    # print(timeFunction(gcdStein, 123456789456, 987654321654))
