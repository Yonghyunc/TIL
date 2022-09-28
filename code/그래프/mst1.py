'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


v, e = map(int, input().split())
adjM = [[0] * (v + 1) for _ in range(v + 1)]
adjL = [[] for _ in range(v + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())

    # 인접행렬
    adjM[u][v] = w
    adjM[v][u] = w

    # 인접리스트
    adjL[u].append((v, w))
    adjL[v].append((u, w))
