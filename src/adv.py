from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Sigi", "outside")


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
    "n": room[player.current_room].n_to,
    "s": room[player.current_room].s_to,
    "e": room[player.current_room].e_to,
    "w": room[player.current_room].w_to
    }

    print(f"Current Location: {player.current_room}")
    print(textwrap.wrap(room[player.current_room].description))

    selection = input("Please select a direction to move. ")
    # next_room = room[player.current_room].[selection]

    try:
        next_room = directions[selection]
        if next_room != "":
            print(f"You've moved to {next_room.name}")
            if next_room.name.split()[0] == "Grand":
                player.current_room = next_room.name.split()[1].lower()
            else:
                player.current_room = next_room.name.split()[0].lower()
        else:
            print("There is no room in that direction.")

    except ValueError:
        print("Please enter a direction.")