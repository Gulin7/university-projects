import matplotlib.pyplot as plt
import math
import numpy as np


def efunc(x):
    return math.e ** (-(x ** 2))


def create_domain(left, right):
    """
    Creates a domain between left and right with elements increasing with 0,01 .

    :param left: the minimum/inf of the domain
    :param right: the max/sup of the domain
    :return: the domain
    """
    x = left
    domain = []
    while x < right:
        domain.append(x)
        x += 0.01
    return domain


def create_image_of_funct(domain, function):
    """

    :param function:
    :param domain: the domain of the function
    :return: the image of the function
    """
    image = []
    for element in domain:
        image.append(function(element))
    return image


if __name__ == '__main__':
    """
    This is to show what the graph of our function looks like"""
    while True:
        try:
            n = int(input('Enter a positive integer: '))
            if n > 0:
                break
            else:
                print('Not a positive number!')
        except ValueError:
            print('That\'s not an integer!!!')
        except:
            print('Invalid input!')
    figure, ((plt1, plt2), (plt3, plt4)) = plt.subplots(2, 2)
    figure.set_figwidth(10)
    figure.set_figheight(5)
    domain_1 = create_domain(-n, n)
    image_1 = create_image_of_funct(domain_1, efunc)
    plt1.plot(domain_1, image_1, color='purple', marker='o', linewidth='1')
    domain_2 = create_domain(-4, 4)
    image_2 = create_image_of_funct(domain_2, efunc)
    plt2.plot(domain_2, image_2, color='purple', marker='o', linewidth='1')
    domain_3 = create_domain(-10, 10)
    image_3 = create_image_of_funct(domain_3, efunc)
    plt3.plot(domain_3, image_3, color='purple', marker='o', linewidth='1')
    domain_4 = create_domain(-25, 25)
    image_4 = create_image_of_funct(domain_4, efunc)
    plt4.plot(domain_4, image_4, color='purple', marker='o', linewidth='1')
    plt.show()
    """
    We will now compute the result of the given integral as the trapezian rules says:
    -> our domain will consist of elements between [-2000,2000], 
    but the numbers can be modified for a more accurate result
    -> the elements Xk are the elements represented by the domain
    -> it is also shown that the result is indeed rad(pi)"""
    domain = create_domain(-5000, 5000)
    efunc_integral_value = 0
    for ind in range(len(domain) - 1):
        efunc_integral_value += (domain[ind + 1] - domain[ind]) * (efunc(domain[ind + 1]) + efunc(domain[ind])) / 2
    print(f"The result is: {efunc_integral_value}")
    print(f'The radical of pi is: {math.pi ** (1 / 2)}')
