# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
from rope import Rope
from sword import Sword

class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
        self.gold = 0

    def take(self, item_name):
        item_found = False
        for item in self.current_room.inventory:
            if(item.name.lower() == item_name):
                self.inventory.append(item)
                self.current_room.inventory.remove(item)
                print(f"\nYou've picked up {item.name}!")
                item_found = True
        if (not item_found):
            print(f"{item_name} not found!")

    def drop(self, item_name):
        item_found = False
        for item in self.inventory:
            if(item.name.lower() == item_name):
                self.inventory.remove(item)
                self.current_room.inventory.append(item)
                print(f"\nYou've dropped {item.name}.")
                item_found = True
        if(not item_found):
            print(f"\nYou don't have any {item_name}")

    def open_inventory(self):
        print("Inventory: ")
        for item in self.inventory:
            item.__str__()


