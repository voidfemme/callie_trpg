class Square:
    def __init__(self, terrain):
        self.terrain = terrain

    def is_occupied(self) -> bool:
        return False

# I think this is going to mostly end up as a subclass to help make up a Map
# Squares will be used to make the grid based on pre-designed maps
#   def get_terrain(self):return self.terrain

