class Cursor:
    def __init__(self, position, target) -> None:
        self.position = position
        self.target = target

    def is_player(self) -> bool:
        return False

    def is_enemy(self) -> bool:
        return False
#[Cursor] for moving around the screen, selecting units/tiles. Main controlable element during gameplay. 
#Cursor should move along the grid by default, able to be sped up/freed from the grid by holding down a button 
#If the cursor is over a unit, display that unit's stats on the frame
#If the cursor is over terrain, display any effects on the frame 
#When the player presses the "confirm" button, the cursor's target should be checked
#If the target is an empty tile or a player unit which has already moved, open the "Empty" menu from the [Menu] class (An empty tile is one which has no Units on it)
#If the target is a player unit which has not already moved, open the "Player" menu
#If the target is an enemy unit, open the "Enemy" menu