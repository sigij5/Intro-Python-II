from room import Room
from player import Player
import textwrap
from item import Item
from rope import Rope
from sword import Sword
from gold import Gold

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

# item = {
#     'rope': Rope("Rope", "a long rope, useful for any traveler", 100),
#     'sword': Sword("Sword", "a rusty old sword", 20),
#     'gold': Gold("Gold", 'shiny money', 100),
# }


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms
room['foyer'].inventory = [Rope("Rope", "a long rope, useful for any traveler", 100)]

# room['foyer'].inventory.append(Rope("Rope", "a long rope, useful for any traveler", 100))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Player", room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
selection = ""

while selection != "q":
    directions = {
    "n": player.current_room.n_to,
    "s": player.current_room.s_to,
    "e": player.current_room.e_to,
    "w": player.current_room.w_to
    }

    print(f"\nCurrent Location: {player.current_room.name}")
    print(textwrap.fill(player.current_room.description, width=70))

    if (len(player.current_room.inventory) > 0):
        print(f"Items in room: ")
        player.current_room.print_items()

    selection = input("\nPlease select an action or direction. ")
    # next_room = room[player.current_room].[selection]

    if len(selection.split()) > 1:
        item_name = selection.split()[1].lower()
        if selection.split()[0] == 'take':
            player.take(item_name)
        elif selection.split()[0] == 'drop':
            player.drop(item_name)
    
    else:
        try:
            if selection != "q":
                if selection in directions:
                    next_room = directions[selection]
                    if next_room != "":
                        print(f"You've moved to {next_room.name}")
                        player.current_room = next_room
                    else:
                        print("There is no room in that direction.")
                elif selection == "i":
                    player.open_inventory()
                else:
                    print("You can't do that... sorry!")
        
        except ValueError:
            print("Please enter a direction.")