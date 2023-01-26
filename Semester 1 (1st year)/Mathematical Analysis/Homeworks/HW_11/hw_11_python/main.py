import numpy as np
import matplotlib.pyplot as mpplt


# To do: plot the level curves of f1, f2, f3, f4, f5, f6 where
# All fucntions are defined over R^2 with values in R and are defined as [x y]* A* ┌x┐
# 														                                                     └y┘
# f1, f2 have a unique minimum
# f3, f4 have a unique maximum
# f5, f6 have a unique saddle point

# A1 = [[1, 0],
#       [0, 1]]


def f1(x, y):
	return x ** 2 + y ** 2


def gradient_f1(x, y):
	return 2 * x, 2 * y


# A2 = [[1, 1],
#      [-1, 1]]
# f1(x, y)= f2(x, y)


def f2(x, y):
	return x ** 2 + y ** 2


def gradient_f2(x, y):
	return 2 * x, 2 * y


# A3 = [[-1, 0],
#       [0, -1]]


def f3(x, y):
	return -1 * (x ** 2) - (y ** 2)


def gradient_f3(x, y):
	return (-2) * x, (-2) * y


# A4 = [[-1, -1],
#       [1, -1]]
# f3(x, y)= f4(x, y)


def f4(x, y):
	return -1 * (x ** 2) - (y ** 2)


def gradient_f4(x, y):
	return (-2) * x, (-2) * y


# A5 = [[1, 0],
#      [0, -1]]


def f5(x, y):
	return x ** 2 - y ** 2


def gradient_f5(x, y):
	return 2 * x, (-2) * y


# A6 = [[1, 1],
#      [-1, -1]]
# f5(x, y)= f6(x, y)


def f6(x, y):
	return x ** 2 - y ** 2


def gradient_f6(x, y):
	return 2 * x, (-2) * y


# x(k+1) = x(k) + df/dx(x(k))
# y(k+1) = y(k) + df/dy(y(k))
def plot_level_curves(function, function_gradient, x_start, y_start):
	# x_start and y_start are lists of coordonates for the 3 points where we calculate the gradient and level contours at
	x_end = x_start[:]
	y_end = y_start[:]

	for index in range(3):
		dfdx, dfdy = function_gradient(x_start[index], y_start[index])
		x_end[index] += dfdx
		y_end[index] += dfdy

	xlist = np.linspace(-10, 10, 1000)
	ylist = np.linspace(-10, 10, 1000)
	xspace, yspace = np.meshgrid(xlist, ylist)
	zspace = function(xspace, yspace)
	number_of_levels = len(x_start)
	levels = np.zeros(number_of_levels)
	for index in range(len(x_start)):
		levels[index] = function(x_start[index], y_start[index])
	levels = np.sort(levels)
	contours = mpplt.contour(xspace, yspace, zspace, levels, colors = 'black')
	mpplt.title(str(function).split()[1])
	mpplt.clabel(contours, fontsize = 8)
	for index in range(3):
		mpplt.plot([x_start[index], x_end[index]], [y_start[index], y_end[index]], 'g--o', linestyle = "-")
	mpplt.show()


if __name__ == "__main__":
	list_of_functions = [f1, f2, f3, f4, f5, f6]
	x_start = list(np.arange(0, 6))

	plot_level_curves(f1, gradient_f1, [-1, 3, -5], [1, 3, -5])

	plot_level_curves(f2, gradient_f2, [1, -3, 5], [1, 3, -5])

	plot_level_curves(f3, gradient_f3, [1, -3, -5], [1, 3, -5])

	plot_level_curves(f4, gradient_f4, [-1, -3, 5], [-1, 3, -5])

	plot_level_curves(f5, gradient_f5, [1, -3, -8], [-3, 6, -9])

	plot_level_curves(f6, gradient_f6, [-1, 3, -8], [-3, -6, 9])
