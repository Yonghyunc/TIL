# Today I Learned

<br><br>

---

# 분할 정복
설계 전략  
- 분할 (Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눔
- 정복 (Conquer) : 나눈 작은 문제를 각각 해결
- 통합 (Combine) : 필요하다면 해결된 해답을 모음

<br><br>

## 병합 정렬
여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식  

◽ 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄  
◽ top-down 방식

시간 복잡도 : O(n log n)

<br>

### < 과정 >  
◽ 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속함  
![image](https://user-images.githubusercontent.com/93974908/192276200-67d5ff49-e00a-47a0-a78e-4c1f9f18c0fb.png)


◽ 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합 (n개의 부분집합이 1개로 병합될 때까지 반복)
![image](https://user-images.githubusercontent.com/93974908/192276301-6b6da357-5229-45aa-995a-151f1d085751.png)

### 💻 수도 코드
◽ 알고리즘 : 분할 과정
```
merge_sort(LIST m)
    IF length(m) == 1:
        RETURN m
    
    LIST left, right
    middle <- length(m) / 2
    FOR x in m before middle
        add x to left
    FOR x in m after or equal middle
        add x to right
    
    left <- merge_sort(left)
    right <- merge_sort(right)

    RETURN merge(left, right)
```

◽ 알고리즘 : 병합 과정
```
merge(LIST left, LIST right)
    LIST result

    WHILE length(left) > 0 OR length(right) > 0
        IF length(left) > 0 AND lenght(right) > 0
            IF first(left) <= first(right)
                append popfirst(left) to result
            ELSE
                append popfirst(right) to result
        ELIF length(left) > 0
            append postfirst(left) to result
        ELIF length(right) > 0
            append popfirst(right) to result
    RETURN result
```




<br><br>

## 퀵 정렬
주어진 배열을 두 개로 분할하고, 각각을 정렬  

#### ❗ 병합 정렬과 다른 점 ❗
1. 병합 정렬은 그냥 두 부분으로 나누는 반면, 퀵 정렬은 분할할 때 기준아이템 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킴
2. 각 부분의 정렬이 끝난 후, 병합 정렬은 "병합"이 필요하지만, 퀵 정렬은 필요하지 않음

◽ 알고리즘
```
quickSort(A[], l, r)
    if l < r
        s <- partition(A, l, r)
        quickSort(A[], l, s - 1)
        quickSort(A[], s + 1, r)
```
> if l < r : 내가 정렬할 구간이 실제로 존재하는 경우 

<br>

◽ Hoare-Partition 알고리즘
```
partition(A[], l, r)
    p <- A[l]           // p: 피봇 값
    i <- l, j <- r
    WHILE i <= j
        WHILE i <= j and A[i] <= p : i ++
        WHILE i <= j and A[i] >= p : j --
        IF i < j : swap(A[i], A[j])
    
    swap(A[l], A[j])
    RETURN j
```
> swap(A[l], A[j]) : 피봇이 자기자리를 찾아가는 과정


<br>

### 🔗[quick_sort.py](code/quick_sort.py)

<br>


◽ 아이디어  
p(피봇)값들 보다 큰 값은 오른쪽, 작은 값들은 왼쪽 집합에 위치하도록 함  
피봇을 두 집합의 가운데에 위치시킴  

<br>

◽ 피봇 선택 : 왼쪽 끝 / 오른쪽 끝 / 임의의 세개 값 중 중간 값  

<br>

◽ Lomuto partition 알고리즘
```
partition(A[], p, r)
    x <- A[r]
    i <- p - 1

    FOR j in p -> r - 1
        IF A[j] <= x
            i ++, swap(A[i], A[j])
    
    swap(A[i + 1], A[r])
    RETURN i + 1
```


<br><br>

## 이진 검색
자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법  
> 자료가 정렬되어 있어야 함!!

<br>

### < 과정 >  
1. 자료의 중앙에 있는 원소를 고름
2. 중앙 원소의 값과 찾고자 하는 목표 값 비교
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해 새로 검색 수행, 크다면 오른쪽 반에 대해 새로 검색 수행
4. 찾고자 하는 값을 찾을 때까지 1 ~ 3 과정 반복


<br><br>


◽  알고리즘 : 반복구조
```
binarySearch(n, S[], key)
low <- 0
high <- n - 1

WHILE low <= high
    mid <- low + (high - low) / 2
    
    IF S[mid] == key
        RETURN mid
    ELIF S[mid] > key
        high <- mid - 1
    ELSE
        low <- mid + 1
RETURN -1
```

<br>

◽ 알고리즘 : 재귀구조
```
binarySearch(a[], low, high, key)
    IF low > high
        RETURN -1
    ELSE
        mid <- (low + high) / 2
        IF key == a[mid]
            RETURN mid
        ELIF key < a[mid]
            RETURN binarySearch(a[], low, mid -1 ,key)
        ELSE
            RETURN binarySearch(a[], mid + 1, high, key)
```

<br><br>

### ▶ 분할 정복의 활용
병합 정렬 : 외부 정렬의 기본이 되는 정렬 알고리즘, 멀티코어 CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 사용  

퀵 정렬 : 매우 큰 입력 데이터에 대해 좋은 성능 O


<br><br>

---

# 백트래킹
여러 가지 선택지(옵션)들이 존재하는 상황에서 한가지 선택  
선택이 이루어지면 새로운 선택지들의 집합이 생성됨  
이런 선택을 반복하면서 최종 상태에 도달  

<br>

#### ❗ 백트래킹과 깊이 우선 탐색과의 차이 ❗
어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임 == **Prunning (가지치기)** 

*백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만, 이 역시 최악의 경우에는 여전히 지수함수 시간을 요하므로 처리 불가능한 경우 O*  

<br>

### 🚩 백트래킹 알고리즘
1. 상태 공간 트리의 깊이 우선 검색 실시
2. 각 노드가 유망한지 점검
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색 계속

◽ 일반 백트래킹 알고리즘  
```
checknode(node v)
    IF promising(v)
        IF there is a solution at v
            write the solution
        ELSE
            FOR each child u of v
                checknode(u)
```

상태공간트리




<br>

### 🔗[부분집합의합.py](code/부분집합의합.py)

<br>