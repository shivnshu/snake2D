#!/usr/bin/env python

import curses
from curses import wrapper

def print_score(stdscr, current_score, scr_height, scr_width):
    """Print the updated score to screen."""
    stdscr.addstr(scr_height - 2, scr_width / 2 - 4, "Score: " + str(current_score))

def start(stdscr):
    """Function to initialise box drawing."""
    current_score = 0
    total_height, total_width = stdscr.getmaxyx()
    start_x = 30
    end_x = total_width - start_x
    start_y = 12
    end_y = total_height - 3
    snake_box = curses.newwin(end_y - start_y, end_x - start_x, start_y, start_x)
    snake_box.border()
    while True:
        print_score(stdscr, current_score, total_height, total_width)
        snake_box.refresh()
        stdscr.refresh()

def main(stdscr):
    """Main Function."""
    stdscr.clear()

    stdscr.addstr("Welcome to snake2D!\n\n")
    stdscr.addstr("Rules:\n")
    stdscr.addstr("1. Snake must not collide with walls.\n")
    stdscr.addstr("2: Snake must not collide with itself.\n\n")
    stdscr.addstr("Use following keys to control the snake whenever applicable.\n")
    stdscr.addstr("h: left\t\tj: below\tk :upper\tl: right\n\n")
    stdscr.addstr("Press Return to start..\n")

    curses.curs_set(False)
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        return_pressed = key == curses.KEY_ENTER or key == 10 or key == 13
        # stdscr.addstr(str(return_pressed))
        if return_pressed:
            start(stdscr)
            # break

    # stdscr.refresh()
    # stdscr.getch()

if __name__ == "__main__":
    wrapper(main)
