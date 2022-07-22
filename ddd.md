## 표준 입출력

1. 표준 입력 예제 (input)
- **한줄로 받음**
- **문자열로 받음**

### map(function, iterable)

각 원소에 function을 적용<br/>
리스트 뿐만 아니라 문자열에도 적용 가능

- input과 map함수를 이용해 원하는 대로 입력 받기
  
  ```python
  a, b = map(int, input().split())
  ```

a, b, c = map(int, input())
print(a + b + c)

> > > 6

# map 함수는 문자열에도 적용이 가능하기 때문에 답이 6이 됨

```
2. 표준 출력 예제 (print)
- 출력
- 줄 바꿈 발생

- 콤마를 이용해 여러 인자를 넣으면 공백을 기준으로 출력
``` python
a = 'happy'
b = 'day'

print(a, b)
>>> happy day
```

- end= : print의 본질을 바꿈 (줄 바꿈 -> end='' 옵션으로 바꿈)
  
  ```python
  a = 'happy'
  b = 'day'
  ```

print(a, end='@')
print(b)

> > > happy@day

print(a, b, end='@')

> > > happy day@

```
- sep= : 구분자
``` python
a = 'happy'
b = 'day'

print(a, b, sep='\n')
>>> happy
>>> day
```

---

## lambda 함수

- == 익명함수
- 한 줄로 간단히 코드를 표현

```python
# 사용자 지정 함수
def minus_two(x):
    return x - 2

# lambda 함수
minus_two = lambda x: x - 2

result = minus_two(5)
print(result)

# map과 함께 사용 가능
minus_numbers = list(map(lambda x: x - 2, [5, 6]))
print(minus_numbers)
```

---

## 재귀함수 (recursion)

- 함수가 자기 자신을 계속 호출하며 문제를 해결하는 것
- 상위(원래) 문제를 해결하기 위해, 그보다 좁은 범위의 하위 문제를 먼저 해결

팩토리얼 문제

```python
4! = 4 * 3 * 2 * 1
4! = 4 * 3!
3! = 3 * 2!
2! = 2 * 1!
1! = 1

def factorial(n):
  if n <= 1: # 종료 조건
    return 1

  return n * factorial(n - 1) # 자기자신 호출
```

- 모든 재귀는 반복문으로도 표현 가능
- 반복문보다 더 직관적이고 코드가 간결 but 난해
  <br/><br/>
- 재귀함수의 구조
1. 종료 조건
2. 점화식(재귀식) : 재귀 함수를 호출하는 식

---

# 가상환경

--- 

# 이중리스트

= 리스트를 원소로 가지는 리스트

= 행렬

#### 이차원 리스트 순회

###### 1. 이중 for문을 이용한 행 우선 순회

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for i in range(3): # 행
    for j in range(4): # 열
        print(matrix[j][i], end=" ")
    print()
>> 하나의 행을 출력
```

###### 2. 이중 for문을 이용한 열 우선 순회

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for i in range(4): 
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()
```

인덱스의 순서에 따라 출력 다르게 O

###### 3. 행 우선 순회를 이용해 이차원 리스트의 총합 구하기

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

total = 0

for i in range(3): 
    for j in range(4):
        total += matrix[i][j]
    print()

# pythonic하게!
total = sum(map(sum, matrix))
# map함수 ==> matrix 내 각각의 원소에 sum 함수 적용
# 적용한 값을 sum으로 더함
```

>  무조건 pythonic한 방법을 쓰는 것이 좋은 것은 아님!

>  가독성과 이해 가능한지가 더 중요!!!!

---

# 아스키코드

컴퓨터는 숫자만 이해할 수 있음

- 비트 - 0과 1

- 바이트 - 1byte = 8bits

문자를 저장하기 위해서

    ↓

##### 아스키(ASCII) 코드

- 알파벳을 표현하는 대표 인코딩 방식

###### ord(문자)

- 문자 -> 아스키코드로 변환하는 내장함수 

###### chr(아스키코드)

- 아스키코드 -> 문자로 변환하는 내장함수

---

## 파일 입출력

open(file, mode='r', encoding=None)

파일이름을 문자열로 받음 ==> 'sample.json'     # 상대 경로

encoding = 'uft-8'

json -- 딕셔너리와 형태 유사

json.load ==>  json -> dict

pprint -- 출력 가독성 증가

from pprint import pprint

if __name __ =='____main____':

--> 직접 실행 시에만 실행 (불러오기 시에는 실행 X)
