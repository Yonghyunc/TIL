# Today I Learned

1. [객체지향 프로그래밍 (OOP)](#1-객체지향-프로그래밍-oop)
2. [객체지향 프로그래밍이 필요한 이유](#2-객체지향-프로그래밍이-필요한-이유❓)
3. [OPP 기초](#3-opp-기초)
4. [객체와 클래스 문법](#4-객체와-클래스-문법)
5. [OOP 속성](#5-oop-속성)
6. [OOP 메서드](#6-oop-메서드)
7. [객체 지향의 핵심 개념](#7-객체-지향의-핵심-개념)


<br/>

---

# 1. 객체지향 프로그래밍 (OOP)
### ⭐**확장성**⭐
- 컴퓨터 프로그래밍의 패러다임(방법론) 중 하나
  - 즉, 프로그램을 만드는 하나의 방법


> 객체 = 정보 + 행동 = 변수 + 함수
- 프로그램을 여러 개의 독립된 개체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍


<br/><br/>

### 프로그램 : 기능 vs. 구조  
  - 기능 -> 절차지향
  - 구조 -> 객체지향

<br/>

### ▶️ 절차지향 프로그래밍
문제점 : 하나를 바꾸면 여러 부분을 연달아 바꿔야 함 (즉, 원하는 부분만 수정 불가능)
 <br/> ⬇️ <br/>

 특정 기준에 맞춰 서로 다른 객체가 주고받도록 <br/>
 데이터와 기능(메서드) 분리 <br/>
 추상화된 구조(인터페이스)

<br/><br/>

---

# 2. 객체지향 프로그래밍이 필요한 이유❓
현실세계 너무 복잡 -> 추상화 (복잡한 건 숨기고 필요한 것만 드러내는 것)

### ⭕장점
- 클래스 단위로 모듈화 (각각 역할 단위로 분리하여 사용) -> 협업 수월
- 필요한 부분만 수정 가능 -> 프로그램 유지보수가 쉬움


### ❌단점
- 설계 시 많은 노력과 시간 필요
- 실행 속도가 상대적으로 느림 (사람이 편하면 컴퓨터가 힘들다...)

<br/><br/>

---

# 3. OPP 기초

## 📌**객체(object)**
**속성**과 **행동**으로 구성된 모든 것 
<br/>

클래스(설계도) -> 객체(실제 사례)
<br/><br/>

- 역할 : 책임에 대한 메타 정보
- 책임 (행위) - 메서드 호출
- 협력   <br/>
--> 객체끼리 서로 요청, 응답

<br/>

### 객체는 특정 타입의 인스턴스
-	1, 200, 5는 모든 int의 인스턴스
-	‘hello’, ‘bye’는 모두 string의 인스턴스
-	[1, 2, 3], []은 모두 list의 인스턴스

<br/>

### 객체의 특징
- 타입(type) : 어떤 연산자와 조작이 가능한가?
- 속성(attribute) : 어떤 상태(데이터)를 가지는가?
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

### **객체 = 속성(상태, 정보) + 기능**

<br/>

## 📌**인스턴스**
클래스로 만든 객체 - 타입/클래스의 인스턴스 (종속)
<br/>
   - 클래스 : 강아지 <br/>
   - 리트리버는 객체다(O) <br/>
   - 리트리버는 인스턴스다(X) <br/>
   - 리트리버는 강아지의 인스턴스다(O)
<br/><br/>



## 📌**클래스** == 타입 
객체를 만드는 도구 (설계도) <br/>

클래스를 만든다 == 타입을 만든다 <br/>
### 왜 클래스가 타입일까?
- 개별 객체를 하나의 타입으로 보는 것(추상화)
- 각각의 개별 존재 -> 하나의 클래스 == 타입

<br/>
  <img width="250" src=https://i.esdrop.com/d/f/GQtKpTuAPv/Ce1fMa2siW.png alt="인스턴스_클래스">
<br/>

**파이썬은 모든 것이 객체** (모든 것에 속성과 행동이 존재) 

<br/>


<br/><br/>

---

# 4. 객체와 클래스 문법
## 기본 문법
- 클래스 정의 : `class MyClass:`
- 인스턴스 생성 : `my_instance = MyClass()`
- 메서드 호출 : `my_instance.my_method()`
- 속성 : `my_instance.my_attribute`

**파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스**
<br/>

### 객체 비교하기
- ==
  - 동등한(equal) - 값이 같은지
  - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
- is
  - 동일한(identical) - id 값이 같은지
``` python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b, a is b)  # True False

a = [1, 2, 3]
b = a
print(a == b, a is b)  # True True
```
<br/><br/>

---

# 5. OOP 속성

1. 속성
- 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터
- 클래스 변수/인스턴스 변수 존재
<br/>

2. 인스턴스 변수
- 인스턴스가 개인적으로 가지고 있는 속성
- 각 인스턴스들의 고유한 변수
- 생성자 메서드(__init__)에서 self.<name>으로 정의
- <instance>.<name>으로 접근, 할당

``` python
class Person:
  def __init__(self, name):
    self.name = name

john = Person('john')
print(john.name)  # john
john.name = 'John Kim'
print(john.name)  # John Kim
```
<br/>

3. 클래스 변수
- 한 클래스의 모든 인스턴스가 공유하는 값
- 클래스 선언 내부에서 정의
- <classname>.<name> = 클래스이름.클래스변수
- 인스턴스를 통해서도 접근 O -> 인스턴스.클래스변수
<br/>

``` python
class Circle():
  pi = 3.14  # 클래스 변수 정의

  def __init__(self, r):
    self.r = r  # 인스턴스 변수

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi)  # 3.14
print(c1.pi)  # 3.14
print(c2.pi)  # 3.14

Circle.pi = 5  # 클래스 변수 변경
print(Circle.pi)  # 5
print(c1.pi)  # 5
print(c2.pi)  # 5
```
<br/>
❗ 클래스 변수 변경 시, 무조건!!! 클래스.클래스변수 형식으로 변경

``` python
c2.pi = 5  # 인스턴스 변수 변경
print(Circle.pi)  # 3.14 (클래스 변수)
print(c1.pi)  # 3.14 (클래스 변수)
print(c2.pi)  # 5 (새로운 인스턴스 변수가 생성됨)
```

### 인스턴스와 클래스 간의 이름 공간
= 함수의 scope
- 인스턴스 만들었을 때, 
  - 인스턴스 변수가 있으면 그대로 사용
  - 없으면 클래스 변수 호출

<br/><br/>


---

# 6. OOP 메서드

### **메서드**
- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
- 클래스 안에 있는 함수 -- 괄호 존재
<br/>
< 종류 > <br/>
1. 인스턴스 메서드 -> 인스턴스 처리 (개별 행동) <br/>
2. 클래스 메서드 -> 클래스 처리 <br/>
3. 스태틱 메서드 -> 나머지

<br/><br/>

## 1. 인스턴스 메서드
- 인스턴스 변수 사용 / 인스턴스 변수에 값 설정
-	클래스 내부에 정의되는 메서드의 기본

<br/>

### 1. self 
- 인스턴스 메서드에서 무조건 첫번째 인자!! (인스턴스 자기자신)

<br/>

### 2. 생성자 메서드 (__init__)
- 괄호 안에 argument를 넣어주면 두번째 parameter로 들어감 (첫번째는 무조건 self)

<br/>

### 3. 매직 메서드
- Double underscore(__) == 던더 == 스페셜 메서드
- 특수한 동작을 위해 만들어진 메서드
- 특정 상황에서 자동으로 불림


``` python
class Person:
  def __init__(self, name):
    self.name = name

person1 = Person('조용현')
# person1은 객체이자, Person의 인스턴스
# '조용현'은 name으로 들어감

print(person1)  # <__main__.Person object at 0x000001A61DDC5DF0>
```
⬇️ <br/>

``` python
# 이름을 보이게 하고 싶음 --> 매직 메서드 사용
class Person:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

person1 = Person('조용현') 

print(person1)  # 조용현
```

``` python
class Person:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def __add__(self, other):
    return self.name + other.name

person1 = Person('조용현')
person2 = Person('아리가지')

print(person1 + person2)  # 조용현아리가지
```

<br/>

## 4. 소멸자 메서드
- 인스턴스 객체가 소멸되기 직전에 호출되는 메서드


``` python
class Person:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def __del__(self):
    print("삭제되었습니다")


person1 = Person('조용현')
del person1
print(person1.name)

# 오류 name 'person1' is not defined
```

``` python
person1 = Person('조용현')
person2 = person1
print(id(person), id(person2))  # 아이디 같음
del person1
print(person2.name)
# 조용현
# 삭제되었습니다

# 1. 오류메시지가 안 뜨는 이유?

# 2. print가 "삭제되었습니다"보다 먼저 나오는 이유?

## del 키워드는 객체를 지우는 게 아니라, 변수가 객체를 가르키는 참조값을 없앰 (포스트잇을 뗀다)

# 즉, 
# 같은 객체에 person1, person2 포스트잇이 붙어있음
# del person1 -- person1 포스트잇이 떼어짐
# print() -- (객체가 가르키는) 변수 출력
```
<br/><br/>

## 2. 클래스 메서드
- 클래스가 사용할 메서드
- @classmethod 데코레이터 반드시 사용!!
- 첫번째 인자 == cls
<br/>

- 클래스 내 속성을 활용할 때
- 클래스는 인스턴스 변수 사용 불가 (인스턴스 - 가능 O but 조회만)

- 웬만하면 인스턴스 메서드, 클래스 메서드를 써야할 때만..!

- 속성을 다루지 않고 단지 기능만 다룰 때

### 데코레이터 : 함수를 어떤 함수로 꾸며서 기능을 부여

``` python
def add_print(original): # 파라미터로 함수를 받음
  def wrapper():
    print('함수 시작')
    original()
    print('함수 끝')
  return wrapper

@add_print
def print_hello():
  print('hello')

print_hello()
# '함수 시작'
# 'hello'
# '함수 끝'
```

> **클래스 메서드 vs. 인스턴스 메서드**
> - 클래스 메서드 -> 클래스 변수 사용 (cls)
> - 인스턴스 메서드 -> 인스턴스 변수 사용 (self)
>
> 둘 다 쓰고 싶다면?
> - 클래스 메서드 : 인스턴스 변수 사용 불가
> - 인스턴스 메서드 : 둘 다 사용 가능 ✔️

<br/><br/>

## 3. 스태틱 메서드
- 항상 고정된 값이 들어갈 때 (self, cls 필요 없을 떄)
- @staticmethod 데코레이터 사용하여 정의


``` python
class Person:

  def __init__(self, name):
    self.name = name

  def call_name(self):  # 무조건 self 를 가지고 있어야만 출력 가능
    return f'대전 2반 {self.name} 입니다!'

  @staticmethod
  def hello(): # self를 굳이 가지고 있을 필요 없을 때 
    return '안녕하세요!'

person1 = Person('조용현')
print(person1.call_name())  # 대전 2반 조용현 입니다!
print(person1.hello()) # 안녕하세요!
```


<br/><br/>

---

# 7. 객체 지향의 핵심 개념
1. 추상화
2. 캡슐화
3. 다형성
4. 상속

<br/><br/>

## 1. 추상화
- 불필요한 세부사항은 걷어내고, 중요한 것에만 초점을 맞춤
- 객체들이 소통했을 때 서로의 기능 몰라도 됨 -- 답만 나오면 됨
- ex) 카페를 가서 커피를 주문했을 떄, 바리스타가 원두 몇알을 넣고, 어떤 기계를 사용하는지 관심 X

<br/><br/>

## 2. 캡슐화
- 다른 객체는 내부의 행위에 관여할 수 X <-- 알 필요가 없으니(추상화)
- 바꾸면 안 되는 것을 바꾸거나, 오류 났을 때를 방지하기 위해 건드리면 안될 코드 표시
- 캡슐로 싸놓는다는 뜻
- 객체에게 자율성 부여
- public / protected / private


``` python
class Player:
    def __init__(self):
        self.sea = [0] * 15
        self.attacked = [False] * 15

    def set_ship(self, index):
        for j in range(3):
            self.sea[index + j - 1] = 1

me = Player()
me.set_ship(1) # 요청만

# me 객체가 바꾸는 것이 아니라 Player 내부에서 바꿈 -- Player 객체에 자율성 부여
```
<br/>

- Public Member
  - 어디에서나 호출 가능
  - 가장 일반적

<br/>

- Protected Member
  - 언더바 1개
  - 느슨하게 제한 (권장사항) - 문법적으로 O , 암묵적으로 X


<br/>

- Private Member
  - 언더바 2개
  - 강하게 제한
  - 자기자신 안에서만 실행 O
  - 바뀐 이름으로 접근 가능 But 암묵적으로 X


<br/>

### ▶️ getter (조회)

``` python
class Person:
  counts = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_age(self):
    return self.__age

person1 = Person('조용현', 25)
print(person1.get_age())  # 25
# 호출로 인한 응답을 출력
```


### ▶️ setter (변경)
- set해달라고 물어보기


``` python
class Person:
  counts = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    self.__age = age  # 요청할 때 넣은 argument

person1 = Person('조용현', 25)
print(person1.get_age())  # 25

person1.set_age(20)
print(person1.get_age())  # 20

# 객체에 요청 메시지를 보내면, 요청에 맞는 함수를 찾아 응답을 줌
```




#### 편하게 쓰면서 getter와 setter의 기능을 사용하기 위해 ==> property객체

``` python
class Person:

  def __init__(self, age):
    self.age = age

  @property  # getter
  def age(self):
    return self._age

  @age.setter 
  def age(self, new_age):
    if new_age <= 19:
      raise ValueError('Too Young For SSAFY')
      return
    
    self._age = new_age
```

<br/><br/>

## 3. 다형성
- 어떤 객체라도 상관 없음 -- 결과만 잘 받으면 됨
- 다른 객체이더라도 내가 요청을 보냈을 때 동일한 응답이 오면 OK
- 관심X (추상화) -> 간섭X (캡슐화) -> 누구라도 상관X
- 
<br/>

### ▶️ 메서드 오버라이딩
- 상속받은 메서드를 재정의 (덮어쓰기)
- 특정 기능만 바꿀 떄 


<br/><br/>

## 4. 상속
- 객체의 공통점 = 하나의 클래스로부터 받음 --> 당연히 상속 가능
- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계, 제약 조건을 모두 상속 받음
- 메서드 재사용


<br/><br/>

---



