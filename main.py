from copy import deepcopy
import sys
from generation import carte_finale
from affichage import afficher
from deplacement import mouvement
from verificationdeplacement import verif_obstacle,vertif_bonus
from verification_carte import verif_colone,verif_ligne

#nb_ligne,nb_colone,nb_obstacle,nb_bonus = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])

#carte = carte_finale(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
nb_ligne,nb_colone,nb_obstacle,nb_bonus = 10,10,0,5
carte = carte_finale(10,10,0,5)
monde = []
monde.append(deepcopy(carte))


position = [0,0]
point = 0
num_carte = 0 
position_carte = {(0,len(carte)*-1,len(carte[0])):1}
#(0,-10,10)
position_carte = {(((0,len(carte)*-1)),(0,len(carte[0]))):1}
#((0,-10),(0,10))
#print(position_carte)

test_colone= 0
test_ligne = 0

while True :
    liste_position_carte = list(position_carte.keys())
    touche = afficher(carte,position,point,test_ligne,test_colone)
    if touche == "q" :
        break
    position = mouvement(touche,position)
    if verif_colone(position,nb_colone,test_colone) :
        test_colone+=1
        carte = carte_finale(nb_ligne,nb_colone,nb_obstacle,nb_bonus)
    if verif_ligne(position,nb_ligne,test_ligne) :
        test_ligne+= 1
        carte = carte_finale(nb_ligne,nb_colone,nb_obstacle,nb_bonus)
    #if verif_obstacle(carte,position) :
    #    break
    #if vertif_bonus(carte,position) :
    #    point += 1
    if point == 5 :#int(sys.argv[4]) :
        break
    
    

