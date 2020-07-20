# Write a class to hold player information, e.g. what room they are in
from item import Item
# currently.
class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.items = []
        self.hasDisplayedInventory = False

    def __str__(self):
        output = f'You are currently in:\n***{self.currentRoom.name}***\n\n{self.currentRoom.description}\n\n'
        if(hasattr(self.currentRoom, 'n_to')):
            output += f'N/n: Go North\n'
        if(hasattr(self.currentRoom, 'e_to')):
            output += f'E/e: Go East\n'
        if(hasattr(self.currentRoom, 's_to')):
            output += f'S/s: Go South\n'
        if(hasattr(self.currentRoom, 'w_to')):
            output += f'W/w: Go West\n'
        if(self.currentRoom.hasItems()):
            output += f'\n(take <item> ex. take coins) {self.currentRoom.getItems("Room")}'
        if(self.hasDisplayedInventory):
            output += self.getInventory()
            self.hasDisplayedInventory = False
        output += 'i: Get inventory\n'
        output += 'q: Quit game\n'
        return output
    
    def set_current_room(self, selection):
        if(str.lower(selection) == 'n' and hasattr(self.currentRoom, 'n_to')):
            self.currentRoom = self.currentRoom.n_to
        if(str.lower(selection) == 'e' and  hasattr(self.currentRoom, 'e_to')):
            self.currentRoom = self.currentRoom.e_to
        if(str.lower(selection) == 's' and  hasattr(self.currentRoom, 's_to')):
            self.currentRoom = self.currentRoom.s_to
        if(str.lower(selection) == 'w' and  hasattr(self.currentRoom, 'w_to')):
            self.currentRoom = self.currentRoom.w_to

    def takeItem(self, item):
        newItem = self.currentRoom.getItem(item)
        if(newItem != None):
            self.items.append(newItem)
        self.currentRoom.removeItem(item)
    
    def dropItem(self, item):
        for obj in self.items:
            if(obj.name.lower() == item):
                self.items.remove(obj)
                self.currentRoom.addItem(obj)
    
    def getInventory(self):
        output = ""
        if(len(self.items) == 0):
            return "You have no inventory\n\n"
        else:
            output = "\n(drop <item> ex. drop sword) Your current inventory:\n"
            for item in self.items:
                output += f'{item.name}: {item.description}\n'
            output += '\n'
            return output
    
    def setInventoryFlag(self):
        self.hasDisplayedInventory = True





        # return f'Your current room is:\n {self.currentRoom.name}\n{self.currentRoom.description}'
