def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split())  # V 마지막 정점, 0~V번 정점. 개수 (V + 1)ro
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])
edge.sort(key=lambda x: x[2])
rep = [i for i in range(V + 1)]  # 대표원소 배열

N = V + 1  # 실제 정점 수
cnt = 0  # 선택한 edge의 수
total = 0  # MST 가중치의 합
for u, v, w in edge:
    if find_set(u) != find_set(v):
        cnt += 1
        union(u, v)
        total += w
        if cnt == N - 1:  # 간선 수
            break

print(total)
