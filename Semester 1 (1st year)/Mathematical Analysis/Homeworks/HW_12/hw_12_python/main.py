import random
import numpy as np
import matplotlib.pyplot as mpplt

EPSILON = 0.01  # Represents the range of admitted errors when nearing the min point
LAMBDA = 50  # Represents the maximum number of steps the descent should have in order to find the min point
LATEST_ELEMENT = -1
X_SPOT = 0
Y_SPOT = 1
CHART_BOUND = 100  # Should always be a positive integer


def f(x, y, b):
	return (1 / 2) * ((x ** 2) + b * (y ** 2))


def gradient_f(x, y, b):
	return x, b * y


def step(x, y, b):
	return 1 - (((b ** 3) * (y ** 2) - ((b * y) ** 2)) / ((b ** 3) * (y ** 2) + (x ** 2)))


def next_step(x, y, b):
	return x * (1 - step(x, y, b)), y * (1 - b * step(x, y, b))


def descend(x_start, y_start, b):
	x = [x_start]
	y = [y_start]
	dfdx, dfdy = gradient_f(x_start, y_start, b)
	while (abs(dfdx) >= EPSILON or abs(dfdy) >= EPSILON) and len(x) <= LAMBDA:
		next_x, next_y = next_step(x[LATEST_ELEMENT], y[LATEST_ELEMENT], b)
		x.append(next_x)
		y.append(next_y)
		dfdx, dfdy = gradient_f(x[LATEST_ELEMENT], y[LATEST_ELEMENT], b)
	return x, y


def show_data_points(x_list, y_list, b):
	print("b ==", b)
	for index in range(len(x_list)):
		print(index, ". ", x_list[index], ", ", y_list[index], "-> ", f(x_list[index], y_list[index], b))


def plot_descent(x_start, y_start, b):
	x_descent, y_descent = descend(x_start, y_start, b)
	show_data_points(x_descent, y_descent, b)

	x_space = np.linspace(-1 * CHART_BOUND, CHART_BOUND + 0.1, 100)
	y_space = np.linspace(-1 * CHART_BOUND, CHART_BOUND + 0.1, 100)
	x_val, y_val = np.meshgrid(x_space, y_space)
	z_val = f(x_val, y_val, b)
	levels = []
	for k in range(len(x_descent)):
		levels.append(f(x_descent[k], y_descent[k], b))
	levels = np.sort(levels)
	contours = mpplt.contour(x_val, y_val, z_val, levels, colors = 'black')
	mpplt.clabel(contours, inline = True, fontsize = 8)
	mpplt.plot(x_descent, y_descent, 'r--o')
	mpplt.title("b == " + str(b) + " (" + str(len(x_descent)) + " steps)")
	mpplt.show()


if __name__ == "__main__":
	for b in [1, 1 / 2, 1 / 5, 1 / 10]:
		plot_descent(random.randint(-1 * CHART_BOUND + (CHART_BOUND // 2), CHART_BOUND - (CHART_BOUND // 2)),
		             random.randint(-1 * CHART_BOUND + (CHART_BOUND // 2), CHART_BOUND - (CHART_BOUND // 2)), b)
