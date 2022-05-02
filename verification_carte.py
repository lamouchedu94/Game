def verif_colone(position,nb_colone,test) : 
    
    if position[1]/nb_colone-int(position[1]/nb_colone) == 0 and position[1]!=0:
        print(f'nb colone {test}')
        return True
    return False

def verif_ligne(position,nb_ligne,test) :
    if position[0]*-1/nb_ligne-int(position[0]*-1/nb_ligne) == 0 and position[0]!=0:
        print(f'nb ligne {test}')
        return True
    return False