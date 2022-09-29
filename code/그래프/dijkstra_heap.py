# 2) 힙을 이용한 다익스트라 알고리즘

from heapq import heappush, heappop


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]  # 힙 선언 [(비용, 정점)]

    while heap:
        # 1. 최단 거리가 가장 짧은 정점을 선택
        min_dist, min_node = heappop(heap)

        # 2. 이미 최단 거리로 기록되어 있는 값보다 높은 경우 무시
        if min_dist > distance[min_node]:
            continue

        # 3. 해당 정점에 인접한 정점에 대해 최단 거리 갱신
        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist  # new_distance
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 나올 수 없는 임의의 큰 수
distance = [INF] * (n + 1)  # 출발 정점에서 다른 정점들까지의 최단 거리(무한으로 초기화)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

dijkstra(1)  # 1번 정점에서 시작
print(distance)
