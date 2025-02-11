import matplotlib.pyplot as plt
import numpy as np

from src.goph420_lab01.integration import (
    integrate_gauss
)

#  equation 18
z = (x - np.mean(x)) / sigma
lims = [np.inf, z]
#  equation 17
stand_normal_prob = (1/np.sqrt(2*np.pi))*np.exp((-1/2)*z**2)
#  equation 16
stand_gauss_norm = integrate_gauss(stand_normal_prob)

