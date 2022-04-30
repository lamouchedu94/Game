import sys
from generation import carte_finale
from affichage import afficher

carte = carte_finale(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))

while True :
    touche = afficher(carte)
    if touche == "q" :
        break
    

