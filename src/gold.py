from item import Item

class Gold(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def __str__(self):
        return f"{super().__str__()}, with value {self.value}"