class Unit:
    def __init__(self, name, position, hp, attack, defense, speed) -> None:
        self.name = name
        self.position = position
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def has_moved(self) -> bool:
        return False

    def has_acted(self) -> bool:
        return False

# class to represent any unit on the field, human or otherwise, player or enemy
# there are two keywords to keep in mind: Acted and Moved. 
# Moved only cares about if the unit has been moved from its starting position at the top of the turn 
# Acted can be any other action taken on a turn: Attacking, Waiting, and (later versions) Use item, Talk
#   def  attack(enemy) :
      # Load the combat scene [[some kind of call from screen]]
      # Decide whether the attack hits
      # Calculate outgoing damage 
      # enemy.deal_damage(outgoing)
      # check if the enemy is dead, if not, enemy responds
      # calculate incoming damage
      # self.hp -= incoming
      # check if this unit is dead
      # set flag to show unit has acted for this turn

#   def move(destination) :
       # Get the unit's current position
       # Calculate the distance between the current position and the destination
       # Verify distance <= movement_range (currently will be = speed but potentially will be a calculation based on speed to scale more effectively at higher levels)
       # if true, set this.position=destination
       # call screen to animate unit movement 
       # set flag to show unit has moved for this turn

#   def wait() :
       # set flag to show unit has acted for this turn
       # set flag to show unit has moved for this turn if it is not already set
       # we set both flags just in case so the unit cannot move after performing the action.
       # we don't do that after attacking because I want units to be able to move after attacking if they have not already
       # waiting assumes the intention is that the unit will not need to do anything further for the turn
       
