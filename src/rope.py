from item import Item

class Rope(Item):
    def __init__(self, name, description, length):
        super().__init__(name, description)
        self.length = length

    # def __str__(self):
    #     return f"{super().__str__()}, {self.length} long"