import sys
from generation import carte_finale
from affichage import afficher
from deplacement import mouvement
from verificationdeplacement import verif_obstacle,vertif_bonus

carte = carte_finale(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
#carte = carte_finale(10,20,10,5)
position = [0,0]
point = 0
while True :
    touche = afficher(carte,position,point)
    if touche == "q" :
        break
    position = mouvement(touche,position)
    if verif_obstacle(carte,position) :
        break
    if vertif_bonus(carte,position) :
        point += 1
    if point == int(sys.argv[4]) :
        
        break
    

