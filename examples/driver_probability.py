import numpy as np
import matplotlib.pyplot as plt

from goph420_lab01.integration import (
    integrate_gauss,
)

x = np.linspace(4.1, 10, 100)


def stand_normal_prob(c):
    """"
    Uses equation 17.

    Note that z doesn't need to be used directly as the integration process will use it.
    """
    return (1 / np.sqrt(2 * np.pi)) * np.exp((-1 / 2) * c ** 2)

def prob_seismic(x):
    """
    For part i. of question 8.

    This function computes the probability of a seismic event with a magnitude greater than 4.0.
    """

    print(f'Computing the probability of a seismic event with magnitudes greater than 4...')
    x = np.asarray(x)  # convert x to an array
    mean = 1.5  # given in lab
    stdev = 0.5  # given in lab

    print(f'Mean: {mean}')
    print(f'Standard deviation: {stdev}')

    #  equation 18
    z = (x - mean) / stdev

    # integration limits
    lims = [2, 10]

    #  equation 24 + using gauss
    return integrate_gauss(stand_normal_prob, lims, 5)

def prob_distance():
    """
    For part ii. of question 8.

    This function determines the probability that the true value is between 10.25-10.35m.
    """
    L_mean = 10.28
    stdev = 0.5  # given in lab, from part i
    L1 = 10.25
    L2 = 10.35

    lims = [((L1 - L_mean) / stdev), ((L2 - L_mean) / stdev)]

    return integrate_gauss(stand_normal_prob, lims, 3)

def main():
    stand_gauss_norm = prob_seismic(x)
    print(f'Standard (Gaussian) Normal: {stand_gauss_norm}')

    gauss_prob = prob_distance()
    print(f'The probably of distance between 10.25 - 10.35m is: {gauss_prob}')

    # now we plot the convergence of probability estimates with increasing integration points.

    # first, defining variables
    points = np.array([1, 2, 3, 4, 5])
    mean = 1.5  # given in lab, from part i
    stdev = 0.05  # given in lab, from part ii
    magnitude = 4
    L_mean = 10.28  # from part ii.
    L1 = 10.25  # from part ii.
    L2 = 10.35  # from part ii.

    seismic_prob = []
    distance_prob = []

    z = (magnitude - mean) / stdev

    for i in points:
        seismic_prob.append(integrate_gauss(stand_normal_prob, [4, 10], i))
        distance_prob.append(integrate_gauss(stand_normal_prob, [(L1 - L_mean) / stdev, (L2 - L_mean) / stdev], i))

    print("Seismic Probabilities:", seismic_prob)
    print("Distance Probabilities:", distance_prob)

    plt.figure()
    plt.grid()
    plt.loglog(points, seismic_prob, "-r", label = "Seismic Probability")
    plt.loglog(points, distance_prob, "-b", label = "Distance Probability")
    plt.xlabel("Integration Points")
    plt.ylabel("Probability")
    plt.legend()
    plt.savefig("C:/Users/sydne/git/goph420/goph420-w2025-lab01-stSP/figures/probability_convergence.png")
    plt.show()


if __name__ == "__main__":
    main()



