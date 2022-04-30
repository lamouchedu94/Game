import sys
from generation import carte_finale
from affichage import afficher
from deplacement import mouvement

carte = carte_finale(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
#carte = carte_finale(10,20,10,5)
position = [0,0]

while True :
    touche = afficher(carte,position)
    if touche == "q" :
        break
    position = mouvement(touche,position)
    

