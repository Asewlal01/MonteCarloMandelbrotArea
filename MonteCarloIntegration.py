import numpy as np
from Mandelbrot import inMandelbrotSet


def randomSampling(low, high, iterations, samples):
    """
    Computes the area of the Mandelbrot set using pure random sampling

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

    # Looping through samples
    for _ in range(samples):
        # Get random values for real and imaginary part of c
        real = np.random.uniform(low, high)
        imag = np.random.uniform(low, high)

        # Calculate c
        c = real + 1j * imag

        # Add to mandelbrot area if in set
        N += inMandelbrotSet(c, iterations)

    # Compute area of mandelbrot set
    mandelbrot = total * N / samples

    return mandelbrot


def latinHypercubeSampling(low, high, iterations, samples):
    """
    Computes the area of the Mandelbrot set using Latin Hypercube Sampling

    :param low: Minimum value of real and complex values for c
    :param high: Maximum value of real and complex values for c
    :param iterations: Number of iterations used in mandelbrot equation
    :param samples: Number of samples
    :return: Computed area of the Mandelbrot set
    """

    # Total area
    total = (high - low) ** 2

    # Create array with positions
    positions = np.arange(samples)

    # Shuffle array
    np.random.shuffle(positions)

    # Step size of real and imaginary axis
    step = (high - low) / (samples - 1)

    # Number of points in mandelbrot set
    N = 0

    # Loop through each position
    for i, j in enumerate(positions):
        # Convert i,j to a complex value a+bi
        a = i * step + low
        b = j * step + low

        # To c
        c = a + 1j * b

        # Add to mandelbrot area if in set
        N += inMandelbrotSet(c, iterations)

    # Compute area
    mandelbrot = total * N / samples

    return mandelbrot


def orthogonalSampling(low, high, iterations, samples):
    """
    Computes the area of the Mandelbrot set using Orthogonal Sampling

    :param low: Minimum value of real and complex values for c
    :param high: Maximum value of real and complex values for c
    :param iterations: Number of iterations used in mandelbrot equation
    :param samples: Number of samples
    :return: Computed area of the Mandelbrot set
    """

    # Total area
    total = (high - low) ** 2

    # Samples has to be a perfect square
    sqr = int(np.floor(np.sqrt(samples)))
    samples = sqr ** 2

    # Create array with minor columns
    columns = np.linspace(low, high, samples)

    # Randomly shuffle minor columns
    np.random.shuffle(columns)

    # Creating major rows
    rows = np.linspace(low, high, sqr + 1)

    # Number of points in mandelbrot
    N = 0

    # Looping through each major row
    for i in range(len(rows) - 1):
        # Creating array with minor rows in current row
        minorrow = np.linspace(rows[i], rows[i + 1], sqr, endpoint=False)

        # Shuffling minor row
        np.random.shuffle(minorrow)

        # Looping through each minor row
        for j in range(len(minorrow)):
            # Create complex number
            c = columns[sqr * i + j] + 1j * minorrow[j]

            # Add to mandelbrot area if in set
            N += inMandelbrotSet(c, iterations)

    # Compute area
    mandelbrot = total * N / samples

    return mandelbrot
