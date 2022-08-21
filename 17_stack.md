# Today I Learned
- [스택 (Stack)](#스택stack)
- [DP (Dynamic Programming)](#dp-dynamic-programming)



<br/><br/>
--- 

# 스택(stack)

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 선형 구조 : 자료 간의 관계가 1대 1
- 자료를 삽입하거나 꺼낼 수 있음
- 후입선출 : 마지막에 삽입한 자료를 가장 먼저 꺼냄
 #### 🔗 [stack.py](https://github.com/Yonghyunc/TIL/blob/master/code/stack.py)
<br/><br/>

## 스택 구현
스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산
<br/>

- 자료구조 : 자료를 **선형**으로 저장할 저장소
  - 배열 O
  - 저장소 자체를 스택이라 부르기도 함
  - 마지막 삽입된 원소의 위치 == **top**
<br/>

- 연산
  - 삽입 : 저장소에 자료 저장 == push
  - 삭제 : 저장소에서 자료 꺼냄 (삽입의 역순)  == pop
  - isEmpty : 스택이 공백인지 아닌지 확인
    - 비어있으면 True
    - 비어있지 않으면 False
  - peek : 스택의 top에 있는 원소 반환
<br/><br/>

### 스택의 삽입/삭제 과정
push ==> top ++ (탑 증가) // stack[top] <- A
<br/>

## 스택의 push 알고리즘
- append 메서드를 통해 리스트의 마지막에 데이터 삽입
> append 메서드는 느림,,,
``` python
def push(item):
  s.append(item)
```
크기가 정해져있는 스택을 만드는 것이 일반적
``` python
# 형식을 갖춰서 구현
def push(item, size):
  global top
  top += 1
  if top == size:
    print('overflow!') # 디버깅용
  else:
    stack[top] = item

# 크기가 정해진 배열과 top포인터를 사용하는 것을 권장
size = 10
stack = [0] * size
top = -1

push(10, size)
# 아래처럼 풀어서도 구현 가능
top += 1
stack[top] = 20
```

> overflow 오류
>> stack을 너무 작게 만들었거나
>> 너무 push를 많이 함

<br/>

## 스택의 pop 알고리즘
``` python
def pop():
  if len(s) == 0:
    # underflow -- 더이상 스택에서 꺼낼게 없음 (디버깅용)
    return
  else:
    return s.pop(-1)
```

``` python
def pop():
  global top
  if top == -1:
    print('underflow') # 디버깅용
    return 0
  else:
    top -= 1
    return stack[top + 1]

print(pop())

if top > -1:
  top -= 1
  print(stack[top])
```
 #### 🔗 [stack1_stack.py](https://github.com/Yonghyunc/TIL/blob/master/code/stack1_stack.py)


<br/>

 ### 스택 구현 고려 사항
 - 1차원 배열을 사용하여 구현할 경우 구현 용이 But 스택 크기 변경 어려움
> 문제풀이 -> 크기 예측
- 해결 위해 => 저장소를 동적으로 할당하여 스택 구현 (동적 연결리스트)

<br/><br/>

---

## 스택 응용1 : 괄호검사
괄호검사 알고리즘 개요
- 문자열에 있는 괄호를 차례대로 조사하면서 왼쪽 괄호를 만나면 스택에 삽입하고, 오른쪽 괄호를 만나면 스택에서 top 괄호를 삭제한 후 오른쪽 괄호와 짝이 맞는지 검사
- 스택이 비어 있거나, 괄호의 짝이 맞지 않거나, 마지막 괄호까지 조사한 수에도 스택에 괄호가 남아 있으면 실패

#### 🔗 [stack_괄호매칭.py](https://github.com/Yonghyunc/TIL/blob/master/code/stack_%EA%B4%84%ED%98%B8%EB%A7%A4%EC%B9%AD.py)


<br/>

## 스택 응용2 : function call 
- 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리

#### 🔗 [function_call.py](https://github.com/Yonghyunc/TIL/blob/master/code/function_call.py)

<br/>
---

### 재귀호출
실제 동작 -> 이동
- 자기 자신을 호출하여 순환 수행되는 것
- 일반적인 호출방식보다 프로그램의 크기를 줄이고 간단하게 작성 가능

``` python
# 피보나치 수를 구하는 재귀함수

def fibo(n):
  if n < 2 :
    return n
  else:
    return fibo(n - 1) + fibo(n - 2)
```



<br/><br/>

---
## Memoization
중간값을 어떻게 저장하지?
0(2^n) -- 기하급수적으로 증가

- 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 함
- 동적 계획법의 핵심

``` python
# memo를 위한 배열을 할당하고, 모두 0으로 초기화
# memo[0]을 0으로 memo[1]는 1로 초기화

def fibo1(n):
  if n >= 2 and len(memo) <= n:
    memo.append(fibo1(n-1) + fibo1(n-2))
  return memo[n]

memo = [0, 1]
```

<br/><br/>

---
# DP (Dynamic Programming)
동적 계획 알고리즘
- 최적화 문제 해결 알고리즘
- 작은 부분 문제들을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제 해결

``` python
# 피보나치 수 DP 적용 알고리즘

def fibo2(n):
  f = [0, 1]

  for i in range(2, n + 1):
    f.append(f[i - 1] + f[i - 2])
```


<br/><br/>

--- 
## DFS (깊이우선탐색)