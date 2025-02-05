import numpy as np


def integrate_newton(x, f, alg):
    """
    This function performs numerical integration of discrete data using the Newton-Cotes rules.

    Parameters
    -----
    x: array_like
        Contains the coordinates of sample points.
    f: array_like, same shape as x
        Contains the values of sample points.
    alg: (optional) str flag
        Has a default value of "trap" and "simp" based on algorithm used.

    Returns
    -----
    float: float
        Provides the integral estimate.

    Notes
    -----
    Assume constant step size for x.

    Raises
    -----
    ValueError
        If x and f do not have the same length.
    """

    x = np.asarray(x).flatten()
    f = np.asarray(f).flatten()

    if len(x) != len(f):
        raise ValueError(f'len(x) is {len(x)}, len(f) is {len(f)}, but they should be equal.')

    def integrate_newton_trap(x, f):
        """
        This function performs numerical integration of discrete data using the trapezoid rule.

        Parameters
        -----
        x: array_like
            Contains the coordinates of sample points.
        f: array_like, same shape as x
            Contains the values of sample points.

        Returns
        -----
        integral: float
            Provides the integral estimate.
        """
        h = np.diff(x)  # calc difference between values
        integral = np.sum(h * (f[:-1] + f[1:]) / 2)  # h * average of all intermediate elements of f
        return integral


    def integrate_newton_simp(x, f):
        """
        This function performs numerical integration of discrete data using Simpson's rule.

        Parameters
        -----
        x: array_like
            Contains the coordinates of sample points.
        f: array_like, same shape as x
            Contains the values of sample points.

        Returns
        -----
        integral: float
            Provides the integral estimate.

        Raises
        -----
        ValueError
            If the number of points is not odd.
        """

        if len(x) % 2 == 0:  # make sure the number of points is odd
           raise ValueError("The number of points (len(x)) must be odd for Simpson's 1/3 rule.")

        n = len(x) - 1  # number of intervals
        h = (x[-1] - x[0]) / n  # step size

        integral = f[0] + f[-1]  # first and law terms
        integral += 4 * np.sum(f[1:-1:2])  # odd terms
        integral += 2 * np.sum(f[2:-2:2])  # even terms
        integral *= h / 3  # multiply by 1/3
        return integral

    if alg.strip().lower() == 'trap':
        return integrate_newton_trap(x, f)
    elif alg.strip().lower() == 'simp':
        return integrate_newton_simp(x, f)
    elif alg not in ['trap', 'simp']:
        raise TypeError("Please use either the Trapezoid rule or Simpson's rule.")

def integrate_gauss(f, lims, npts):
    """
    This function performs numerical integration of a function using Gauss-Legendre quadrature.

    Parameters
    -----
    f: callable object
        Function to be integrated.
    lims: object with len(2).
        Contains the lower and upper bound of integration.
    npts: int
        Has possible values of 1, 2, 3, 4, 5, but a default of 3.

    Returns
    -----
    float: float
        Provides the integral estimate.

    Notes
    -----


    Raises
    -----
    TypeError
        If f is not callable.
    ValueError
        If lims does not have a length of 2.
    ValueError
        If lims[0] or lims[1] are not float convertible.
    ValueError
        If npts is not one of the possible values.
    """

