N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    for j in range(N):
        s += arr[i][j]

print(s)
