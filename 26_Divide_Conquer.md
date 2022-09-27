# Today I Learned
[분할 정복](#분할-정복)
- [병합 정렬](#병합-정렬)
- [퀵 정렬](#퀵-정렬)
- [이진 검색](#이진-검색)

[백트래킹](#백트래킹)
<br><br>

---

# 분할 정복
> 하나의 사고방식

설계 전략  
- 분할 (Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눔
- 정복 (Conquer) : 나눈 작은 문제를 각각 해결
- 통합 (Combine) : 필요하다면 해결된 해답을 모음

<br><br>

## 병합 정렬 (Merge Sort)
여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식  
> 분할했던 리스트를 합치면서 정렬  
> list1 = [1 2 4 7]  
> list2 = [3 6 8 9]  
> 1과 3 비교 -> 2와 3 비교 -> 4와 3 비교 -> ... -> 7과 8 비교 -> 자연스럽게 남은 숫자가 끝에 들어감  
> 1 2 3 4 6 7 8 9  


◽ 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄  
◽ top-down 방식

시간 복잡도 : O(n log n)
> log n : 반씩 쪼갬
> 쪼갤 때마다 연산이 이루어짐 / 각각의 원소를 다 보기 때문에 * n 

<br>

### < 과정 >  
◽ 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속함  
> 물리적으로 반으로 분할

![image](https://user-images.githubusercontent.com/93974908/192276200-67d5ff49-e00a-47a0-a78e-4c1f9f18c0fb.png)


◽ 병합 단계 : 2개의 부분집합을 정렬하면서 하나의 집합으로 병합 (n개의 부분집합이 1개로 병합될 때까지 반복)
![image](https://user-images.githubusercontent.com/93974908/192276301-6b6da357-5229-45aa-995a-151f1d085751.png)

### 💻 코드
◽ 알고리즘 : 분할 과정
``` python 
def merge(left, right):
    merged_arr = []
    i, j = 0, 0  # 왼쪽, 오른쪽 리스트 각각의 인덱스

    while i < len(left) and j < len(right):
        # 왼쪽 리스트의 원소가 작거나 같으면 삽입
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        # 오른쪽 리스트의 원소가 작으면 삽입
        else:
            merged_arr.append(right[j])
            j += 1

    # 왼쪽과 오른쪽 리스트 중 하나라도 원소를 모두 소모하면, 남은 리스트의 원소를 모두 삽입
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    return merged_arr


def merge_sort(arr):
    # 더 이상 분할할 수 없는 경우(종료 조건)
    if len(arr) <= 1:
        return arr

    # 1. 리스트를 분할하여 각각 정렬
    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    # 2. 정렬된 두 리스트를 병합
    return merge(left_arr, right_arr)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
```
> 파이썬의 슬라이싱 : 범위를 벗어나는 슬라이싱 -> 빈 리스트를 반환함  
> `merged_arr.extend(left[i:])` 해당 코드 문제 X  

> L.extend(m) : 순회형 m의 모든 항목들을 리스트 끝에 추가 (+=)

<br>

▫ 병합 정렬의 단점 : 빠르지만 메모리를 많이 사용함 (추가적으로 리스트를 계속 만들면서 정렬하기 때문에)

<br><br>

## 퀵 정렬
> 전통적인 정렬 알고리즘 중 평균적으로 가장 빠름

주어진 배열을 두 개로 분할하고, 각각을 정렬  
> 특정한 피벗 값을 기준으로 분할 

시간 복잡도 : O(n log n)  

> 이진 검색과 달리 정렬되어 있지 않기 때문에, 가운데 값으로 피벗을 정할 수 없음  
> 어떤 값을 피벗으로 뽑느냐에 따라 코드가 달라짐  
> 왼쪽, 가운데, 오른쪽, 랜덤 등등  

#### ❗ 병합 정렬과 다른 점 ❗
1. 병합 정렬은 그냥 두 부분으로 나누는 반면, 퀵 정렬은 분할할 때 기준아이템 중심으로, 이보다 작은 것은 왼편, 큰 것은 오른편에 위치시킴
2. 각 부분의 정렬이 끝난 후, 병합 정렬은 "병합"이 필요하지만, 퀵 정렬은 필요하지 않음

<br>

◽ 알고리즘
``` python
def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)  # 피벗을 기준으로 왼쪽, 오른쪽을 나누는 가운데 위치 구하기
        quick_sort(arr, left, middle - 1)  # 왼쪽 퀵정렬
        quick_sort(arr, middle + 1, right)  # 오른쪽 퀵정렬
```
> if left < right : 내가 정렬할 구간이 실제로 존재하는 경우   


<br>

◽ Hoare-Partition 알고리즘
``` python
def partition(arr, left, right):
    pivot = arr[left]  # 가장 왼쪽 원소를 피벗으로 지정
    i, j = left, right

    while i <= j:
        # 1. 피벗보다 큰 값이 나올 때까지 i + 1
        while i <= j and arr[i] <= pivot:
            i += 1

        # 2. 피벗보다 작은 값이 나올 때까지 j - 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        # 3. 피벗보다 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]  # i > j가 되면 피벗과 j 위치 원소 교환 (피벗을 가운데로 옮기는 작업)

    return j
```
> s (맨 왼쪽에서 시작) : 피벗값보다 크거나 같은 값을 만나면 그 자리에서 멈춤  
> e (맨 오른쪽에서 시작) : 피벗값보다 작거나 같은 값을 만나면 그 자리에서 멈춤  
> 
> 멈췄는데 s < e 이면 s <-> e 
> e < s 이면 멈춰서 피벗값 교환  
> 
> `arr[left], arr[j] = arr[j], arr[left]` : 피벗이 자기자리를 찾아가는 과정  
> 
> 각 왼쪽, 오른쪽 리스트에서 새로운 정렬과정 수행  

일반적으로 호어가 로무트보다 효율적  
퀵 정렬 == 호어 방식


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
> 호어와 분할방식이 다름 (오른쪽을 피벗으로 놓고 몰아감)
> i = -1, j = 0 에서 시작 (함께 이동)

``` python
def partition(arr, left, right):
    pivot = arr[right]  # 가장 오른쪽 원소를 피벗으로 지정
    i, j = left - 1, left

    while j < right:
        if pivot > arr[j]:
            i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1
```
> arr[i + 1] : 피벗을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽에 오게 만듦
> i + 1 임을 유의


<br>

◽ 파이썬스러운 방식 but 메모리 더 많이 씀

``` python
def quick_sort(arr):
    # 더 이상 분할할 수 없는 경우(종료 조건)
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # 가장 왼쪽 원소를 피벗으로 지정
    arr = arr[1:]  # 피벗 제외하여 새로운 리스트 생성

    left_arr = [i for i in arr if i <= pivot]  # 피벗보다 작거나 같은 원소는 왼쪽으로 분할
    right_arr = [j for j in arr if j > pivot]  # 피벗보다 큰 원소는 오른쪽으로 분할

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
print(quick_sort(numbers))
```
> 안정정렬이라는 장점 有


> 퀵 정렬 ➡ 불안정정렬  
> arr = [2, 1, 1, 2, 3, 3]    
> 안정정렬 : 같은 값이더라도 순서가 보장 (병합 정렬)  
> 불안정정렬: 같은 값이면 순서 보장 X (퀵 정렬)  

<br>


▫ 퀵 정렬의 단점  
O(n^2)이 나올 때가 있음 - 피벗이 정확하게 반을 나누지 않는 경우  
ex) 1 2 3 4 5 6 (pivot == 1) ➡ n번의 분할 시행 ➡ O(n^2)  
이미 정렬되어 있거나, 피벗을 계속해서 최소값을 뽑는 경우  

BUT 흔한 경우는 아니기 때문에, 일반적으로 퀵 정렬이 제일 빠르다고 함


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