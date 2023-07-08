# player
#   move
#   attack
#   wait
# enemy
#   inspect
# System
#   Units
#   Save
#   Load
#   Restart
#   Quit
class Menu:
    def __init__(self, player, enemy, cursor) -> None:
        pass

    # def display_player_menu(unit):
        # Call the screen class to display the menu for unit actions
        # Wait for user input
        # if the user presses back, close the most recent menu
        # switch : selection
        # case (selection is move) :
            # provide user cursor to select destination
            # prevent cursor from moving past unit's movement range
            # when user presses confirm button, use cursor's coordinate in the call
            # this.unit.move(destination)
            # close the menu
        # case (selection is attack) :
            # provide user cursor to select target
            # call screen to display pre-combat prediction 
            # once user confirms, initiate combat
            # this.unit.attack(target)
            # close the menu
        # case (selection is wait) :
            # check if the unit has moved
            # if not, provide user with a confirmation window 
            # this.unit.wait()
            # close the menu

    # def display_enemy_menu(enemy)
        # Call the screen class to display enemy menu
        # TBD: add other kinds of interactions for this menu
        # switch: selection
        # case (selection is inspect)
            # call screen to display the unit's status screen
            # if user presses back, close status screen 
            # close the menu


