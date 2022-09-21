# Today I Learned


<br><br>

---

# 반복(Iteration) & 재귀(Recursion)

**반복 ↔ 재귀**  

반복 : 수행하는 작업이 완료될 때까지 계속 반복 (루프)  
재귀 : 주어진 문제의 해를 구하기 위해 동일하면서 더 작은 문제의 해를 이용  
> 파이썬의 경우, 재귀의 깊이 제한이 있음 (주의할 것!!)

<br><br>

### ◼ 반복구조  
초기화 : 반복되는 명령문을 실행하기 전에 (한번만) 조건 검사에 사용할 변수의 초기값 설정  
조건 검사  
반복할 명령문 실행  
업데이트 : 무한 루프가 되지 않게 조건이 거짓이 되게 함  

<br>

### 🔹 반복을 이용한 선택정렬  
``` python
# 오름차순 정렬

def selection_sort(arr):
    n = len(arr)

    for i in range(0, n - 1):
        # min_idx를 정렬되지 않는 부분 중 맨 앞 인덱스로 초기화
        min_idx = i     

        # 맨 앞 인덱스 + 1 부터 비교하여 최소값 인덱스 찾기
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]     # 맨 앞의 값과 최소값을 교환


numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
selection_sort(numbers)
print(numbers)


# result
# [1, 2, 2, 3, 3, 5, 5, 7, 8, 9]
```

<br><br>

### ◼ 재귀적 알고리즘
하나 또는 그 이상의 기본 경우  
하나 또는 그 이상의 유도된 경우  

<br>

### ◼ 재귀 함수  
함수 내부에서 직접 혹은 간접적으로 자기 자신을 호출하는 함수  
재귀적 정의를 이용하여 함수 구현 ➡ 기본 부분 + 유도 부분  
함수 호출은 프로그램 메모리 구조에서 스택을 사용 ➡ 재귀 호출은 반복적인 스택의 사용을 의미하며 메모리 및 속도에서 성능저하 발생  

<br>

### 🔹 팩토리얼 재귀 함수  
▶ 재귀적 정의
- 기본 부분 : N <= 1 인 경우, n = 1
- 유도 부분 : N > 1, n! = n * (n -1)!


▶ n! 에 대한 재귀함수
``` python
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)
```
<br>

### 🔹 재귀를 이용한 선택정렬
``` python
def selection_sort(i):
    # 종료 조건 (마지막 원소일 때는 더이상 정렬할 필요가 없으므로 재귀 종료)
    if i == len(numbers) - 1:
        return

    # min_idx를 정렬되지 않는 부분 중 맨 앞 인덱스로 초기화
    min_idx = i 

    # 맨 앞 인덱스 + 1 부터 비교하여 최소값 인덱스 찾기
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_idx]:
            min_idx = j

    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]    # 맨 앞의 값과 최소값을 교환
    selection_sort(i + 1)                                          # 재귀 호출


numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
selection_sort(0)
print(numbers)


# result 
# [1, 2, 2, 3, 3, 5, 5, 7, 8, 9]
```


<br><br>

### ❔ 반복 ❔ 재귀 ❔  
재귀는 문제 해결을 위한 알고리즘 설계가 간단하고 자연스러움  
BUT, 일반적으로 재귀적 알고리즘은 반복 알고리즘보다 더 많은 메모리와 연산을 필요로 함  
입력 값 n이 커질수록 재귀 알고리즘은 반복에 비해 비효율적일 수 있음

<br>

