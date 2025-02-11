import scipy as sp
import numpy as np

from goph420_lab01.integration import (
    integrate_gauss
)


def test_gauss_legendre():
    f = lambda x: np.sin(x)  # function to test
    lims = [0, np.pi/2]  # limits
    print("Testing Gauss Legendre rule...")
    print(f'Using f(x) from a = {lims[0]} to b = {lims[1]}...')  # Manually print the function

    for n in range(1, 10):
        I_exp, _ = sp.integrate.fixed_quad(f, lims[0], lims[1], n = n + 1)  # _ is to extract only the integral
        I_act = integrate_gauss(f, lims, npts = 3)

        print(f'Expected: {I_exp}')
        print(f'Actual: {I_act}')

if __name__ == "__main__":
    test_gauss_legendre()