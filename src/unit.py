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