![image](https://user-images.githubusercontent.com/93974908/191393418-31d45af5-bca6-4630-9ba5-1cb55a81d028.png)

<br><br>

---

# 완전 검색 기법

> Baby-gin Game 문제

고지식한 방법(brute-force)  
문제를 해결하기 위한 간단하고 쉬운 접근법   
상대적으로 빠른 시간에 알고리즘 설계 O  
문제에 포함된 자료의 크기가 작다면 유용  

<br>

완전 검색 ➡ 수행 속도는 느리지만, 해답을 찾아낼 확률이 높음  

**문제 풀이 시, 우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직**

<br><br>

---

# 📌 순열 (Permutation)
서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것  
서로 다른 n개 중 r개를 택하는 순열 ➡ nPr  

<br>

nPr = n * (n - 1) * (n - 2) * ... * (n - r + 1) = n! / (n - r)!    
nPn = n!

<br>
다수의 알고리즘 문제들은 순서화된 요소들의 집합에서 최선의 방법을 찾는 것과 관련O

N개의 요소들에 대해 n!개의 순열 존재 ➡ n > 12 인 경우, 시간 복잡도 ⬆⬆⬆  

<br><br>

## 순열 생성 방법  
- 사전적 순서
- 최소 변경을 통한 방법

<br>

## 🔹 단순하게 순열을 생성하는 방법
``` python
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            for k in range(1, 4):
                if k != i and k != j:
                    print(i, j, k)

# result
'''
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''
```


<br>

## 🔹 재귀 호출을 통한 순열 생성  
p = [] : 데이터가 저장된 배열  
k : 원소의 개수
n : 선택된 원소의 수  

### 1️⃣ 자기 길이만큼 순열 뽑기  
리스트 자기 자신을 이용하기 때문에 메모리 절약 가능
``` python
def permutations(i, k):
    if i == k:  # 인덱스 i == 원소의 개수
        print(p)
        return

    for j in range(i, k):
        p[i], p[j] = p[j], p[i]
        permutations(i + 1, k)
        p[i], p[j] = p[j], p[i]


p = [1, 2, 3]
permutations(0, 3)


# result
'''
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 2, 1]
[3, 1, 2]
'''
```
![image](https://user-images.githubusercontent.com/93974908/191396907-9cfa0981-4fcb-4b09-a165-c1e5ca63610b.png)

<br>

### 2️⃣ visited를 이용해 순열 뽑기

▶ 자기 길이만큼 순열 뽑기
``` python
def permutations(i, k):
    if i == k:
        print(p)
        return

    for j in range(k):
        if not visited[j]:                # a[j]가 아직 사용되지 않았으면
            # 1. i번째 원소를 뽑는다
            visited[j] = True             # a[j] 사용됨으로 표시
            p[i] = a[j]                   # p[i]는 a[j]로 결정

            # 2. 재귀함수 진행
            permutations(i + 1, k)        # p[i+1] 값을 결정하러 이동

            # 3. 재귀함수 종료 후, 뽑았던 i번째 원소 삭제
            visited[j] = False            # a[j]를 다른 자리에서 쓸 수 있도록 해제


n = 3
a = [i for i in range(1, n + 1)]
visited = [False] * n
p = [0] * n
permutations(0, n)


#result
'''
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
'''
```
<br>

▶ 원하는 개수만큼 순열 뽑기
``` python
# k개의 수 중 r개 선택한 순열

def permutations(i, k, r):
    if i == r:
        print(p)
        return

    for j in range(k):
        if not visited[j]:                # a[j]가 아직 사용되지 않았으면
            visited[j] = True             # a[j] 사용됨으로 표시
            p[i] = a[j]                   # p[i]는 a[j]로 결정

            permutations(i + 1, k, r)     # p[i+1] 값을 결정하러 이동
            
            visited[j] = False            # a[j]를 다른 자리에서 쓸 수 있도록 해제


n = 5           # 배열의 길이
r = 3           # 뽑고 싶은 원소의 개수
a = [i for i in range(1, n + 1)]
visited = [False] * n
p = [0] * r
permutations(0, n, 3)
```

<br><br>

---

# 📌 부분 집합
집합에 포함되는 원소들을 선택하는 것  

N개의 원소를 포함한 집합  
- 자기 자신과 공집합을 포함한 모든 부분집합의 개수는 2^n개
- 원소의 수가 증가하면 부분집합의 개수는 지수적으로 증가

<br>

### 바이너리 카운팅을 통한 사전적 순서
바이너리 카운팅은 사전적 순서로 생성하기 위한 가장 간단한 방법  

**바이너리 카운팅 (Binary Counting)**
- 원소 수에 해당하는 N개의 비트열 이용
- n번째 비트값이 1이면 n번째 원소가 포함되었음을 의미

<br>

### 🔹 모든 부분집합 생성
``` python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1 << n):  # 1 << n : 부분집합의 개수
    for j in range(n):
        if i & (1 << j):  # j번 비트가 0이 아니면 arr[j]가 부분집합의 원소
            print(arr[j], end=' ')
    print()
```
> 공집합을 빼고 싶다면 가장 바깥 for문의 범위를 range(1, 1 << n)으로 설정해주면 됨

<br>

### 🔹 재귀를 활용한 부분집합 생성
``` python
def subset(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    else:
        bit[i] = False
        subset(i + 1, k)
        bit[i] = True
        subset(i + 1, k)


arr = [3, 6, 7]
n = len(arr)

bit = [False] * n
subset(0, n)
```

<br><br>

---

# 📌 조합 (Combination)
서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것

nCr = n! / ((n - r)! * r!), (n >= r)  
nCr = n-1Cr-1 + n-1Cr  (재귀적표현)  
nC0 = 1 (아무것도 고르지 않는 1가지 경우)



![image](https://user-images.githubusercontent.com/93974908/191423009-18533821-375f-4414-a864-6f90cd4e21fe.png)

<br>

▶ 10개의 원소 중 3개를 고르는 조합
``` python
n = 10

for i in range(n - 2):              # j, k로 선택될 원소 남김
    for j in range(i + 1, n - 1):   # k로 선택될 원소 남김
        for k in range(j + 1, n):
            print(i, j, k)
```
<br>

▶ n개에서 r개를 고르는 조합 (재귀)
``` python
def combinations(n, r, s):
    if r == 0:
        print(*comb)

    else:
        for i in range(s, n - r + 1):
            comb[r - 1] = arr[i]
            combinations(n, r - 1, i + 1)


arr = [1, 2, 3, 4, 5]
n = len(arr)
r = 3
comb = [0] * r
combinations(n, r, 0)
```


1. 선택 (순열/부분집합/조합)
2. 행동
3. 결과비교

<br><br>

---

# 탐욕 (Greedy) 알고리즘
최적해를 구하는 데 사용되는 근시안적인 방법  
여러 경우 중 하나를 선택할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달  
각 선택 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, 그것이 최적이라는 보장은 없음

한번 선택된 것은 번복 X ➡ 제한적인 문제에 적용  
최적화 문제 : 가능한 해들 중에서 가장 좋은 해를 찾는 것

동작 과정 
1) 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분 해 집합에 추가
2) 실행 가능성 검사 : 새로운 부분 해 집합이 실행가능한지 확인
3) 해 검사 : 새로운 부분 해 집합이 문제의 해가 되는지 확인

