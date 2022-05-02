import curses
from curses import wrapper

def afficher(carte,position,point,test_ligne,test_colone) :
    #Affiche la carte et attend une entrée pour la renvoyer
    def main(stdscr):
        ligne = 0
        colone = 0
        stdscr.clear()
        curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
        curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_BLACK)
        curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)

        stdscr.clear()
        for i in range(len(carte)):
            for j in range(len(carte[0])) :
                if carte[i][j] == "#" :
                    stdscr.addstr(carte[i][j],curses.color_pair(1))
                
                elif carte[i][j] == "0" :
                    stdscr.addstr(carte[i][j],curses.color_pair(3))
                
                else :
                    stdscr.addstr(carte[i][j],curses.color_pair(2))        
            stdscr.addstr("\n")
            stdscr.refresh()
        #print(position[0]*-1-len(carte)*test_ligne,position[1]-len(carte[0])*test_colone)
        #stdscr.refresh()
        #stdscr.getkey()
        if position[0]*-1-len(carte)*test_ligne < 0 :
            ligne = (position[0]*-1-len(carte)*test_ligne)*-1
        else :
            ligne = position[0]*-1-len(carte)*test_ligne
        
        if position[1]-len(carte[0])*test_colone < 0 :
            colone = (position[1]-len(carte[0])*test_colone)*-1
        else :
            colone = position[1]-len(carte[0])*test_colone
        
        stdscr.addstr(2,len(carte[0]),f"{ligne},{colone},{test_ligne},{test_colone}")

        stdscr.addstr(ligne,colone,"$")
        stdscr.addstr(0,len(carte[0]),str(position))
        stdscr.addstr(1,len(carte[0]),f'Vous avez : {str(point)} point(s)')
        stdscr.refresh()
        
        return stdscr.getkey() 
    return(wrapper(main)) 