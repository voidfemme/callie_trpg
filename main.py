#!/usr/bin/env python3
import curses
from src.game import Game


def main(stdscr):
    # Initialization code here
    # Create Screen, Menu, Cursor, Square, and Unit objects
    # Set up any curses settings needed, like color mode or setting the input mode
    curses.curs_set(0)
    stdscr.keypad(True)

    game = Game(stdscr)

    while True:
        # Game loop code here
        # Draw current state of game to the Screen
        # waiting for user input
        # updating the game state based on that input
        game.draw()
        key = stdscr.getch()

        # Input handling code here
        #   something like getch (the simplest) which waits for the user to press a key
        #   and returns the value of that key.
        #   move cursor around the screen, select units, open menus.

        game.handle_input(key)

        # Drawing
        #   clearing the screen
        #   drawing the map and units
        #   refreshing the screen to show the new state.

        # Updating the game state
        #   moving units
        #   attacking
        #   opening/closing menus
        #   invalid actions
        #   give feedback to user when they do something


if __name__ == "__main__":
    curses.wrapper(main)
