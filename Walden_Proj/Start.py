import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time 
from random import randint
from Gerador_Walden import vestimenta
'''from random import randint
from Gerador_Walden import fisico
from Gerador_Walden import rosto
from Gerador_Walden import pele
from Gerador_Walden import vestimenta
from Gerador_Walden import fala
from Gerador_Walden import vicio
from Gerador_Walden import cabelo
from Gerador_Walden import virtude
'''
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    BANDY = curses.color_pair(1)
    GANDB = curses.color_pair(2)
    (curses.LINES - 1, curses.COLS - 1)#importete
    pad = curses.newpad(100, 100)
    stdscr.refresh()

    #stdscr.addstr(vestimenta(randint(1,6)))

wrapper(main)
