# 인접 리스트


n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]  # 이차원 행렬

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)  # 리스트에 인접 정점 삽입
    graph[v2].append(v1)  # 무방향

for line in graph:
    print(*line)
