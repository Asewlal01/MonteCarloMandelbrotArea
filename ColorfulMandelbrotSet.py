import numpy as np
import matplotlib.pyplot as plt


def mandelbrot_Set_Image(re_low: float, re_high: float, im_low: float, im_high: float, re_res: int, im_res: int,
                         iterations: int):
    """
    Creates image of Mandelbrot Set within the given range
    """
    X = np.linspace(re_low, re_high, re_res)
    Y = np.linspace(im_low, im_high, im_res)
    Z = np.zeros((re_res, im_res), dtype=complex)

    i = 0
    for a in X:
        j = 0
        for b in Y:
            Z[j][i] = a + 1j * b
            j += 1
        i += 1

    C = Z
    colors = np.zeros(Z.shape)
    for i in range(iterations):
        Z = Z ** 2 + C
        addition = np.abs(Z) < 10
        colors += addition
    plt.imshow(colors, extent=(re_low, re_high, im_low, im_high), cmap="jet")
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.show()
    return
