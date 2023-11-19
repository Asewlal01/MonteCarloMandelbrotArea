import numpy as np
from Mandelbrot import inMandelbrotSet
from scipy.stats import qmc


def quasiMC(low, high, iterations, samples):
    """
    Computes the area of the Mandelbrot set using Quasi Monte Carlo method
    Quasi Monte Carlo method uses Sobol' sequence random numbers instead of pseudo random numbers

    :param low: Minimum value of real and complex values for c
    :param high: Maximum value of real and complex values for c
    :param iterations: Number of iterations used in mandelbrot equation
    :param samples: Number of samples
    :return: Computed area of the Mandelbrot set
    """

    # The total area
    total = (high - low) ** 2

    # Number of points in mandelbrot set
    N = 0

    # Generating Sobol sequence between low and high
    sobol_seq = qmc.Sobol(d=2)
    seq = (high - low) * sobol_seq.random(n=samples) + low

    real = seq[:, 0]
    imag = seq[:, 1]

    # Calculate c
    c = real + 1j * imag

    for e in c:
        # Add to mandelbrot area if in set
        N += inMandelbrotSet(e, iterations)

    # Compute area of mandelbrot set
    mandelbrot = total * N / samples

    return mandelbrot
