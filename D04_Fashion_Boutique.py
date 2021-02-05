box = list(map(int, input().split()))
capacity = int(input())
counter_racks = 1
current_rack_capacity = capacity

while len(box) > 0:
    item = box.pop()
    if current_rack_capacity >= item:
        current_rack_capacity -= item
    else:
        counter_racks += 1
        current_rack_capacity = capacity
        current_rack_capacity -= item

print(counter_racks)