> BUT, 최적해를 반드시 구한다는 보장 X

<br><br>

---

## 활동 선택 문제  
시작시간과 종료시간이 있는 n개의 활동들의 집합 A = {A1, A2, ..., An}, 1 <= i <= n에서 서로 겹치지 않는 최대갯수의 활동들의 집합 S를 구하는 문제   
➡ 양립 가능한 활동들의 크기가 최대가 되는 S(0, n+1) 부분집합을 선택하는 문제

<br>

### 탐욕 기법을 적용한 반복 알고리즘
![image](https://user-images.githubusercontent.com/93974908/191429157-82616075-f216-4776-b148-4c5b88e58400.png)
> 1) 종료 시간이 빠른 순으로 활동 정렬  
> 2) 종료 시간이 가장 빠른 a1 선택하고, 시간이 겹치는 활동을 모두 제거  
> 3) 남은 활동들에 대해 앞의 과정 반복

<br>


재귀 알고리즘

<br>

탐욕 알고리즘의 필수 요소
- 탐욕적 선택 속성
- 최적 부분 구조
원문제의 최적해 = 탐욕적 선택 + 하위 문제의 최적해

<br>

### 탐욕 기법과 동적 계획법 비교
|                            탐욕 기법                            |                     동적 계획법                      |
| :-------------------------------------------------------------: | :--------------------------------------------------: |
| 매 단계에서, 가장 좋게 보이는 것을 빠르게 선택 ➡ 지역 최적 선택 | 매 단계의 선택은 해결한 하위 문제의 해를 기반으로 함 |
|       하위 문제를 풀기 전에 (탐욕적) 선택이 먼저 이루어짐       |               하위 문제가 우선 해결됨                |
|                          Top-down 방식                          |                    Bottom-up 방식                    |
|                     일반적으로, 빠르고 간결                     |                  좀 더 느리고, 복잡                  |

<br>

### 대표적인 탐욕 기법 알고리즘
![image](https://user-images.githubusercontent.com/93974908/191434915-ce17eedc-5214-4091-b909-9fe8c492de73.png)


<br>


Baby-Gin 풀이  
[완전 탐색](baby_gin_1.py)  
[탐욕 기법](baby_gin_2.py)
