import numpy as np 

tab_donne = np.genfromtxt("beeradvocate5.csv",delimiter=",")
#print("Le tableau de donnée original est ")
#print(tab_donne)
#print("La taille de ce tableau est")
print(tab_donne.shape)
print("Question 1 :")
print()
tab_note20 = 4*tab_donne
print(tab_note20,)


print()
print("Question 2 :")
print()
print("Question a :")
print()
nombre_bierre = tab_note20.shape[0] # Question 2) a)
print("Le nombre de bierre dans le tableau est ",nombre_bierre) 


apparence = tab_note20[:,0]
arome = tab_note20[:,1]
palate = tab_note20[:,2]
gout = tab_note20[:,3]
globale = tab_note20[:,4]
print()
print("Question b :")
print()
moyenne_tab = np.array([apparence.mean(),arome.mean(),palate.mean(),gout.mean(),globale.mean()]) #Question 2) b) faire un tableau avec toute les moyennes
print(moyenne_tab)


print()
print("Question c :")
print()

note_max_apparence = apparence.max()
print("La note max pour le critère apparence est ",note_max_apparence)

print()
print("Question d :")
print()
print("La moyenne du critère arome pour les 500 premières lignes est ",arome[0:500].mean(),arome[0:500].shape)

print()
print()
print("Question e :")
print("La moyenne du critère arome pour les 500 dernières lignes est ",arome[-500:].mean(),arome[-500:].shape)


print()
print("Question f :")
print()
print("La medianne pour le critére aroma des indices pair est ", np.median(arome[0:arome.size:2]))

print()
print("Question g :")
print()
print("L'indice de la meilleur obtenue au globale est ",np.where(globale==(globale.max())))

print()
print("Question h :")
print()
Variance_tab=np.array([np.var(apparence),np.var(arome),np.var(palate),np.var(gout),np.var(globale)])
print(Variance_tab)

print()
print("Question i :")
print()
print("Nombre de note supérieur à 15 ",tab_note20[tab_note20>15].size)

print()
print("Question j :")
print()
print("Nombre de note supérieur à 15 dans arôme ",arome[arome>15].size)

print()
print("Question k :")
print()
print("Nombre de note supérieur à la moyenne dans arôme ",arome[arome>arome.mean()].size)

print()
print("Question l :")
print()
print("Nombre de note supérieur à la mediane dans palate ",palate[palate>np.median(palate)].size)

print()
print("Question m :")
print()

compteur_note=0
tableau_verif = None
verif = True
i=0
j=0
while i<tab_note20.shape[0]:
	tableau_verif = tab_note20[i]>15
	verif=True
	#print(tableau_verif) # sert au debug mode
	while j<tableau_verif.size and verif:
		if tableau_verif[j]==False:
			verif=False
		j+=1
		if j==tableau_verif.size and verif:
			compteur_note+=1
	j=0
	i+=1

print("Nombre de bierre ayant obtenue plus de 15 dans toutes les categories",compteur_note)

print()
print("Question n :")
print()
tableau_gout15 = tab_note20[tab_note20[:,3]>15]
print("La note globale moyenne des bieres ayant une note superieure a 15 dans le critere gout est",tableau_gout15[:,4].mean())

print()
print("Question o :")
print()

tableau_moyenne5 = np.arange(tab_note20.shape[0])
tableau_moyenne5 = (1/5)*(apparence+arome+palate+gout+globale)
print(tableau_moyenne5)
tableau_moyenne5_sans_max = tableau_moyenne5[tableau_moyenne5<tableau_moyenne5.max()]
print("L'indice de la bière ayant obtenu la seconde meilleur note en moyenne sur les 5 critères est ",np.where(tableau_moyenne5==tableau_moyenne5_sans_max.max()))

print()
print("Question p :")
print()
tab_mote20_moyenne = np.insert(tab_note20,tab_note20.shape[1],tableau_moyenne5,axis=1) # Permet d'avoir le tableau avec les 5 notes mais aussi la moyennes de ses 5 notes dans la même ligne
tab_note20_moyenne_sup15 = tab_mote20_moyenne[tab_mote20_moyenne[:,5]>15]
note_min_gout = tab_note20_moyenne_sup15[:,3].min()
print("L'indice de la bière ayant obtenu la moins bonne note en gout parmi les bières ayant une moyenne supérieur à 15 est",np.where(tab_note20[:,3]==note_min_gout))

print()
print("Question q :")
print()
tab_noteo_sup_med = tab_note20[tab_note20[:,4]>=np.median(tab_note20[:,4])]
print("La moyenne du critére arôme parmi les bières ayant obtenu une note globale supérieur à la mediane est ",tab_noteo_sup_med[:,1].mean())

print()
print("Question r :")
print()
apparence6 = 6*apparence
palate05 = 0.5*palate
gout0 = 0*gout
globale2 = 2*globale
print(apparence6.shape)
print(palate05.shape)
print(gout0.shape)
print(globale2.shape)
moyenne_globale = (1/9.5)*(apparence6+arome+palate05+globale2)
print("La note de la meilleure bière selon le classement est ",moyenne_globale.max())
print("Son indice est ",np.where(moyenne_globale==moyenne_globale.max()))

print()
print("Question s :")
print()
matrice_covariance = np.cov(tab_note20,bias='True')
print(matrice_covariance,matrice_covariance.shape)

print()
print("Question 3 :")
print()

D,V = np.linalg.eig(matrice_covariance)
print(D.max())
print()


input()