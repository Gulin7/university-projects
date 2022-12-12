import numpy as np
import matplotlib.pyplot as plt


def gradient_descent(start, gradient, learn_rate, max_steps, tollerance=0.001):
    steps = [start]
    x = start
    for index in range(max_steps):
        diff = learn_rate * gradient(x)
        if np.abs(diff) < tollerance:
            break
        x = x - diff
        steps.append(x)
    return steps, x


def function_1(x):
    return x ** 2 - 4 * x + 7


def gradient_1(x):
    return 2 * x - 4


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


# NON-CONVEX
def function_2(x):
    return (x - 1) * x * (x + 1)


def gradient_2(x):
    return 3 * x ** 2 - 1


if __name__ == '__main__':
    domain_1 = create_domain(-1000, 1000)
    image_1 = create_image_of_funct(domain_1, function_1)
    figure, ((plt1, plt2), (plt3, plt4)) = plt.subplots(2, 2)
    figure.set_figwidth(20)
    figure.set_figheight(10)
    #
    found_elements, x = gradient_descent(1000, gradient_1, 0.05, 50)
    image_found = create_image_of_funct(found_elements, function_1)
    plt1.plot(domain_1, image_1, color='black', linewidth='3')
    plt1.plot(found_elements, image_found, linestyle="dashed", marker='o', color='purple')
    #
    found_elements, x = gradient_descent(1000, gradient_1, 0.2, 50)
    image_found = create_image_of_funct(found_elements, function_1)
    plt2.plot(domain_1, image_1, color='black', linewidth='3')
    plt2.plot(found_elements, image_found, linestyle="dashed", marker='o', color='purple')
    #
    domain_3 = create_domain(-10000, 10000)
    image_3 = create_image_of_funct(domain_3, function_1)
    found_elements, x = gradient_descent(10000, gradient_1, 0.8, 50)
    image_found = create_image_of_funct(found_elements, function_1)
    plt3.plot(domain_3, image_3, color='black', linewidth='3')
    plt3.plot(found_elements, image_found, linestyle="dashed", marker='o', color='purple')
    #
    domain_2 = create_domain(-1000, 1000)
    image_2 = create_image_of_funct(domain_2, function_2)
    found_elements, x = gradient_descent(1000, gradient_2, 0.0001, 20)
    image_found = create_image_of_funct(found_elements, function_2)
    plt4.plot(domain_2, image_2, color='black', linewidth='3')
    plt4.plot(found_elements, image_found, linestyle="dashed", marker='o', color='purple')
    #
    plt.show()
