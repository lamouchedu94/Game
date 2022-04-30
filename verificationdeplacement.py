import curses,time
from curses import wrapper

def verif_obstacle(carte, position):
    if carte[position[0]*-1][position[1]] == "#" :
        def main(stdscr):
            curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
            curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_BLACK)
            for i in range(5) :
                stdscr.addstr(len(carte)//2,len(carte[1])//2,"Game Over", curses.color_pair(1) )
                stdscr.refresh()
                time.sleep(0.25)
                
                stdscr.addstr(len(carte)//2,len(carte[1])//2,"Game Over", curses.color_pair(1) | curses.A_REVERSE )
                
                stdscr.refresh()
                time.sleep(0.5)
        
        wrapper(main)

        return True
    return False

def vertif_bonus(carte,position) :
    if carte[position[0]*-1][position[1]] == "0" :
        carte[position[0]*-1][position[1]] = "."
        return True