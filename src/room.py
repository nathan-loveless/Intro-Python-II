# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'{self.name} {self.description}'

    def getItems(self, where):
        value=f'{where} contains the following items:\n'
        for item in self.items:
            value += f'{item.name}: {item.description}\n'
        value += '\n'
        return value

    def getItem(self, item):
        for obj in self.items:
            if(obj.name.lower() == item):                
                return obj
            else:
                return None

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        for obj in self.items:
            if(obj.name.lower() == item):
                self.items.remove(obj)

    def hasItems(self):
        if(len(self.items) == 0):
            return False
        return True
