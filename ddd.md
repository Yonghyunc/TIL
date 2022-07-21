## 표준 입출력
1. 표준 입력 예제 (input)
- **한줄로 받음**
- **문자열로 받음**

### map(function, iterable)
각 원소에 function을 적용<br/>
리스트 뿐만 아니라 문자열에도 적용 가능

- input과 map함수를 이용해 원하는 대로 입력 받기
``` python
a, b = map(int, input().split())

a, b, c = map(int, input())
print(a + b + c)
>>> 6

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
``` python
a = 'happy'
b = 'day'

print(a, end='@')
print(b)
>>> happy@day

print(a, b, end='@')
>>> happy day@
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

``` python
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

``` python
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
