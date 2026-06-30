class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def pick_item(self, item):
        self.inventory.append(item)

    def __str__(self):
        inventory = ", ".join(str(item) for item in self.inventory)
        return f"{self.name} | Health: {self.health} | Inventory: {inventory}"

class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} : {self.description}"

class Room:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        return self.name

player = Player("Hammad")
room = Room("Bedroom")
key = Items("Key", "Opens the door")

room.items.append(key)
player.pick_item(key)
player.take_damage(20)

print("Player Information")
print(player)
print("\nRoom Name:")
print(room)
print("\nRoom Items:")
for item in room.items:
    print(item)

print("\nPlayer Inventory:")
for item in player.inventory:
    print(item)