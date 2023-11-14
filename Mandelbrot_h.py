import numpy as np


def mandelbrot(c: complex, iterations: int):
    """
    Compute the mandelbrot equation with iter number of iterations

    :param c: Constant value
    :param iterations: Number of iterations
    :return: Value after all iterations
    :return: The interation number when abs(z) becomes larger than 2
    """

    # Initial value for z
    z = c

    # Looping
    for j in range(iterations):
        # Goes to infinity
        if abs(z) > 2:
            return j
        else:
            z = z**2 + c

    return z, -1


def inMandelbrotSet(c: complex, iterations: int):
    """
    Checks if c is in the Mandelbrot set

    :param c: Constant value
    :param iterations: Number of iterations
    :return: True if in set, otherwise false
    :return: When abs(z) > 2
    """

    # Check value
    val, j = mandelbrot(c, iterations)

    return val != np.inf, j
