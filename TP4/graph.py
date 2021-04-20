# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:00:09 2020

@author: Honorin
"""

import numpy as np
import matplotlib.pyplot as plt 
data = np.genfromtxt('beeradvocate5.csv',delimiter=',')
#Appearance Aroma Palate Taste Overall
Appearance = data[:,0]
Aroma = data[:,1]
Palate = data[:,2]
Taste = data[:,3]
Overall = data[:,4]
def taille(tab):
    return np.shape(tab)[0]

def score_entre(critere, i, j):
    return np.count_nonzero((critere >= i) & (critere<j))
def fig1():
    fig, ax = plt.subplots(figsize=(10,5))
    ax.set_xlabel('Score')
    ax.set_ylabel('Number of ratings')
    ax.xaxis.set_ticks(range(5))
    width = 0.2
    Score = np.arange(1, 5, 1)
    Nb_app = [score_entre(Appearance, 1, 2), score_entre(Appearance, 2, 3), score_entre(Appearance, 3, 4), score_entre(Appearance, 4, 5)]
    ax.bar(Score + width/2, Nb_app, width, label='Appearance', color = 'red')
    Nb_ar = [score_entre(Aroma, 1, 2), score_entre(Aroma, 2, 3), score_entre(Aroma, 3, 4), score_entre(Aroma, 4, 5)]
    ax.bar(Score + 3/2*width, Nb_ar, width, label='Aroma', color = 'blue')
    Nb_pal = [score_entre(Palate, 1, 2), score_entre(Palate, 2, 3), score_entre(Palate, 3, 4), score_entre(Palate, 4, 5)]
    ax.bar(Score + 5/2*width, Nb_pal, width, label='Palate', color = 'green')
    Nb_tas = [score_entre(Taste, 1, 2), score_entre(Taste, 2, 3), score_entre(Taste, 3, 4), score_entre(Taste, 4, 5)]
    ax.bar(Score + 7/2*width, Nb_tas, width, label='Taste', color =(0.749,0.749,0) )
    ax.legend(loc="upper left")
    plt.show()
    #ax.set_ylim([0,3000]) rend degueu le graph
def fig2():
    fig, ax = plt.subplots(figsize=(10,5))
    ax.set_xlabel('Aroma score')
    ax.set_ylabel('Taste score')
    
    x = np.arange(1, 5, 0.1)
    y = np.arange(1, 5, 0.1)
    A_s1 = data[np.where(Overall<=4),1]
    A_s2 = data[np.where(Overall>4),1]
    T_s1 = data[np.where(Overall<=4),3]
    T_s2 = data[np.where(Overall>4),3]
    ax.plot(A_s1, T_s1, "+r", label = 'Overall <= 4') 
    ax.plot(A_s2, T_s2, 'og', label = 'Overall > 4') 
    ax.plot(x, y, ":k")
    #ax.legend(loc= "lower rigt")
    ax.axis([1,5,1,5])
    plt.show()

fig1()
fig2()