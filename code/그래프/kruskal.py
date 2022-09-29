# 특정 원소가 속한 집합 찾기 (루트 노드 찾기)
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])  # 경로 압축(Path compression)
    return parent[node]


n, m = map(int, input().split())  # 정점, 간선 개수
edges = []
for _ in range(m):
    s, e, w = map(int, input().split())  # 시작 정점, 도착 정점, 비용
    edges.append((w, s, e))

edges.sort()  # (중요) 최소 비용의 간선부터 차례로 검사하기 위해 비용을 기준으로 오름차순 정렬

parent = list(range(n + 1))
counts = 0  # MST의 간선 개수 (정점 - 1 개가 되면 종료를 하기 위함)
cost = 0  # MST의 가중치 총합(== 최소 비용)

for dist, x, y in edges:
    x_root, y_root = find_set(x), find_set(y)  # x와 y의 각각 대표값

    if x_root != y_root:  # 사이클이 아니면 (서로소이면)
        parent[y_root] = x_root  # union
        cost += dist
        counts += 1  # 없어도 정상적으로 동작하지만, 효율성을 위해 사용

        if counts >= n - 1:  # 간선의 최대 개수는 정점 - 1 이므로 break
            break

print(cost)


# def find_set(x):
#     while x != rep[x]:
#         x = rep[x]
#     return x


# def union(x, y):
#     rep[find_set(y)] = find_set(x)


# V, E = map(int, input().split())  # V 마지막 정점, 0~V번 정점. 개수 (V + 1)ro
# edge = []
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     edge.append([u, v, w])
# edge.sort(key=lambda x: x[2])
# rep = [i for i in range(V + 1)]  # 대표원소 배열

# N = V + 1  # 실제 정점 수
# cnt = 0  # 선택한 edge의 수
# total = 0  # MST 가중치의 합
# for u, v, w in edge:
#     if find_set(u) != find_set(v):
#         cnt += 1
#         union(u, v)
#         total += w
#         if cnt == N - 1:  # 간선 수
#             break

# print(total)
