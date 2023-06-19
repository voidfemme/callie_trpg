import curses
from src.cursor import Cursor
from src.unit import Unit
from src.square import Square


class Game:
    def __init__(self, stdscr) -> None:
        self.stdscr = stdscr
        self.cursor = Cursor((0, 0), None)
        self.units = [Unit("Player", (5, 5), 10, 5, 2, 3)]
        self.squares = [[Square("grass") for _ in range(20)] for _ in range(20)]

    def draw(self):
        self.stdscr.clear()
        for y, row in enumerate(self.squares):
            for x, square in enumerate(row):
                char = "*" if any(unit.position == (x, y) for unit in self.units) else "."
                self.stdscr.addch(y, x, char)
        self.stdscr.move(*self.cursor.position)
        self.stdscr.refresh()

    def handle_input(self, key):
        if key == curses.KEY_UP and self.cursor.position[1] > 0:
            self.cursor.position = (self.cursor.position[0], self.cursor.position[1] - 1)
        elif key == curses.KEY_DOWN and self.cursor.position[1] < len(self.squares) - 1:
            self.cursor.position = (self.cursor.position[0], self.cursor.position[1] + 1)
        elif key == curses.KEY_LEFT and self.cursor.position[0] > 0:
            self.cursor.position = (self.cursor.position[0] - 1, self.cursor.position[1])
        elif key == curses.KEY_RIGHT and self.cursor.position[0] < len(self.squares[0]) - 1:
            self.cursor.position = (self.cursor.position[0] + 1, self.cursor.position[1])
        elif key == ord("q"):
            return False

