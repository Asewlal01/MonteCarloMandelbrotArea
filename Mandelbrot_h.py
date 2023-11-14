import numpy as np


def whenLeaveMandelbrotSet(c: complex, iterations: int):
    """
    Compute the mandelbrot equation with iter number of iterations

    :param c: Constant value
    :param iterations: Number of iterations
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

    return j + 1
