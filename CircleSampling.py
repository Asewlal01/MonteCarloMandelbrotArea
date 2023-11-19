import math
import numpy as np
from Mandelbrot_h import whenLeaveMandelbrotSet as wlms


def RS_circle(iter_num: int, s_num: int, R: int = 2) -> np.ndarray:
    '''Compute the area of the Mandelbrot set by pure random sampling within a circle.
    Parameters:
        iter_num: the number of iterations (i)
        s_num: the number of samples (s)
        R: the radius of the circle
    Returns:
        A_h: the areas of the Mandelbrot set during the run
    '''
    history = np.zeros((s_num, iter_num))
    # history is the historical data for all samples at each step in the iteration
    for s in range(s_num):
        U1 = np.random.uniform(0, 1)
        U2 = np.random.uniform(0, 1)
        theta = U1 * 2 * math.pi
        r = R * math.sqrt(U2)
        real = r * math.cos(theta)
        imag = r * math.sin(theta)
        c = complex(real, imag)
        j = wlms(c, iter_num)
        # j is the iteration number when c leave the Mandelbrot set
        # If c never leave the Mandelbrot set, j = iter_num
        history[s, :j] = 1

    # Compute the area of the Mandelbrot set
    N_h = history.sum(axis=0)
    # N_h is the number of samples that are in the Mandelbrot set during the run
    A_total = math.pi * R**2  # The area of the sampling region
    A_h = N_h / s_num * A_total

    return A_h


def LHS_circle(iter_num: int, s_num: int, R: int = 2) -> np.ndarray:
    '''Compute the area of the Mandelbrot set by Latin hypercube sampling within a circle.
    Parameters:
        iter_num: the number of iterations (i)
        s_num: the number of samples (s)
        R: the radius of the circle
    Returns:
        A_h: the areas of the Mandelbrot set during the run
    '''
    idx = np.arange(s_num)
    np.random.shuffle(idx)
    history = np.zeros((s_num, iter_num))
    # history is the historical data for all samples at each step in the iteration
    for s in range(s_num):
        U1 = np.random.uniform(0, 1)
        U2 = np.random.uniform(0, 1)
        # Split the circular sampling region into s sectors, and get the RV: theta
        theta = 2 * math.pi * (s + U1) / s_num
        # Divide the sector into s equal parts of equal area, and get the RV: r
        r = R * math.sqrt((idx[s] + U2) / s_num)
        real = r * math.cos(theta)
        imag = r * math.sin(theta)
        c = complex(real, imag)
        j = wlms(c, iter_num)
        # j is the iteration number when c leave the Mandelbrot set
        # If c never leave the Mandelbrot set, j = iter_num
        history[s, :j] = 1

    # Compute the areas of the Mandelbrot set during the run
    N_h = history.sum(axis=0)
    # N_h is the number of samples that are in the Mandelbrot set during the run
    A_total = math.pi * R**2  # The area of the sampling region
    A_h = N_h / s_num * A_total

    return A_h


def OS_circle(iter_num: int, s_num: int, R: int = 2) -> np.ndarray:
    '''Compute the area of the Mandelbrot set by orthogonal sampling within a circle.
    Parameters:
        iter_num: the number of iterations (i)
        s_num: the number of samples (s)
        R: the radius of the circle
    Returns:
        A_h: the areas of the Mandelbrot set during the run
    '''
    # Radius of the sampling region
    R = 2

    # Samples has to be a perfect square
    sqr = int(np.floor(np.sqrt(s_num)))
    s_num = sqr**2

    # Create array with minor sectors
    sectors = np.linspace(0, 2 * math.pi, s_num)

    # Randomly shuffle minor sectors
    np.random.shuffle(sectors)

    # Creating major rings
    rings = R * np.sqrt(np.linspace(0, 1, s_num + 1))

    # Creating the historical data for all samples at each step in the iteration
    history = np.zeros((s_num, iter_num))

    # Looping through each major ring
    for i in range(sqr):
        # Creating array with minor rings in current
        low = i * sqr
        high = (i + 1) * sqr
        minor_rings = rings[low:high]

        # Shuffling minor rings
        np.random.shuffle(minor_rings)

        # Looping through each minor ring
        for j in range(sqr):
            # Creating complex number
            s = sqr * i + j
            theta = sectors[s]
            l = minor_rings[j]
            real = l * math.cos(theta)
            imag = l * math.sin(theta)
            c = complex(real, imag)

            # Adding to mandelbrot
            # j is the iteration number when c leave the Mandelbrot set
            # If c never leave the Mandelbrot set, j = iter_num
            j = wlms(c, iter_num)
            history[s, :j] = 1

    # Computing the number of samples that are in the Mandelbrot set during the run
    N_h = history.sum(axis=0)

    # Computing the area of the sampling region
    A_total = math.pi * R**2

    # Computing the areas during the run
    A_h = N_h / s_num * A_total

    return A_h
