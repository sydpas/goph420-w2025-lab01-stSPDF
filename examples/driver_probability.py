import matplotlib.pyplot as plt
import numpy as np

from goph420_lab01.integration import (
    integrate_gauss
)

list = [4,5,6]

def prob_seismic(x):
    x = np.asarray(x)
    #  equation 18
    z = (x - np.mean(x)) / np.std(x)
    lims = [-np.inf, z]
    # test
    #  equation 17
    stand_normal_prob = (1/np.sqrt(2*np.pi)) * np.exp((-1/2)*z**2)
    #  equation 16
    stand_gauss_norm = integrate_gauss(stand_normal_prob, lims, 3)
    print(stand_gauss_norm)

if __name__ == "__main__":
    prob_seismic(list)



