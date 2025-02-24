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
        h = np.diff(x)  # step size
        integral = np.sum(h * (f[:-1] + f[1:]) / 2)  # h * average of all intermediate elements of f
        return integral

    def integrate_newton_simp(x, f):
        """
        This function performs numerical integration of discrete data using Simpson's multi-application rule.

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

        # using equation (6)
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

    if not callable(f):
        raise TypeError("The function f must be callable.")
    if not len(lims) == 2:
        raise ValueError("The parameter 'lims' must have two elements: a and b.")
    if lims[0] != float(lims[0]) or lims[1] != float(lims[1]):
        raise ValueError("lims[0] and lims[1] must be float convertible. ")
    if npts not in [1, 2, 3, 4, 5]:
        raise ValueError("npts must be either 1, 2, 3, 4, or 5.")

    # creating sample points and weights for integration over [-1, 1]
    xi_star, ci_star = np.polynomial.legendre.leggauss(npts)
    a, b = lims

    # shifts then scales sample points from [-1, 1] to [a, b], eq (9)
    xi = ((b + a) / 2) + (((b - a) / 2) * xi_star)

    # only scales weights from [-1, 1] to [a, b], eq (10)
    ci = ((b - a) / 2) * ci_star

    # approx integral
    integral = 0
    for i in range(npts):
        integral += ci[i] * f(xi[i])
    return integral
