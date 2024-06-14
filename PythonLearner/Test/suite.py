import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time 

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BANDY = curses.color_pair(1)
    GANDB = curses.color_pair(2)
    OANDW = curses.color_pair(3)


    win = curses.newwin(3,18,2,2)
    box = Textbox(win)
    rectangle(stdscr, 1,1,5,20)
    stdscr.refresh()

    box.edit()
    text = box.gather().strip().replace("\n", "")

    stdscr.addstr(10,40, text)

    stdscr.getch()


wrapper(main)

    
