# 인접 행렬

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]  # 이차원 행렬

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1  # 간선이 있으면 1
    graph[v2][v1] = 1  # 무방향

for line in graph:
    print(*line)
