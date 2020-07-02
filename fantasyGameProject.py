inv = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}
newList = ['gold coin','tent','dagger','tent','soap']

def displayInventory(dictObject):
    print('')
    print('Inventory:')
    total = 0
    for k, v in dictObject.items():
        print(str(v) + ' ' + k)
        total = total + v
    print('Total number of items: ' + str(total))

def addToInventory(inventory, addedItems):
    for x in addedItems:
        inventory.setdefault(x, 0)
        inventory[x] = inventory[x] + 1

displayInventory(inv)
addToInventory(inv,newList)
displayInventory(inv)