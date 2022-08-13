# Today I Learned
1. [디버깅](#1-디버깅)
2. [문법 에러](#2-문법-에러-syntax-error)
3. [예외](#3-예외-exception)
4. [예외 처리](#4-예외-처리)



<br/>

---
## 1. 디버깅
### ▶️ 버그 : 소프트웨어에서 발생하는 문제
### ▶️ 디버깅 : 잘못된 프로그램을 수정하는 것
- 에러 메시지가 발생하는 경우
- 로직 에러 (오류는 없지만 결과물이 다른 경우)
<br/>

✔️ 버그가 많이 발생하는 곳 --> 제어가 되는 시점 (조건/반복, 함수)
<br/>
  
- 디버깅 방법
  - print 함수 활용
  - 개발 환경에서 제공하는 기능 활용
  - python tutor 활용
  - 뇌컴파일, 눈디버깅

<br/>

---
## 2. 문법 에러 (Syntax Error)
- 파이썬 프로그램 실행 X
- Invalid syntax : 문법 오류
- assign to literal : 잘못된 할당
- EOL (End of Line)
- EOF (End of File)

<br/>
---

## 3. 예외 (Exception)
- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행 멈춤
- 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
<br/>

- ZeroDivisionError : 0으로 나눌 수 없는데 0으로 나눴을 때
- NameError : namespace 상에 이름이 없는 경우
- TypeError
  - 타입 불일치
  - argument 누락
  - argument 개수 초과
  - argument type 불일치
- ValueError : 값이 적절하기 않거나 없는 경우
- IndexError : 인덱스가 존재하지 않거나 범위를 벗어나는 경우
- KeyError : 해당 키가 존재하지 않는 경우 (-> 대신 get 메서드 활용 O)
- ModuleNotFoundError : 설치가 잘 안 됐거나, 가상환경 문제
- ImportError : 모듈은 있으나 존재하지 않는 클래스/함수를 가져오는 경우
- KeyboardInterrupt : 임의로 프로그램을 종료하였을 때 (ctrl + c)
- IndentationError : 들여쓰기 문제

<br/>

---

## 4. 예외 처리

- try문 (시도, 실행)
  - 오류가 발생할 가능성이 있는 코드 실행
  - 예외 발생 X -> except 없이 실행 종료
<br/>

- except문
  - 예외 발생 시 실행
  - 예외 처리 코드
<br/>

❗ try문은 반드시 한 개 이상의 except문 필요
<br/>

- 에러 메시지 처리 (as)
  - 발생 가능한 에러를 모두 명시
  - 에러 별로 별도의 에러처리
  - 순차적 수행 -> 가장 작은 범주부터 예외 처리 해야 함

- else문
  - 예외 발생 X 시 실행

- finally문
  - 예외 발생 여부와 관계없이 항상 실행

