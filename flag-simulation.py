import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parametry symulacji
p_numer_x = 30
p_number_y = 30
l_flag = 10.0
h_flag = 5.0
wind_amp = 0.1
wind_freq = 0.1
dt = 0.1
num_frames = 40

# Tworzenie siatki flagi
x = np.linspace(0, l_flag, p_numer_x)
y = np.linspace(0, h_flag, p_number_y)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)  # Początkowa pozycja flagi

# Symulacja napięcia materiału
def simulate(Z, dlugosc_x, dlugosc_y):
    Z_new = np.zeros_like(Z)
    # usrednianie pozycji z sasiadujacymi punktami
    for i in range(1, Z.shape[0] - 1):
        for j in range(1, Z.shape[1] - 1):
            Z_new[i, j] = (Z[i+1, j] + Z[i-1, j] + Z[i, j+1] + Z[i, j-1]) / 4
    # brzegi sa nieruchome
    Z_new[0, :] = Z[0, :]
    Z_new[:, 0] = Z[:, 0]
    Z_new[-1, :] = Z[-1, :]
    Z_new[:, -1] = Z[:, -1]
    return Z_new

# Główna pętla symulacji
for frame in range(num_frames):
    # Symulacja efektu wiatru
    Z += wind_amp * np.sin(2 * np.pi * (X * wind_amp * frame * dt))

    # Symulacja napięcia materiału
    Z = simulate(Z, l_flag / (p_numer_x - 1), h_flag / (p_number_y - 1))

    fig = plt.figure(figsize=(12, 6))  # Zwiększenie rozmiaru figury
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='r', edgecolor='k')
    
    ax.set_xlim([0, l_flag])
    ax.set_ylim([0, h_flag])
    ax.set_zlim(1.5 * np.min(Z), 1.5 * np.max(Z))  # Zwiększenie zakresu osi Z
    
    # kąt widzenia kamery
    ax.view_init(elev=25, azim=30)
