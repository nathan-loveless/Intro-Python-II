# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom

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





        # return f'Your current room is:\n {self.currentRoom.name}\n{self.currentRoom.description}'
