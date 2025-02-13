import numpy as np

from goph420_lab01.integration import (
    integrate_gauss
)

x = np.linspace(4.1, 9.9, 100)

def prob_seismic(x):
    """
    For part i. of question 8.
    """

    print(f'Computing the probability of a seismic event with magnitudes greater than 4...')
    x = np.asarray(x)  # convert x to an array
    mean = 1.5  # given in lab
    stdev = 0.5  # given in lab

    print(f'Mean: {mean}')
    print(f'Standard deviation: {stdev}')

    #  equation 18
    z = (x - mean) / stdev

    def stand_normal_prob(c):
        #  equation 17
        return (1/np.sqrt(2 * np.pi)) * np.exp((-1/2) * c ** 2)
        #  z doesn't need to be used directly as the integration process will use it

    # integration limits
    lims = [0, np.max(z)]

    #  equation 24 + using gauss
    stand_gauss_norm = integrate_gauss(stand_normal_prob, lims, 3)

    print(f'Standard (Gaussian) Normal: {stand_gauss_norm}')


if __name__ == "__main__":
    prob_seismic(x)



