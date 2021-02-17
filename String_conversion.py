nums = []
i = 0
while True:
    text = input()
    if text == "":
        break
    text = text.replace("× 10", "E")
    text = text.replace(" ", "")
    text = text.replace("–", "-")
    num = float(text)
    nums.append(f"+ {num} * T ^ {i} _")
    i += 1

print(*nums, sep="\n")

