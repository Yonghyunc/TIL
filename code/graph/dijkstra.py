# SWEA 1795. 인수의 생일 파티
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4xuqCqBeUDFAUx&categoryId=AV4xuqCqBeUDFAUx&categoryType=CODE&problemTitle=%EC%83%9D%EC%9D%BC+%ED%8C%8C%ED%8B%B0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1


def dijkstra(N, X, adj, d):
    for i in range(N + 1):
        d[i] = adj[X][i]
    U = [X]
    for _ in range(N - 1):  # N개의 정점 중 출발을 제외한 정점 선택
        w = 0
        for i in range(1, N + 1):
            if (i not in U) and d[i] < d[w]:  # 남은 노드 중 비용이 최소인 w
                w = i
        U.append(w)
        for v in range(1, N + 1):  # 정점 i가
            if 1 < adj[w][v] < 100000:  # w에 인접이면
                d[v] = min(d[v], d[w] + adj[w][v])


N, M, X = map(int, input().split())
adj1 = [[100000] * (N + 1) for _ in range(N + 1)]
for i in range(N + 1):
    adj1[i][i] = 0
for _ in range(M):
    x, y, c = map(int, input().split())
    adj1[x][y] = c
dout = [0] * (N + 1)
dijkstra(N, X, adj1, dout)
print(dout)
