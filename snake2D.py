#!/usr/bin/env python3

import curses
# import random
import time
from curses import wrapper

def print_score(stdscr, current_score, scr_height, scr_width):
    """Print the updated score to screen."""
    stdscr.addstr(scr_height - 2, scr_width // 2 - 4, "Score: " + str(current_score))

def draw_snake(snake_box, snake_pixel):
    """Draw the snake on the box."""
    snake_box.border()
    for x, y in snake_pixel:
        snake_box.addstr(y, x, "*")

def walk_snake(snake_pixels, snake_dir):
    """Updae snake_pixels as to walk in snake direction."""
    head = snake_pixels[-1]
    new_head = (head[0] + snake_dir[0], head[1] + snake_dir[1])
    snake_pixels.append(new_head)
    del snake_pixels[0]

def test_collision(snake_box, snake_pixels):
    """Function to detect box or snake collision."""
    height, width = snake_box.getmaxyx()
    # If collision with wall, only head would collide.
    head = snake_pixels[-1]
    if (head[0] <= 0 or head[0] >= width):
        return True
    if (head[1] <= 0 or head[1] >= height):
        return True
    return len(snake_pixels) != len(set(snake_pixels))

def start(stdscr):
    """Function to initialise box drawing."""
    current_score = 0
    snake_pixels = [(1, 1), (2, 1), (3, 1)]
    snake_dir = (1, 0)
    total_height, total_width = stdscr.getmaxyx()
    start_x = total_width // 5
    end_x = total_width - start_x
    start_y = 12
    end_y = total_height - 3
    snake_box = curses.newwin(end_y - start_y, end_x - start_x, start_y, start_x)
    snake_box.border()
    stdscr.nodelay(True)
    while True:
        draw_snake(snake_box, snake_pixels)
        print_score(stdscr, current_score, total_height, total_width)
        snake_box.refresh()
        snake_box.clear()
        stdscr.refresh()
        walk_snake(snake_pixels, snake_dir)
        if test_collision(snake_box, snake_pixels):
            break
        c = stdscr.getch()
        if c == ord("j"):
            snake_dir = (0, 1)
        elif c == ord("k"):
            snake_dir = (0, -1)
        elif c == ord("h"):
            snake_dir = (-1, 0)
        elif c == ord("l"):
            snake_dir = (1, 0)
        time.sleep(0.1)

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
        # stdscr.nodelay(False)
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
