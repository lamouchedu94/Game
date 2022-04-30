from random import randint

def creation_carte(nb_ligne, nb_colone) :
    #Création de la carte
    carte = []
    for i in range(nb_ligne) :
        carte.append(["."])
        for j in range(nb_colone-1) :
            carte[i].append(".")
    return carte

def obstacles(carte,nb_obstacle):
    # carte[[".",".",".","."][".",".",".","."][".",".",".","."]]
    #Generation de la position des obstacles
    obstacle = []
    for i in range(nb_obstacle) :
        co = randint(0,len(carte)-1),randint(0,len(carte[0])-1)
        obstacle.append(co)
    return obstacle

def modif_carte(carte,obstacle,bonus) :
    #Ajout des obstacles dans la cartes
    for car in obstacle :
        carte[car[0]][car[1]] = '#'
    for car in bonus :
        carte[car[0]][car[1]] = '0'

def carte_finale(nb_ligne, nb_colone,nb_obstacle,nb_bonus) :
    carte = creation_carte(nb_ligne,nb_colone)
    obstacle = obstacles(carte,nb_obstacle)
    bonus = obstacles(carte,nb_bonus)
    modif_carte(carte,obstacle,bonus)
    return carte
