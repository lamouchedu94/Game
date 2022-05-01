
def verif_carte(liste_position_carte,position ) : 
    if position[0]>int(liste_position_carte[0][1]) and position[1]<int(liste_position_carte[0][2]):
        return False 
    return True