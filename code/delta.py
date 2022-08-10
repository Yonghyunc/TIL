di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 3
M = 4
arr = [[1, 2, 3, 4], [4, 5, 6, 7]]

for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)




# 다른 방법

for i in range(N):
    for j in range(M):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)



# 만약 두 칸씩 이동해야 한다면 ?

for i in range(N):
    for j in range(M):
        for d in range(1, 3): # 두 칸 이동
            for k in range(4):
                ni = i + di[k] * d
                nj = j + dj[k] * d
                if 0 <= ni < N and 0 <= nj < M:
                    print(ni, nj)

for i in range(N):
    for j in range(M):
        for k in range(4): # 방향 먼저 해도 상관없음
            for d in range(1, 3): 
                ni = i + di[k] * d
                nj = j + dj[k] * d
                if 0 <= ni < N and 0 <= nj < M:
                    print(ni, nj)