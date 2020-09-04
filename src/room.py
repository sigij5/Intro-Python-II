# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, n_to="", s_to="", e_to="", w_to="", inventory=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.inventory = inventory

    def print_items(self):
        for item in self.inventory:
            print(f"{item.name} - {item.description}")