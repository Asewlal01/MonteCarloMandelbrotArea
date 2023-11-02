import numpy as np


def mandelbrot(c: complex, iterations: int):
    """
    Compute the mandelbrot equation with iter number of iterations

    :param c: Constant value
    :param iterations: Number of iterations
    :return: Value after all iterations
    """

    # Get max value
    maxvalue = np.finfo(complex).max

    # Take square root
    maxvalue = np.sqrt(maxvalue)
    # Initial value for z
    z = c

    # Looping
    for _ in range(iterations):
        # If overflowing
        if abs(z) > maxvalue:
            return np.inf
        else:
            z = z ** 2 + c

    return z


def inMandelbrotSet(c, iterations):
    """
    Checks if c is in the Mandelbrot set

    :param c: Constant value
    :param iterations: Number of iterations
    :return: True if in set, otherwise false
    """

    # Check value
    val = mandelbrot(c, iterations)

    return val != np.inf


