stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for item, amount in inventory.items():
        print(str(amount) + ' ' + item)
        total = total + amount
    print('\nTotal number of items: ' + str(total))

def addToInventory(dictionary, addedItemsList):
    for i in range(len(addedItemsList)):
        dictionary.setdefault(addedItemsList[i], 0)
        dictionary[addedItemsList[i]] += 1
    return dictionary

displayInventory(stuff)
print('\n' + str(len(dragonLoot)) + ' more items to be added:\n' + str(dragonLoot))
stuff = addToInventory(stuff, dragonLoot)
print('\n(New)')
displayInventory(stuff)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print('\n(Other)')
displayInventory(inv)

