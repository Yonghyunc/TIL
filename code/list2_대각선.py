N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    for j in range(N):
        if i == j:
            s += arr[i][j]


# 대각선 인덱스 값이 같으니
s = 0
for i in range(N):
    s += arr[i][i]


# 반대 대각선
s = 0
for i in range(N):
    s += arr[i][N - 1 - i]


# 양방향 대각선 합을 구해라
# 크기가 홀수일 때, 가운데가 두 번 더해지는 것을 고려해야 함

s1 = 0
s2 = 0
for i in range(N):
    for j in range(N):
        if i > j:
            s1 += arr[i][j]
        elif i < j:
            s2 += arr[i][j]

s1 = 0
s2 = 0
for i in range(N):
    for j in range(i + 1, N):
        s2 += arr[i][j]
        s1 += arr[j][i]


# 사선의 합
