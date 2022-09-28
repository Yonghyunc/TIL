def prim2(r, V):
    MST = [0] * (V + 1)  # MST 포함여부
    MST[r] = 1  # 시작정점 표시
    s = 0  # MST 간선의 가중치 합
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V + 1):  # MST에 포함된 정점i와 인접한 정점j 중 MST에 포함되지 않은 비용 중 최소 비용
            if MST[i] == 1:
                for j in range(V + 1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        u = j
                        minV = adjM[i][j]
        s += minV
        MST[u] = 1
    return s


V, E = map(int, input().split())
adjM = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    # 인접행렬
    adjM[u][v] = w
    adjM[v][u] = w

ans = prim2(0, V)
print(ans)
