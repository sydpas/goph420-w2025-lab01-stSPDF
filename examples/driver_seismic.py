import matplotlib.pyplot as plt
import numpy as np

from goph420_lab01.integration import (
    integrate_newton,
)

def main():
    data = np.loadtxt("C:/Users/sydne/git/goph420/goph420-w2025-lab01-stSP/data/s_wave_data.txt")
    t_data = data[:,0]
    v_data = data[:,1]
    v2_data = v_data**2

    # part 1

    plt.figure(figsize=(6, 8))

    plt.subplot(2,1,1)
    plt.grid()
    plt.plot(t_data, v_data, "-b", label="Seismic wave data")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (mm²/s²)")
    plt.legend()

    plt.subplot(2,1,2)
    plt.grid()
    plt.plot(t_data, v2_data, "-r", label="Squared Seismic wave data")
    plt.xlabel("Time (s)")
    plt.ylabel("Squared velocity (mm²/s²)")
    plt.legend()

    plt.suptitle("Velocity as a Function of Time", fontsize=14)

    # find the maximum absolute velocity and the boundary when v > 0.005 vmax which will be T

    # find the max abs velocity (strongest seismic wave)
    boundary = 0.005 * np.max(np.abs(v_data))  # and multiply by 0.005 to find the significant velocity points
    T_boundary = np.where(np.abs(v_data) > boundary)[0]  # find velocity about the boundary
    T = t_data[T_boundary[-1]]  # find the last time when velocity is above the boundary

    print(f'Estimated duration when velocity is significant: {T} seconds')

    # integrate v^2 over T using trap and simp

    integral_trap = integrate_newton(t_data, v2_data, "trap")
    integral_simp = integrate_newton(t_data, v2_data, "simp")

    print(f'Average squared velocity using trapezoid rule: {integral_trap} mm²/s²')
    print(f"Average squared velocity using Simpson's 1/3 rule: {integral_simp} mm²/s²")

    # plot the convergence by plotting delta t against approx rel error in log-log space

    plt.savefig("C:/Users/sydne/git/goph420/goph420-w2025-lab01-stSP/figures/s_wave_figure.png")
    plt.show()


if __name__ == "__main__":
    main()