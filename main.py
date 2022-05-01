from copy import deepcopy
import sys
from generation import carte_finale
from affichage import afficher
from deplacement import mouvement
from verificationdeplacement import verif_obstacle,vertif_bonus
from verification_carte import verif_carte

carte = carte_finale(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
#carte = carte_finale(10,20,10,5)
monde = []
monde.append(deepcopy(carte))


position = [0,0]
point = 0
num_carte = 0 
position_carte = {(0,len(carte)*-1,len(carte[0])):1}
#print(position_carte)
liste_position_carte = list(position_carte.keys())



while True :
    carte = monde[num_carte]
    touche = afficher(carte,position,point)
    if touche == "q" :
        break
    position = mouvement(touche,position)
    if verif_carte(liste_position_carte,position) :
        break
    if verif_obstacle(carte,position) :
        break
    if vertif_bonus(carte,position) :
        point += 1
    if point == 5 :#int(sys.argv[4]) :
        break
    
    

