import curses
from curses import wrapper
import time
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    BANDY = curses.color_pair(1)
    GANDB = curses.color_pair(2)
    (curses.LINES - 1, curses.COLS - 1)#importete
    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            pad.addstr(char, GANDB)
    
    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(0,0,5, i,10,25+i)
        time.sleep(0.2)

    pad.refresh(5, 5, 5, 5, 25, 25)
    stdscr.getch()


wrapper(main)
