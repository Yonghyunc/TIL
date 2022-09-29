# 유니온 파인드 (Union-Find)
# == 서로소 집합 == 상호 배타 집합 == Disjoint Set


# 1. 반복문
def find_set1(node):
    while node != parent[node]:
        node = parent[node]
    return node


# 2. 재귀
def find_set2(node):
    if node != parent[node]:
        return find_set2(parent[node])
    return node


# 3. 재귀 - 경로 압축 (부모 노드를 대표값으로 만듦)
def find_set3(node):
    if node != parent[node]:
        parent[node] = find_set3(parent[node])
    return parent[node]


n, m = map(int, input().split())        # 정점, 간선(Union 횟수) 개수
parent = list(range(n + 1))

for _ in range(m):
    x, y = map(int, input().split())
    x_root, y_root = find_set1(x), find_set1(y)

    # Union
    if x_root != y_root:        # 서로소 집합인 경우만 합집합 연산
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root

# 출력
for i in range(1, n + 1):
    print(find_set1(i), end=' ')
print()
print(parent)


'''
[입력]

6 4
5 6
4 5
3 4
1 3


[출력]

1 2 1 1 1 1 
[0, 1, 2, 1, 3, 4, 5]
'''