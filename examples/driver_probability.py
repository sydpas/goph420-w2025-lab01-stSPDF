import numpy as np
import matplotlib.pyplot as plt

from goph420_lab01.integration import (
    integrate_gauss,
)


def stand_normal_prob(z):
    """"
    Uses equation 17.
    """
    return (1 / np.sqrt(2 * np.pi)) * np.exp((-1 / 2) * z ** 2)


def probability_seismic(magnitude, mean, stdev, npts):
    """
    # for part i. of question 8
    # computing the probability of a seismic event with a magnitude greater than 4.0.
    """

    # equation 18
    z = (magnitude - mean) / stdev

    # integration limits
    lims = [z, 10]

    return integrate_gauss(stand_normal_prob, lims, npts)

def probability_distance(L1, L2, L_mean, stdev, npts):
    """
    for part ii. of question 8.
    # determining the probability that the true value is between 10.25-10.35m.
    """
    # integration limits
    lims = [((L1 - L_mean) / stdev), ((L2 - L_mean) / stdev)]

    return integrate_gauss(stand_normal_prob, lims, npts)

def main():
    mean = 1.5
    stdev = 0.5
    magnitude = 4
    L_mean = 10.28
    L1 = 10.25
    L2 = 10.35
    npts_list = [1, 2, 3, 4, 5]

    prob_gt_4 = [probability_seismic(magnitude, mean, stdev, npts) for npts in npts_list]
    print(f'Probability of an earthquake with magnitude greater than 4: {prob_gt_4}')

    prob_true_value = [probability_distance(L1, L2, L_mean, stdev, npts) for npts in npts_list]
    print(f'The probably of distance between 10.25 - 10.35m is: {prob_true_value}')

    # now we plot the convergence of probability estimates with increasing integration points.
    seismic_prob = []
    distance_prob = []

    for npts in npts_list:
        seismic_prob.append(integrate_gauss(stand_normal_prob, [4, 10], npts))
        distance_prob.append(
            integrate_gauss(stand_normal_prob, [(L1 - L_mean) / stdev, (L2 - L_mean) / stdev], npts))

    print("Seismic Probabilities:", seismic_prob)
    print("Distance Probabilities:", distance_prob)

    plt.figure(figsize=(10, 4))

    # seismic Probability Plot
    plt.subplot(1, 2, 1)
    plt.grid()
    plt.plot(npts_list, seismic_prob, "-r", label="Seismic Probability")
    plt.xlabel("Integration Points")
    plt.ylabel("Probability")
    plt.title("Seismic Probability Convergence")
    plt.legend()

    # distance Probability Plot
    plt.subplot(1, 2, 2)
    plt.grid()
    plt.plot(npts_list, distance_prob, "-b", label="Distance Probability")
    plt.xlabel("Integration Points")
    plt.ylabel("Probability")
    plt.title("Distance Probability Convergence")
    plt.legend()

    plt.tight_layout()
    plt.savefig("C:/Users/sydne/git/goph420/goph420-w2025-lab01-stSP/figures/probability_plots.png")
    plt.show()


if __name__ == "__main__":
    main()



