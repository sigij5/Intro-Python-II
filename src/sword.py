from item import Item

class Sword(Item):
    def __init__(self, name, description, durability):
        super().__init__(name, description)
        self.durability = durability

    def __str__(self):
        return f"{super().__str__()}, with {self.durability} durability"