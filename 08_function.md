# Today I Learned





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

<br/><br/>

### 2. 두 개 이상의 값 반환
- return은 항상 하나의 값 만을 반환<br/>
↓
- 반환 값으로 튜플 사용

<br/><br/>

---
## 함수의 입력
> parameter -- 변수로 사용<br/>
> argument -- 실제로 호출

<br/><br/>

### 1. argument : 함수 호출 시 함수의 parameter를 통해 전달되는 값
   - 필수
   - 선택 : 기본값 전달

### 2. positional arguments 
- 기본적으로 위치에 따라 함수 내에 전달됨
### 3. keyword arguments 
- 직접 어떤 parameter에 어떤 argument 넣을지 지정
> 위치 인자, 키워드 인자 함께 사용 O<br/>
> But, 키워드 → 위치 인자 순서는 불가 (무조건 위치가 먼저)

### 4. default arguments values 
- 기본값 지정

### 5. 정해지지 않은 여러 개의 arguments 처리
