# 1) 일반적인 다익스트라 알고리즘


def dijkstra(start):
    visited = [False] * (n + 1)  # 방문 처리 리스트(최단 거리가 확정된 정점)
    visited[start] = True
    distance[start] = 0

    # 시작 정점과 인접한 정점에 대해 최단 거리 초기화
    for e, w in graph[start]:
        distance[e] = w

    # 시작 정점을 제외한 나머지 정점에 대해서만 반복하므로 n - 1 번 반복함
    for _ in range(n - 1):
        # 1. 최단 거리가 확정되지 않은 정점들 중 최단 거리가 가장 짧은 정점을 선택
        min_dist = INF
        for i in range(1, n + 1):
            if not visited[i] and min_dist > distance[i]:
                min_node = i
                min_dist = distance[i]

        # 2. 해당 정점 최단 거리 확정
        visited[min_node] = True

        # 3. 해당 정점에 인접한 정점에 대해 최단 거리 갱신
        for next_node, dist in graph[min_node]:
            new_dist = distance[min_node] + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist


n, m = map(int, input().split())  # 정점, 간선 개수
graph = [[] for _ in range(n + 1)]
INF = 99999999  # 나올 수 없는 임의의 큰 수
distance = [INF] * (n + 1)  # 출발 정점에서 다른 정점들까지의 최단 거리(무한으로 초기화)

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))  # 방향 그래프

dijkstra(1)  # 1번 정점에서 시작
print(distance)


'''
[입력]

6 11
1 2 3
1 3 5
2 3 2
2 4 6
3 2 1
3 4 4
3 5 6
4 5 2
4 6 3
5 1 3
5 6 6


[출력]

[99999999, 0, 3, 5, 9, 11, 12]
'''
