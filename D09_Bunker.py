bunker = {cat: [] for cat in input().split(", ")}
bunker['all_items_count'] = 0
bunker['all_quality'] = 0
n = int(input())

for _ in range(n):
    cat, item_name, item_params = input().split(' - ')
    item_quantity = int(item_params.split(';')[0].split(':')[1])
    item_quality = int(item_params.split(';')[1].split(':')[1])
    item_data = {item_name: {'quantity': item_quantity, 'quality': item_quality}}
    bunker[cat].append(item_data)
    bunker['all_items_count'] += item_quantity
    bunker['all_quality'] += item_quality


print(f"Count of items: {bunker['all_items_count']}")
print(f"Average quality: {bunker['all_quality']/(len(bunker)-2):.2f}")
# very bad, just training comprehension extremes
print(*[f"{cat} -> {', '.join([list(d.keys())[0] for d in value])}" for cat, value in bunker.items() if isinstance(bunker[cat], list)], sep='\n')