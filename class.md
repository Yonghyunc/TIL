자료구조 : 데이터 저장 + 연산 (삽입, 삭제, 수정, 조회) 
- 리스트, 집합, 딕셔너리, 스택, 큐, 그래프, 트리, 힙,...

알고리즘 
- DFS. BFS, 크루스킬, 프림, 다익스트라, 퀵 정렬, 병합 정렬,...

사고방식 : 정해진 공식 X, 문제를 푸는 방식
- 완전 검색(탐색), DP, 그리디, 분할정복 

> DFS, BFS 는 완전 탐색으로 만들어진 알고리즘


선택 정렬 -> 완전 탐색 -> 그리디  

정렬
- 안정 정렬 : 같은 수가 정렬 후에도 순서가 동일
  - 버블, 삽입, 병합, 카운팅(뒤에서부터 탐색)
- 불안정 정렬 : 뒤죽박죽
  - 선택, 퀵
--> 결국에 쓰는 건 sort, sorted ㅋㅋ

> 답이 같아도 방식이 다르다

---

선택 정렬  
시간복잡도 O(n^2)  

최소값을 선택해서 앞으로 옮김

---

완전 탐색 (Brute-force)  
모든 경우의 수  
문제 유형이 안 보이면 완전 탐색으로 봐야 함 -> 안 풀리는 문제는 X (시간초과가 날 뿐)  

재귀 itertools

``` python
def permutations(i, k):
    if i == k:  # 인덱스 i == 원소의 개수
        result.append(p)
        return

    for j in range(i, k):
        p[i], p[j] = p[j], p[i]
        permutations(i + 1, k)
        p[i], p[j] = p[j], p[i]


p = [1, 2, 3]
result = []

permutations(0, 3)
print(result)

# result
# [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
```
얕은 복사 (주소값 참조) -> result에 들어가는 모든 p가 동일함  

<해결방법>  
1. list 내장함수를 이용하여 p 배열을 새로운 객체로 만들어 줄 수 있음  
`result.append(list(p))`  
2. 리스트 슬라이싱
`result.append(p[:])`


``` python
from itertools import permutations, combinations
# 튜플로 반환

numbers = [1, 2, 3, 4]
length = 3

# 순열
print("--순열--")
for case in permutations(numbers, length):
    print(case)


# 조합
print("--조합--")
for case in combinations(numbers, length):
    print(case)
```

---

permutations 객체를 출력하면 객체 자체가 나옴
print(permutations(numbers, length)) 의 경우에는
모든 순열의 경우를 리스트에 적재한 상태가 아니라 들고만 있는 상태  
iterator : itertools의 모듈들이 반환하는 자료구조 (메모리 적재 X, 계산 X -> 불러올 때마다 현실화) 
``` python 
a = map(int, ["1", "2"])
for i in a:
    print(i)
> 1
> 2

b = list(a)
print(b)
> []

print(map(int, ["1", "2"]))
> <map object at 0x000001F52AA646D0>
```


---

generator은 iterator의 부분집합  
모든 generator는 iterator 이다  
(모든 iterator가 generator는 아님)  
즉, 메모리에 적재되지 않고 뽑으면 사라진다는 특성 또한 존재한다.  

``` python
a = (i for i in range(100000))
print(a)

# <generator object <genexpr> at 0x000001F03CD9DCF0>
```

``` python
import sys

a = sys.getsizeof([i for i in range(100000)])
b = sys.getsizeof((i for i in range(100000)))
c = sys.getsizeof((i for i in range(100000000)))
print(a)
print(b)
print(c)

# 800984
# 112
# 112
```
> 메모리 문제 발생 시 제너레이터 사용 O  
> BUT 반복문을 한 번 밖에 사용하지 못함  
> 딱 한 번의 반복문을 사용할 때 메모리를 아끼기 위해 제너레이터 사용 가능

---

그리디 (사고방식)  
지금 가장 좋은 것을 선택  

