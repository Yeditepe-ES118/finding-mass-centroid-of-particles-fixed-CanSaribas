# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np

def centroid(p1x, p1y, p2x, p2y, p3x, p3y, m1, m2, m3):
    positions = np.array([
        [p1x, p2x, p3x],
        [p1y, p2y, p3y]
    ])  # 2D array: shape (2,3)
    
    masses = np.array([m1, m2, m3])  # 1D array: shape (3,)
    
    tot_mass = np.sum(masses)
    
    cx = np.sum(positions[0, :] * masses) / tot_mass
    cy = np.sum(positions[1, :] * masses) / tot_mass
    
    # Plot points and center of mass
    plt.plot(positions[0, :], positions[1, :], "bo")
    plt.plot(cx, cy, "r+", markersize=12)
    plt.savefig("test.png")
    plt.close()
    
    return cx, cy, tot_mass

# Test
test = centroid(0, 0, 0, 1, 1, 0, 3, 4, 5)
print(test)


    