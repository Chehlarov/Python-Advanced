names = input().split(', ')
heroes = {}

while True:
    data = input()
    if data == "End":
        break
    name, item, price = data.split('-')
    if not heroes.get(name):
        heroes[name] = {}
    if not heroes[name].get(item):
        heroes[name].update({item: int(price)})

print(*[f"{name} -> Items: {len(inventory)}, Cost: {sum([price for item, price in inventory.items()])}" for name, inventory in heroes.items()], sep="\n")