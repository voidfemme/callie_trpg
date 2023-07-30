class Cursor:
    def __init__(self, position, target) -> None:
        self.position = position  # Where the cursor is on the grid
        self.target = target  # What the cursor is looking at

    # Check to see if the target is a player unit
    def is_player(self) -> bool:
        return False

    # Check to see if the target is a player unit
    def is_enemy(self) -> bool:
        return False


# represents the cursor which the player will use to navigate the map, select squares, and open menus
# cursor should be moved stepwise along the grid, and provide its target information to the frame for display
# def check(position):
# not sure if this should be several functions or one but I'm going with the idea of brevity in mind so i'm thinking of it as one function
# get the type of the square at position
# display the square type and any effects in the frame
# check if the square is occupied
# if (square.occupied):
# display the properties of the occupant to the frame
# else
# clear the unit preview window in the frame
