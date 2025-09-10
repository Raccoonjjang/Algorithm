n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr = list(set(arr))

W, H = 10, 10

covered = set()
for x, y in arr:
    for dx in range(W):
        for dy in range(H):
            covered.add((x+dx, y+dy))

print(len(covered))