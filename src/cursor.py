class Cursor:
    def __init__(self, position, target) -> None:
        self.position = position
        self.target = target

    def is_player(self) -> bool:
        return False

    def is_enemy(self) -> bool:
        return False
