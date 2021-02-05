from collections import deque

existing_food = int(input())
line = map(int, input().split())
customers = deque(line)
print(max(customers))

is_complete = True
while len(customers) > 0:
    order = customers[0]
    if order <= existing_food and is_complete:
        existing_food -= order
        customers.popleft()
    else:
        print(f"Orders left: {order}", end=" ")
        customers.popleft()
        is_complete = False

if is_complete:
    print("Orders complete")
