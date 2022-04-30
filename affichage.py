import curses
from curses import wrapper

def afficher(carte,position) :
    #Affiche la carte et attend une entrée pour la renvoyer
    def main(stdscr):
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

        stdscr.addstr(position[0]*-1,position[1],"$")
        stdscr.addstr(0,len(carte[0]),str(position))
        stdscr.refresh()
        
        return stdscr.getkey() 
    return(wrapper(main)) 