![image](https://user-images.githubusercontent.com/93974908/191639320-c8906404-dbba-4d87-882a-1401c717bc83.png)



<br><br>

---

# 0929 그래프

- 최소신장트리(MST)
  - 크루스칼 (집합의 개념을 이용하여 최소신장트리를 찾음) - 서로소 집합(union find)
  - 프림
- 최단경로 알고리즘 - 다익스트라

<br>

## Union - Find
서로소집합  
상호배타집합    
Disjoint Set    

집합의 연산 2가지   
- 멤버십 연산 : in, not in  ➡ Find
- 합집합, 교집합, 차집합 ➡ Union

서로소집합 : 교집합이 없는, 원소가 겹치지 않는 집합

Union-Find
1. make_set
2. find_set
> 대표값(루트노드) : 자기자신 == 부모값

3. union
> find_set 이후 대표값이 다름면 (집합이 다르면) union 가능

집합 -> 트리 형태로 표현    
union_find 에서는 아래에서 위로 올라가는 모양 (루트 노드를 찾음)    
같은 루트를 가르키면 같은 집합  
다른 루트를 가르키면 다른 집합  

같은 집합인지 확인(find_set) -> 합침(union) 
> 일반적으로 더 작은 수에 붙임 

연산 시간   
union - 비교, 할당 뿐   
find 연산 시간이 가장 중요!      - 어떻게 줄일 것이냐   
➡ **경로 압축**    
타고 올라가는 경로가 너무 많으니 압축을 해보자!!    

``` python

# 3. 재귀 - 경로 압축 (부모 노드를 대표값으로 만듦)
def find_set3(node):
    if node != parent[node]:
        parent[node] = find_set3(parent[node])  # 바로 부모만 조회하면 경로가 압축됨
    return parent[node]                         # 현 루트노드를 가져감

```
처음 한 번은 비효율적일 수 있음     
BUT 두번째부터는 경로가 압축되었으므로 타고타고 올라가지 않음   

<br>

## 최소신장트리 (MST)
신장트리    
: 그래프의 모든 노드를 포함하지만, 사이클(순환구조) X     
이어져만 있으면 됨 -> **집합 (Union-Find)**     

여러 신장트리 중 (간선의 가중치)비용이 가장 낮은 트리 ➡ **최소 신장 트리 **   


### 크루스칼
greedy 알고리즘  (최소 비용의 간선을 기준으로 그리디하게 선택)   
가장 적은 비용을 먼저 고름 (사이클이 만들어지지 않게)   
🔽
1. 간선 비용 기준으로 **정렬**
> 크루스칼은 그리디하게 해도 적절하다고 이미 증명됨 -> 그냥 해라

2. 최소 비용부터 뽑아나감
3. 서로소면 union / 아니면(이미 연결, 사이클) 넘어감



### 프림
정점 기준   
인접한 정점에 가는 길 중 최소 비용 선택     
1. 임의의 정점 선택 -> MST에 포함
2. MST에서 갈 수 있는 모든 정점 중 가장 최소 비용 선택

두 개의 리스트 필요     
visited  ->  False로 초기화   : visited[v] == True라면 v가 MST 안에 속해있다
distance  -> infinite로 초기화  : MST에서 v로 가는 간선 비용    
> 인덱스 2가 가진 값의 의미 = 2"로" 가는 간선 비용의 값 

> visited = [False] * (n + 1)  # MST에 포함 여부 리스트     
> distance = [INF] * (n + 1)  # distance[v] => 정점 v가 MST에 속한 정점과 연결된 간선의 비용

인접 정점을 찾아야 하기 때문에 인접 리스트를 만들어야 함    


#### 힙을 이용한 프림 구현
최소 힙 : pop -> 가장 작은 원소   
최대 힙 : pop -> 가장 큰 원소   
힙 == 트리구조  (완전 이진 트리)    

heapq <- 우선순위 큐 (우선순위가 높은 것이 먼저 나감)  

from heapq import heappush, heappop     

heap -> O(log n) 즉, 훨씬 빠름

heappop -> 가장 작은 가중치부터 빠져나옴

<br>

크루스칼 vs. 프림   
어떤 걸 써야할까?   
간선이 많으면 크루스칼 불리(간선) -> 프림 사용    
정점이 많으면 프림 불리 -> 크루스칼 사용

<br><br>

## 다익스트라
특정 정점 -> 다른 모든 정점으로 가는 최단거리    
음의 간선이 없어야 함   
그리디 알고리즘 

동작과정    
1. 출발지점 k 정함    
2. distance : k -> v 비용   
3. 갱신

간선의 값의 합이 최소이면 최단거리  
프림 알고리즘과 비슷    
visited -> 값이 확정되면(True) 그 값이 최단거리   
distance -> k에서 v로 가는 최단거리     

프림과 다른 점  
1. 누적값으로 최단거리를 구함     
2. visited 리스트 O


visited = 최단 경로 확정

heap 이용 시,   
``` python
# 2. 이미 최단 거리로 기록되어 있는 값보다 높은 경우 무시
if min_dist > distance[min_node]:
    continue
```
visited를 최단 경로를 확정하는 용도로 쓰지는 않지만 쓰임        
