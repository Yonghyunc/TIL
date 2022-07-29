# Today I Learned
1. [함수](#함수)
2. [함수의 결과값](#함수의-결과값)
3. [함수의 입력](#함수의-입력)
4. [Python의 범위](#python의-범위-scope)
5. [함수 응용](#함수-응용-)


--- 
## 함수
= 미니 프로그램
- Decomposition (분해)
  - 기능을 분해하고
  - 재사용 가능하게 만들고
- Abstraction(추상화)
  - 원리를 잘 모르더라도 사용할 수  있도록
  - **재사용성**, 가독성, 생산성
<br/><br/>

## 1. 함수의 종류
1. 내장함수 
     - 파이썬 개발자 (자동설치)
2. 외장함수
     - 다른 개발자 (import) 
3. 사용자 정의 함수
     - 내가 만든
<br/><br/>

## 2. 함수의 정의
함수 = 특정한 기능을 하는 코드의 조각 (즉, 미니 프로그램)

 <img width="300" src= https://i.esdrop.com/d/f/GQtKpTuAPv/wGhQwSEzCz.jpg alt="함수">
<br/><br/>

## 3. 함수 기본 구조
함수를 사용하기 위해서는 먼저 함수를 정의해야 함
1. 선언과 호출 (define & call)
   - 선언 = 생성
   - 호출 = 사용
   - def 키워드 활용
   - 들여쓰기를 통해 실행 코드 작성
   - 함수는 **parameter**를 넘겨줄 수 있음
   - 동작 후 **return**을 통해 결과값을 전달
2. 입력 (Input)
3. 문서화 (Docstring)
4. 범위 (Scope)
5. 결과값 (Output)


<br/><br/>

---
## 함수의 결과값
- 출력
- 줄 바꿈 발생
<br/><br/>

### 1. 값에 따른 함수의 종류
- Void function
  - return 값 X, None을 반환하고 종료
- Value returning function
  - return문을 통해 값 반환
  - return을 하개 되면, 값 반환 후 함수 바로 종료

<br/><br/>
>**return vs. print**<br/>
print : 호출될 때마다 값이 출력됨<br/>
return : 데이터 처리위해 사용 (결과값 다시 사용 가능)
<br/>

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

<br/><br/>

### 2. 두 개 이상의 값 반환
- return은 항상 하나의 값 만을 반환<br/>
↓
- 반환 값으로 튜플 사용

<br/><br/>

---
## 함수의 입력
- **한줄로 받음**
- **문자열로 받음**
> parameter -- 변수로 사용<br/>
> argument -- 실제로 호출

<br/>

### 1. argument : 함수 호출 시 함수의 parameter를 통해 전달되는 값
   - 필수 : 없으면 에러
   - 선택 : 값을 전달하지 않아도 되는 경우 기본값 전달

### 2. positional arguments 
- 기본적으로 위치에 따라 함수 내에 전달됨 (순서대로!)
### 3. keyword arguments 
- 직접 변수의 이름으로 특정 argument 전달
> 위치 인자, 키워드 인자 함께 사용 O<br/>
> But, 키워드 → 위치 인자 순서는 불가 (무조건 위치가 먼저)

### 4. default arguments values 
- 기본값 지정

### 5. 정해지지 않은 여러 개의 arguments 처리
> \* : 애스터리스크(Asterisk) = 언패킹 연산자

- 가변 인자 (*args)
  - 여러 개의 위치 인자를 하나의 필수 파라미터로 받아서 사용 <br/><br/>

- 가변 키워드 인자 (*kwargs)
  - 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때
  - 딕셔너리로 묶여 처리됨 <br/><br/>

- 가변 인자 + 가변 키워드 인자 동시 사용 O

<br/>

### 6. 패킹 / 언패킹
패킹 : 여러 개의 데이터를 **묶어서** 변수에 할당<br/>
언패킹 : 시퀀스 속의 요소들을 여러 개의 변수에 **나누어** 할당
- 변수의 개수와 할당 요소들의 개수가 동일해야 함
- \* : 할당하고 남은 요소를 리스트에 담기 가능

    ```python
    numbers = (1, 2, 3, 4, 5)
    a, b, *rest = numbers

    >>> 1 2 [3, 4, 5]
    ```

<br/><br/>

---
## Python의 범위 (Scope)
#### Scope
- global scope : 코드 어디에서든 참조(사용)할 수 있는 공간
- local scope : 함수 내부에서만 참조 가능 <br/><br/>

#### Variable
- global variable
- local variable
<br/><br/>

### 1. 변수 수명주기
- built-in Scope : 파이썬이 실행된 이후부터 영원히 유지
- global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지
- local scope : 함수 호출 때 생성, 함수가 종료될 때까지

<br/>

### 2. 이름 검색 규칙
- 파이썬에서 사용되는 이름들은 이름공간에 저장되어 있음
- **LEGB Rule**

  <img width="300" src= https://i.esdrop.com/d/f/GQtKpTuAPv/EdxCVrkCDu.png alt="LEGB"> <br/>
- 함수 내에서는 바깥 scope의 변수에 접근 가능 But 수정 불가

<br/>

### 3. global문
- 현재 코드 블록 전체에 적용
- 파라미터, for 루프 대상, 클래스/함수 정의 등을 글로벌로 X

<br/>

### 4. nonlocal
- global을 제외하고 가장 가까운 scope의 변수 연결
- - 파라미터, for 루프 대상, 클래스/함수 정의 등으로 정의 X
- 이름공간 상에 존재하는 변수만 가능 (선언된 적 없는 변수 X)

<br/>

## 함수 범위 주의
- 기본적으로 함수에서 선언된 변수는 local scope에 생성되며, 함수 종료 시 사라짐
- 해당 scope에 변수가 없는 경우 LEGB에 의해 이름 검색
  - 변수 접근 가능 but 수정 불가
  - 값을 할당하는 경우 해당 scope의 이름공간에 새롭게 생성되기 때문
  - **단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것**
- 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드 활용 가능
  - 단, 코드가 복잡해지면서 변수 변경 추적이 어렵고, 오류 발생 가능성
  - **함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 return 값을 사용 하는 것을 추천**

<br/><br/>

---
## 함수 응용 <br/><br/>
## 1. 내장 함수
1. map(function, iterable)
- 각 원소에 function을 적용
- 리스트 뿐만 아니라 문자열에도 적용 가능
<br/>

- input과 map함수를 이용해 원하는 대로 입력 받기
``` python
a, b = map(int, input().split())

a, b, c = map(int, input())
print(a + b + c)
>>> 6

# map 함수는 문자열에도 적용이 가능하기 때문에 답이 6이 됨
```
<br/><br/>

2. filter(function, iterable)
- 각 원소에 function을 적용하고, 그 결과가 True인 것들을 반환
<br/>

3. zip(*iterables)
- 복수의 iterable를 모아 튜플을 원소로 하는 zip object를 반환

<br/><br/>

## 2. lambda 함수
- == 익명함수
- 한 줄로 간단히 코드를 표현
- Return문, 조건문, 반복문을 가질 수 없음 (간편 조건문 O)

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

<br/><br/>

## 3. 재귀 함수
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
<br/><br/>

--- 

## 모듈 <br/>
- 다양한 기능을 하나의 파일로 → **모듈** 
- 다양한 파일을 하나의 폴더로 → **패키지** 
- 다양한 패키지를 하나의 묶음으로 → **라이브러리**
- 이것을 관리하는 관리자 → **pip** 
- 패키지의 활용 공간 → **가상환경**
<br/><br/>

### 모듈과 패키지 불러오기
``` python
import module
from module import var, function, class
from module import *

from package import module
from package.module import var, function, class

# 외부 개발자가 만든 코드를 가져다 쓰기 위해
```
<br/>

### 파이썬 패키지 관리자(pip)
- Pip에서 설치하고 import해서 쓴다!!

<br/>

### 가상환경
-	외부 패키지와 모듈을 사용하는 경우, 모두 pip를 통해 설치를 해야 함
-	가상 환경을 만들고 관리하는데 사용되는 모듈 
-	각 프로젝트별 가상환경 (Venv 폴더별로 고유한 프로젝트가 설치됨)
-	<venv>는 가상환경을 포함하는 디렉토리의 경로




