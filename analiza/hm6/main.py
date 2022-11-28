def funct_1(x):
    """

    :param x: float/int, number
    :return: the function funct_1
    """
    return round(x ** 2 + 3 * x + 1, 2)


def deriv_1(x):
    """

    :param x: float/int, number
    :return: the derivative of the function funct_1
    """
    return round(2 * x + 3, 4)


def forward_dif_1(x, h):
    return round((funct_1(x + h) - funct_1(x)) / (h), 2)


def center_dif_1(x, h):
    return round((funct_1(x + h) - funct_1(x - h)) / (2 * h), 2)


def get_h():
    return [0.1, 0.2, 0.3]


if __name__ == '__main__':
    try:
        x = round(float(input('Enter a number: ')), 2)
    except ValueError:
        print('That\'s not a number!')
    h_list = get_h()
    for h in h_list:
        print(f"""The function for x+h has the value {funct_1(x + h)}, and for x: {funct_1(x)}.
The forward difference is: {forward_dif_1(x, h)}.
The centered difference is: {center_dif_1(x, h)}.
Compared to the derivative: {deriv_1(x)}.
The differences are: {round(deriv_1(x) - forward_dif_1(x, h), 2)} ( O(h) ).
                     {round(deriv_1(x) - center_dif_1(x, h), 2)} ( O(h^2) ).
The proportions are: {round((deriv_1(x) - forward_dif_1(x, h)) / h, 2)} ( O(h) ).
                     {round((deriv_1(x) - center_dif_1(x, h)) / (h**2), 2)} ( O(h^2) ).
--------------------------------------------------------------------
""")
