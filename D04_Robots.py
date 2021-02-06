from collections import deque
from datetime import datetime, timedelta

data = input().split(";")

time = datetime.strptime(input(), '%H:%M:%S')

robots = []
# available_products = deque()
products = deque()

for el in data:
    robot_data = el.split("-")
    robot = {}
    robot['name'] = robot_data[0]
    robot['processing_time'] = int(robot_data[1])
    robot['available_at'] = time
    robots.append(robot)
    # available_products.append(robot)

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

time = time + timedelta(seconds=1)
while len(products) > 0:
    p = None
    for r in robots:
        if r['available_at'] <= time:
            p = products.popleft()
            print(f"{r['name']} - {p} [{time.strftime('%H:%M:%S')}]")
            r['available_at'] = time + timedelta(seconds=r['processing_time'])
            break
    time = time + timedelta(seconds=1)
    if p is None:
        products.rotate(-1)
