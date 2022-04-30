touche_possibles = touche_possible = [{"KEY_UP": 1 ,"KEY_DOWN": -1},{"KEY_LEFT": -1,"KEY_RIGHT" : 1}]

def mouvement(touche, position):
    position_avant = position
    try :
        if touche in touche_possible[0] :
            if position[0] + touche_possible[0][touche] < 0 :
                position[0] += touche_possible[0][touche] 
        else :
            if position[1] + touche_possible[1][touche] > 0 :
                position[1] += touche_possible[1][touche]
    except :
        pass
    return position
