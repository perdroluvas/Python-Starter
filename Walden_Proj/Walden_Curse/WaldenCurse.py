import curses
import random
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time 
if __name__ == "__main__":
    

    def main(screen):
        
        #screen.timeout(1000)
        #screen function calls
        num_rows, num_cols = screen.getmaxyx()
        min_x = 1
        min_y = 1
        max_x = num_cols-2
        max_y = num_rows-2
        screen.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        screen.border(0)
        screen.timeout(0)
        screen.addstr(0, 2, "".join(["Screen size: ", str(num_rows), " x ", str(num_cols)]))

        class







wrapper(main)
