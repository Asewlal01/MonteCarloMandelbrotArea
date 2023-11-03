import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c: complex, iterations: int):
    """
    Compute the mandelbrot equation with iter number of iterations

    :param c: Constant value
    :param iterations: Number of iterations
    :return: Value after all iterations
    """

    # Initial value for z
    z = c

    # Looping
    for _ in range(iterations):
        # Goes to infinity
        if abs(z) > 2:
            return np.inf
        else:
            z = z ** 2 + c

    return z


def inMandelbrotSet(c: complex, iterations: int):
    """
    Checks if c is in the Mandelbrot set

    :param c: Constant value
    :param iterations: Number of iterations
    :return: True if in set, otherwise false
    """

    # Check value
    val = mandelbrot(c, iterations)

    return val != np.inf


def mandelbrotSet(low: complex, high: complex, N: int, iterations: int):
    """

    :param low: Lowest value for real and imaginary part of c
    :param high: Highest value for real and imaginary part of c
    :param N: Number of points between low and high on real and imaginary axis
    :param iterations: Number of iterations
    :return: N x N array with bool where true represents in set
    """

    # Get all points
    x = np.linspace(low, high, N)

    # Create mandelbrot set
    mandel = []

    # Looping through all c's
    for a in x:
        # Saving for changing b's
        lst = []
        for b in x:
            # Getting c
            c = a + b * 1j

            # Add to list
            lst.append(inMandelbrotSet(c, iterations))

        # Add to mandelbrot set
        mandel.append(lst)

    return np.array(mandel)


def showMandelbrot(low: complex, high: complex, N: int, iterations: int,
                   color: list = None, background: list = None):
    """
    Function used to show the mandelbrot set based on input

    :param low: Lowest value for real and imaginary part of c
    :param high: Highest value for real and imaginary part of c
    :param N: Number of points between low and high on real and imaginary axis
    :param iterations: Number of iterations
    :param color: Color to give to points that belong to mandelbrot set
    :param background: Color of background (parts that do not belong to mandelbrot set)
    :return: Void
    """
    # Get mandelbrot set
    mandel = mandelbrotSet(low, high, N, iterations).T

    # Set colors
    colors = np.zeros((N, N, 3))

    # Setting the color
    if color is None:
        color = np.array([255, 255, 255])
    else:
        color = np.array(color)

    # Setting the background
    if background is None:
        background = np.array([0, 0, 0])
    else:
        background = np.array(background)

    for i in range(len(mandel)):
        for j in range(len(mandel)):
            if mandel[i, j]:
                colors[i, j] = color
            else:
                colors[i, j] = background

    # Float to int
    colors = colors.astype(int)

    # Show image
    plt.imshow(colors, origin='lower', extent=[low, high, low, high])

    # Set axis labels
    plt.xlabel('$Real$')
    plt.ylabel('$Imaginary$')

    # Show image
    plt.show()

