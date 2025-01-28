import matplotlib as plt


def main():
    data = np.loadtxt("data/s_wave_data.txt")
    t_data = data[:,0]
    v_data = data[:,1]
