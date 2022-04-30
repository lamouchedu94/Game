def verif_obstacle(carte, position):
    if carte[position[0]*-1][position[1]] == "#" :
        return True
    return False
def vertif_bonus(carte,position) :
    if carte[position[0]*-1][position[1]] == "0" :
        carte[position[0]*-1][position[1]] = "."
        return True