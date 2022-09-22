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

