#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:06:50 2023

@author: 21203241
"""

import numpy as np
import matplotlib.pyplot as plt

# Paramètres de la simulation
L = 1.3         # Longueur du domaine carré
N = 75          # Nombre de points en x et y
dx = L/N        # Espace entre les points
dt = 0.01       # Pas de temps
tmax = 0.45      # Durée de la simulation
amplitude = 0.5 # Amplitude des ondes

# Initialisation des variables
u = np.zeros((N,N)) # Hauteur de l'onde
v = np.zeros((N,N)) # Vitesse de l'onde

# Conditions initiales : plusieurs ondes à différents endroits dans le carré
u[N//4,N//4] = amplitude
u[N//4,3*N//4] = amplitude
u[3*N//4,N//4] = amplitude
u[3*N//4,3*N//4] = amplitude

# Boucle principale de la simulation
t = 0.0
while t < tmax:
    # Calcul de la vitesse
    v[1:-1,1:-1] += dt*(u[2:,1:-1] + u[:-2,1:-1] + u[1:-1,2:] + u[1:-1,:-2] - 4*u[1:-1,1:-1])/(dx*dx)

    # Calcul de la hauteur
    u += dt*v

    # Conditions aux limites
    u[0,:] = u[-1,:] = u[:,0] = u[:,-1] = 0.0
    v[0,:] = v[-1,:] = v[:,0] = v[:,-1] = 0.0

    # Affichage de l'onde avec un contour blanc pour mettre en valeur l'onde
    plt.clf()
    plt.imshow(u, cmap='ocean', vmin=-amplitude, vmax=amplitude, extent=[0, L, 0, L])
    plt.colorbar()
    plt.contour(u, levels=[amplitude/2], colors=['white'], extent=[0, L, 0, L])
    plt.title(f"Temps t = {t:.2f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.pause(0.000001)

    # Mise à jour du temps
    t += dt

plt.show()
