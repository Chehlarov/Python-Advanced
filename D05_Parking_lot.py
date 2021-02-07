n = int(input())

result = set()
for _ in range(n):
    op, reg_num = input().split(", ")
    if op == "IN":
        result.add(reg_num)
    elif op == "OUT":
        result.remove(reg_num)

if result:
    for r in result:
        print(r)
else:
    print("Parking Lot is Empty")
