from room import Room
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Skull", "This is a skull, it looks kind of ominous")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("coins", "This is a pile of gold that contains 33 gold coins"), Item("Sword", "Sword + 1")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Body", "This is a dead body, it offers no value to you"), Item("Ring", "Ring of Damage + 1")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Chest", "This chest is empty, the treasure is gone")]),
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
from player import Player

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

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
selection = ''



while(selection != 'q'):
    print(player)
    # print(player.currentRoom.getItems())
    selection = input("please select a direction, item to pick up/drop or 'q' to quit: ")
    itemParser = selection.split(" ")
    if(itemParser[0].lower() == "get"):
        player.takeItem(itemParser[1])
    elif(itemParser[0].lower() == "drop"):
        player.dropItem(itemParser[1])
    elif(selection.lower() == "i" or selection.lower() == "inventory"):
        player.setInventoryFlag()
    else:
        player.set_current_room(selection)

print('You have exited the game, thank you for playing!')




