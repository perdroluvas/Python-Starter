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
    curses.echo() 
    stdscr.attron(GANDB)
    stdscr.border(GANDB)
    stdscr.attroff(GANDB)

    stdscr.move(10,20)       

    stdscr.attron(GANDB)
    rectangle(stdscr,10,10,20,20)
    stdscr.addstr(5,30,"Hello world!")
    stdscr.attroff(GANDB)
    stdscr.refresh()
    while True:
        key = stdscr.getkey()
        if key == "q":
            break

    stdscr.getch()




wrapper(main)
