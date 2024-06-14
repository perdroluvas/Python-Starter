import curses
from curses import wrapper
import time
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    BANDY = curses.color_pair(1)
    GANDB = curses.color_pair(2)
    stdscr.nodelay(True)
    #key = stdscr.getkey()
    #stdscr.addstr(f"key: {key}")
    #stdscr.refresh()
    #stdscr.getch()
    x , y = 0, 0
    string_x = 0
    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_UP":
            y -= 1
        elif key == "KEY_DOWN":
            y += 1
        stdscr.clear()
        #string_x += 1
        #stdscr.addstr(0, string_x//50, "eaeeeeee")
        stdscr.addstr(y,x,"0")
        stdscr.refresh()




wrapper(main)    
