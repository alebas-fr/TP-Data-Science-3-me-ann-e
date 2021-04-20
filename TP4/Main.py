import numpy as np 
import matplotlib.pyplot as plt

tab_donne = np.genfromtxt("beeradvocate5.csv",delimiter=",")

apparence = tab_donne[:,0]
arome = tab_donne[:,1]
palate = tab_donne[:,2]
gout = tab_donne[:,3]
globale = tab_donne[:,4]
echelle = np.arange(1,6)

fig = plt.figure()
fig.add_subplot(2,1,1)
plt.hist([apparence,arome,palate,gout],bins=echelle,color = ['red','blue','green','lightgreen'],label = ['Appearance','Aroma','Palate','Taste'])
plt.xlabel('Score')
plt.ylabel('Number of ratings')
plt.legend(loc="upper left")

fig.add_subplot(2,1,2)
plt.xlabel('Aroma Score')
plt.ylabel('Taste Score')

courbe_verte = tab_donne[tab_donne[:,4]>4]
apparencev = courbe_verte[:,0]
aromev = courbe_verte[:,1]
palatev = courbe_verte[:,2]
goutv = courbe_verte[:,3]
globalev = courbe_verte[:,4]
courbe_rouge = tab_donne[tab_donne[:,4]<=4]
apparencer = courbe_rouge[:,0]
aromer = courbe_rouge[:,1]
palater = courbe_rouge[:,2]
goutr = courbe_rouge[:,3]
globaler = courbe_rouge[:,4]

plt.plot(aromev,goutv,'og',label = "Overall > 4")
plt.plot(aromer,goutr,"+r",label = "Overall <= 4")
plt.plot(echelle,echelle,":k")


plt.legend(loc="lower right")

plt.show()
