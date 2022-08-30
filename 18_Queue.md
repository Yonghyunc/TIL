# Today I Learned
- [큐](#큐queue)
  - [선형 큐](#선형큐)
  - [원형 큐](#원형-큐)
  - [우선순위 큐](#우선순위-큐)
- [BFS](#bfs-breadth-first-search)

<br/><br/>

---

# 큐(Queue)
- 삽입과 삭제의 위치가 제한적
  - 뒤 : 삽입만
  - 앞 : 삭제만
- 선형 자료구조
- **선입선출구조(FIFO)**
  - 큐에 삽입한 순서대로 원소가 저장
  - 가장 먼저 삽입된 원소는 가장 먼저 삭제


<br/>

### 💡 큐의 선입선출 구조
- Front (머리) : 저장된 원소 중 첫 번째 원소 (또는 삭제된 위치)
- Rear (꼬리) : 저장된 원소 중 마지막 원소

<br/>

### 💡 큐의 기본 연산
- 삽입 : enQueue
- 삭제 : deQueue

<br/>

- 공백 상태의 큐 생성 : createQueue()
- 공백상태인지 확인 : isEnmpty()
- 포화상태인지 확인 : isFull()
- 큐의 앞쪽에서 원소를 삭제없이 반환 : Qpeek()

<br/>

## 큐의 연산 과정
1. 공백 큐 생성 : createQueue() <br/>
[] <br/>
front = rear = -1

> Q = [0] * 100 처럼 크기가 정해진 방식으로 큐를 생성해서 값 추가

<br/>

2. 원소 A 삽입 : enQueue(A) <br/>
[A] <br/>
front = -1 <br/>
rear = A

<br/>

3. 원소 B 삽입 : enQueue(B) <br/>
[A, B] <br/>
front = -1 <br/>
rear = B

<br/>

4. 원소 반환/삭제 : deQueue() <br/>
[B] <br/>
front = 0 <br/>
rear = B
> front : 마지막으로 꺼낸 자리 <br/>
> rear : 마지막 저장 위치

<br/>

5. 원소 C 삽입 : enQueue(C) <br/>
[B, C] <br/>
front = 0 <br/>
rear = C

<br/>

6. 원소 반환/삭제 : deQueue()<br/>
[C]<br/>
front = 1<br/>
rear = C

<br/>

7. 원소 반환/삭제 : deQueue() <br/>
[] <br/>
front = rear = 2
> front와 rear와 같아지면 큐가 비어있는 상태


<br/><br/>

---

## 1️⃣ 선형큐
- 1차원 배열 이용한 큐
- 큐의 크기 = 배열의 크기

<br/>

- 초기 상태 : front = rear = -1
- 공백 상태 : front == rear
- 포화 상태 : rear == n -1 (n: 배열의 크기)


<br/>

### ✏️ 삽입 : enQueue(item)
마지막 원소 뒤에 새로운 원소 삽입

<br/>

### ✂️ 삭제 : deQueue()
가장 앞에 있는 원소를 삭제 + 반환하기 위해

<br/>

### 🔧 공백상태 및 포화상태 검사 : isEmpty(), isFull()
> 크기가 정해진 리스트를 이용하여 큐를 구성했을 때

<br/>

### 🔎 검색 : Qpeek()
가장 앞에 있는 원소를 검색하여 반환


``` python 

class Queue:
    def __init__(self, n):
        self.size = n
        self.items = [None] * n
        self.front = -1  # 큐의 머리(앞쪽)
        self.rear = -1  # 큐의 꼬리(뒤쪽)

    # 1. 큐의 뒤쪽에 원소를 삽입하는 연산
    def enqueue(self, item):
        if self.is_full():
            # 여러 가지 방식으로 대응 가능
            # 1) 큐의 크기를 확장하는 방식
            # 2) 이에 대한 예외처리를 해주는 방식
            print('큐가 가득차서 원소를 삽입할 수 없습니다.')
        else:
            self.rear += 1
            self.items[self.rear] = item

    # 2. 큐의 앞쪽에서 원소를 삭제하고 반환하는 연산
    def dequeue(self):
        if self.is_empty():
            print('큐가 비어서 원소를 삭제 및 반환할 수 없습니다.')
        else:
            self.front += 1
            return self.items[self.front]

    # 3. 큐가 공백상태인지 확인하는 연산
    def is_empty(self):
        return self.front == self.rear  # 머리와 꼬리가 같은 곳을 가리키면 공백상태

    # 4. 큐가 포화상태인지 확인하는 연산
    def is_full(self):
        return self.rear == self.size - 1  # 꼬리가 큐의 마지막을 가리키면 포화상태

    # 5. 큐의 앞쪽에서 원소를 삭제 없이 반환하는 연산
    def q_peek(self):
        if self.is_empty():
            print('큐가 비어서 원소를 반환할 수 없습니다.')
        else:
            return self.items[self.front]


queue = Queue(3)  # 크기가 3인 큐 생성

# 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
print(queue.items)  # 삽입 전 큐의 모습
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.items)  # 삽입 후 큐의 모습

# 큐에서 세 개의 데이터 차례로 꺼내서 출력
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

```
큐를 쓸 때마다 이렇게 구현해서 사용해야 한다면, 너무 번거롭다. <br/>
파이썬은 큐를 따로 구현할 필요 없이, 리스트 자료형을 큐처럼 사용할 수 있다.

``` python

queue = []  # 큐 역할을 할 빈 리스트

# 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
print(queue)  # 삽입 전 큐의 모습
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # 삽입 후 큐의 모습

# 큐에서 세 개의 데이터 차례로 꺼내서 출력
# 선입선출(FIFO)를 위해 pop 메서드의 인자로 인덱스 0을 준다.
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

```

<br/><br/>

## ❗ 문제점 : 잘못된 포화상태 인식
배열의 앞부분에 활용할 수 있는 공간이 있음에도, rear = n - 1인 상태 (포화상태)로 인식하여 더 이상 삽입 X

<br/> ➡️ 해결방법
1. 매 연산마다 원소들을 배열의 앞으로 이동시킴 -- 매우 비효율적
2. 원형 큐
> 자료구조 측면에서 이해! 문제풀이에 꼭 사용할 필요는 없음


<br/>

---

## 2️⃣ 원형 큐
- 초기 공백 상태 : front = rear = 0
- 인덱스의 순환 - mod 사용
- front 가 있는 자리는 항상 공백으로 둠


<br/>

---

## 3️⃣ 우선순위 큐
- 우선순위가 높은 순서대로 먼저 나감
- 배열을 이용하여 우선순위 큐 구현 --> 삽입/삭제 연산마다 원소의 재배치 --> 시간 소요, 메모리 낭비
- 배열 + 트리구조

<br/>

---
## 버퍼
- 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역
- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작


- 순서대로 입력/출력/전달되어야 하므로 FIFO 방식의 자료구조인 큐 활용

<br/><br/>

--- 
# BFS (Breadth First Search)
너비 우선 탐색

> 반복

- 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문
- 거리순 탐색

<br/>

1) visited를 True, False로 표현하여 방문 여부 확인
``` python
# 입력 파라미터 : 그래프 G와 탐색 시작점 v

def BFS(G, v):
  visited = [0] * (n + 1)       # n : 정점의 개수
  queue = []                    # 큐 생성
  queue.append(v)               # 시작점 v를 큐에 삽입

  while queue:                  # 큐가 비어있지 않은 경우
    t = queue.pop(0)              # 큐의 첫번째 원소 반환

    if not visited[t]:            # 방문되지 않은 곳이라면
      visited[t] = True             # 방문한 것으로 표시
      visit(t)                      # 정점 t에서 할 일  <- 원하는 코드 

      for i in G[t]:                # t와 연결된 모든 정점에 대해
        if not visited[i]:            # 방문되지 않은 곳이라면
          queue.append(i)               # 큐에 넣기

```


<br/>

2) visited를 숫자로 표현하여 방문 여부 확인 -- 같은 숫자는 같은 우선순위
``` python
# 입력 파라미터 : 그래프 G와 탐색 시작점 v

def BFS(G, v, n):
  visited = [0] * (n + 1)       # n : 정점의 개수
  queue = []                    # 큐 생성
  queue.append(v)               # 시작점 v를 큐에 삽입
  visited[v] = 1
  
  while queue:                  # 큐가 비어있지 않은 경우 (front != rear)
    t = queue.pop(0)              # 큐의 첫번째 원소 반환
    visit(t)
    
    for i in G[t]:                # t와 연결된 모든 정점에 대해
      if not visited[i]:            # 방문되지 않은 곳이라면
        queue.append(i)             # 큐에 넣기
        visited[i] = visited[n] + 1   # n으로부터 1만큼


#   값     A  B  C  D  E  F  G  H  I
# 인덱스  [0][1][2][3][4][5][6][7][8]
# visited  1  2  2  2  3  3  3  3  3    => 같은 값을 가진 원소들끼리는 우선순위 동일 (처리순서 상관 없음)
#    Q     A  B  C  D  E  F  G  H  I
```

