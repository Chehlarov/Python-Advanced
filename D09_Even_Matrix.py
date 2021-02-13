def strs_to_ints(strs):
    return [int(x) for x in strs]


rows = int(input())
matrix = [strs_to_ints(input().split(", ")) for _ in range(rows)]

even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
print(even_matrix)
