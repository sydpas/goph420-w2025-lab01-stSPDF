import matplotlib.pyplot as plt
import numpy as np

def main():
    data = np.loadtxt("C:/Users/sydne/git/goph420/goph420-w2025-lab01-stSP/data/s_wave_data.txt")
    t_data = data[:,0]
    v_data = data[:,1]
    v2_data = v_data**2

    plt.figure(figsize=(6, 8))

    plt.subplot(2,1,1)
    plt.grid()
    plt.plot(t_data, v_data, "-b", label="Seismic wave data")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (mm/s)")
    plt.legend()

    plt.subplot(2,1,2)
    plt.grid()
    plt.plot(t_data, v2_data, "-r", label="Seismic wave data")
    plt.xlabel("Time (s)")
    plt.ylabel("Squared velocity (mm/s)")
    plt.legend()

    plt.suptitle("Velocity as a Function of Time", fontsize=14)
    plt.savefig("C:/Users/sydne/git/goph420/goph420-w2025-lab01-stSP/figures/s_wave_figure.png")
    plt.show()

if __name__ == "__main__":
    main()