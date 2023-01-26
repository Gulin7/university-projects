from matplotlib import pyplot as plt


def calculate_the_points_coordinates(given_norm):
    """
    Calculates the coordinates of all the points that are inside the ball of given norm.

    :param given_norm: float, given_norm
    :return: the list of points(as coords) that are in the ball
    """
    points = []
    reverse_norm = 1 / given_norm
    x = 0.00
    while x <= 1:
        y = 0.00
        x_at_power_norm = x ** given_norm
        while y <= 1:
            if (x_at_power_norm + y ** given_norm) ** reverse_norm < given_norm:
                points.append([x, y])
                points.append([-x, -y])
                points.append([-x, y])
                points.append([x, -y])
            y += 0.04
        x += 0.04
    return points


if __name__ == '__main__':

    # CREATE THE FIGURE
    figure, ((plt_1_25, plt_1_5), (plt_3, plt_8)) = plt.subplots(2, 2, figsize=(8, 8))

    # GET THE LIST OF POINTS
    points_1_25 = calculate_the_points_coordinates(1.25)
    points_1_5 = calculate_the_points_coordinates(1.5)
    points_3 = calculate_the_points_coordinates(3)
    points_8 = calculate_the_points_coordinates(8)

    # PLOT EACH POINT
    for point in points_1_25:
        plt_1_25.plot(point[0], point[1], marker='o', color='blue')
    for point in points_1_5:
        plt_1_5.plot(point[0], point[1], marker='o', color='purple')
    for point in points_3:
        plt_3.plot(point[0], point[1], marker='o', color='yellow')
    for point in points_8:
        plt_8.plot(point[0], point[1], marker='o', color='red')

    # SHOW THE PLOT
    plt.show()
