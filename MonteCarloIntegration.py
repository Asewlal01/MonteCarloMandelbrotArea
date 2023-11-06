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

    # Cuberoot of samples should be an integer to make subgrids
    sqr = np.ceil(samples ** (1 / 3)).astype(int)

    # Step size
    step = (high - low) / sqr

    # Step size in subgrids
    substep = step / (sqr - 1)

    # Number of points that are within mandelbrot set
    N = 0

    # Looping through subgrids
    for i in range(sqr):
        # Lowest point of subgrid on horizontal axis
        sublow_x = i * step + low

        for j in range(sqr):
            # Lowest point of subgrid on vertical axis
            sublow_y = j * step + low

            # Create array with positions
            positions = np.arange(sqr)

            # Shuffling positions
            np.random.shuffle(positions)

            for ii, jj in enumerate(positions):
                # Convert i,j to a complex value a+bi
                a = ii * substep + sublow_x
                b = jj * substep + sublow_y

                # Compute c
                c = a + 1j * b

                # Add to mandelbrot area if in set
                N += inMandelbrotSet(c, iterations)

    # Compute area
    mandelbrot = total * N / samples

    return mandelbrot