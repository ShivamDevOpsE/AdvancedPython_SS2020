# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:54:40 2020

@author: Shivam
"""


# Exercise 12.2
# "Conway´s game of life" is a two-dimensional generzalization of the cellular 
# automata and it is equivalent to a universal Turing Machine.
# Implement the evolution rule on a two-dimensional grid of size 300x300 with
# periodic boundary conditions using numpy.
# Use random initial state for 200 steps.


import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

def update(Num, img, new, N):
    new_life = new.copy()
    
    for i in range(N):
        for j in range(N):
            total = (new[(i-1) % N][(j-1) % N] + new[(i-1) % N][j] + 
                         new[(i-1) % N][(j+1) % N] + new[i][(j-1) % N] + new[i][(j+1) % N] +
                         new[(i+1) % N][(j-1) % N] + new[(i+1) % N][j] +
                         new[(i+1) % N][(j+1) % N])/255
                         
            if new[i][j] == 255:
                if total > 3 or total < 2:
                    new_life[i][j] = 0
                    
                elif total == 3:
                    new_life[i][j] = 255
                    
                    
    img.set_data(new_life)
    new[:] = new_life[:]
    return img

N = 50
Speed = 100
Prob_life = 40

new = np.random.choice([255, 0], N*N, p = [1-((Prob_life)/100), (Prob_life)/100]).reshape(N, N)

fig, ax = plt.subplots()
img = ax.imshow(new, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs = ( img, new, N),
                               frames = 10, interval = Speed,
                               save_count = 50)


plt.show()
            
            