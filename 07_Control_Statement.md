# Today I Learned

## 제어문 (Control Statement)
- 조건문
- 반복문
<br/><br/>
---

# 조건문
## 1. 기본 조건문
- 참 / 거짓에 대한 조건식<br/><br/>
 <img width="350" src= https://i.esdrop.com/d/f/GQtKpTuAPv/6iRf2hahKu.png alt="조건문">

``` python
if 조건:
    참인 경우 실행 코드
else:
    거짓인 경우 실행 코드
```
<br/><br/>
- <예시>
``` python
if a % 2:
  print('홀수')
else:
  print('짝수')
```
- a % 2 는 조건이 아님 But 파이썬이 알아서 그 값을 논리값으로 변경 
  - 0 = falsy
  - 즉, 조건이 거짓이라고 판단
  
<br/><br/>

## 2. 복수 조건문
``` python
if 조건1:
    조건1이 참일 경우 실행 코드
elif 조건2:
    조건2가 참일 경우 실행 코드
elif 조건3:
    조건3이 참일 경우 실행 코드
else:
    모두 거짓일 경우 실행 코드
```

> 조건식을 동시에 검사하는 것이 아니라 순차적으로 비교


> 조건 쓸 때 if-elif 조건이 서로 배타적이어야 함

<br/><br/>

## 3. 중첩 조건문
- 조건문 안의 조건문
``` python
if 조건1:
    if 조건2:
        두가지 조건 모두 참일 경우 실행 코드
else:
    조건1이 거짓일 경우 실행 코드
```
<br/><br/>
## 4. 조건 표현식
- 일반적으로 조건에 따라 값을 정할 때 활용
- = 삼항 연산자
> `true인 경우 값 if 조건 else false인 경우 값`

<br/><br/>

---
# 반복문
- 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용<br/><br/>
 <img width="350" src= https://i.esdrop.com/d/f/GQtKpTuAPv/G666RBqMpJ.png alt="반복문">

<br/><br/>

## 1. while문
- 조건식이 참인 경우 반복적으로 코드 실행
``` python
while 조건:
    참일 경우 실행하는 코드
```
  1.  O/X
  2.  코드 실행
  3.  O/X
  4.  반복하기
- 종료 조건에 해당하는 코드를 통해 반복문 종료
- **while문은 무한 루프를 하지 않도록 종료 조건이 반드시 필요!!!**<br/><br/>
#### 복합 연산자
- 연산 + 할당
`a += 1`

<br/><br/>

## 2. for문
- 시퀀스를 포함한 순회 가능한 객체의 요소를 모두 순회
- 반복가능한 객체를 모두 순회하면 종료 -> 별도의 종료 조건 X<br/><br/>
-  iterable
   - 순회할 수 있는 자료형 : string, list, dict, tuple, range, set 등
   - 순회형 함수 : range, enumerate <br/><br/>


- 딕셔너리는 기본적으로 key를 순회, key를 통해 값을 활용
  - 추가 메서드 활용
    - keys() : key로 구성된 결과
    - values() : value로 구성된 결과
    - items() : (key, value)의 튜플로 구성된 결과<br/><br/>

- **enumerate 순회**
  - (index, value) 형태의 튜플로 구성된 열거형 객체 반환
  - 카운트 (시작:0 -> 수정 가능)
``` python
a = [1, 2, 3, 4, 5]
for i in range(len(a)):
  print(f'현재 {i}번째 데이터는 {a[i]}이다')

를 pythonic 하게 바꾸면

for i, v in enumerate(a):
  print(f'현재 {i}번째 데이터는 {v}이다')
```
<br/><br/>
- **List Comprehension** -- 축약문법과 비슷
  - `[code for 변수 in iterable]`
  - `[code for 변수 in iterable if 조건식]`
<br/><br/>
- Dictionary Comprehension
  - `{key: value for 변수 in iterable}`
  - `{key: value for 변수 in iterable if 조건식}`

<br/><br/>

## 3. 반복문 제어
<br/>
 <img width="400" src=https://i.esdrop.com/d/f/GQtKpTuAPv/N0nJ0466ce.png alt="반복문제어">
<br/><br/>
1. break
- 반복문 종료<br/><br/>

2. continue
- continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행 (스킵, 건너뛰기)
``` python
while a < 5:
  if a == 3:
    continue
  print(a)
  a += 1
```
> a == 3을 벗어날 수 없어 무한루프에 갇히게 됨

<br/>

``` python
for a in range(5):
  if a == 3:
    continue
  print(a)
  a += 1
```
> 종료조건(a in range(5))이 있기 때문에 무한루프 X

<br/>

3. pass
- 아무것도 하지 않음 (문법적으로 필요 But 할 일이 없을 때)
- 반복문 아니어도 사용 가능
- 코드 테스트할 때<br/><br/>

4. else
- 끝까지 반복문을 실행한 후 else문 실행
- break를 통해 중간에 종료되는 경우 else문 실행 X
``` python
for a in range(5):
  print(a)
else:
  print('for문이 정상적으로 다 돌아야만 else문 실행')
```