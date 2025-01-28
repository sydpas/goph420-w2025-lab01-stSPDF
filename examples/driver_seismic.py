

def main():
    data = np.loadtxt("data/s_wave_data.txt")
    t_data = data[:,0]
    v_data = data[:,1]

    plt.figure()
    plt.plot(t_data, v_data, "--", label="s_wave_data")
    plt.xlabel("time (s)")
    plt.ylabel("velocity (mm/s)")
    plt.legend()
    plt.savefig("examples/s_wave_data.png")