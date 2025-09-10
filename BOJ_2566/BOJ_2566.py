arr = [list(map(int, input().split())) for _ in range(9)]

max_value = max(map(max, arr))


positions = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == max_value]


i, j = positions[0]

print(max_value)
print(i + 1, j + 1)  