def sum_1():
    """
    This sum is:
    1/1-1/2+1/3-1/4+1/5-1/6+...
    :return: the result is ln2
    """
    series1 = 0.0
    for i in range(1, 10000000, 2):
        series1 = series1 + (1 / i) - 1 / (i + 1)
    return series1


def sum_2():
    """
    This sum is:
    1/1-1/2-1/4  + 1/3-1/6-1/8  +  1/5-1/10-1/12
    :return: the result is 1/2*the initial sum
    """
    series2 = 0.0
    for i in range(1, 10000000, 2):
        series2 = series2 + (1 / i) - (1 / (2 * i)) - (1 / (2 * (i + 1)))
    return series2


def sum_3():
    """
    This sum is:
    1/1+1/3-1/2  +  1/5+1/7-1/4  +  1/9+1/11-1/6  + ...
    :return: the result of the sum is 1.5*the initial sum
    """
    series3 = 0.0
    aux = 2
    for i in range(1, 10000000, 4):
        series3 = series3 + (1 / i) + (1 / (i + 2)) - (1 / aux)
        aux += 2
    return series3


if __name__ == '__main__':
    print(sum_1())
    print(sum_2())
    print(sum_3())
