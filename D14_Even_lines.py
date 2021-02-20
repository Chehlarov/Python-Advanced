symbols = {"-", ",", ".", "!", "?"}
num = 0
with open("text.txt") as file:
    for line in file:
        if num % 2 == 0:
            for symbol in symbols:
                line = line.replace(symbol, "@")
            line_list = line[:-1].split(" ")
            line_list = list(reversed(line_list))
            print(" ".join(line_list))
        num += 1
