# 객체지향 프로그래밍 -> 확장성
#### 객체가 가장 중요!!

- 프로그램 : 기능 vs. 구조  
  - 기능 -> 절차지향
  - 구조 -> 객체지향


### 클래스
- 객체를 만드는 도구 (설계도)


### 객체
- 역할 : 책임에 대한 메타 정보
- 책임 (행위) - 메서드 호출
- 협력 

> --> 객체끼리 서로 요청, 응답



# 객체지향의 4대 특징
## 1. 추상화
- 불필요한 세부사항은 걷어내고, 중요한 것에만 초점을 맞춤
- (정확한 원리를 몰라도 사용 가능)
- 객체들이 소통했을 때 서로의 기능 몰라도 됨 -- 답만 나오면 됨
- ex) 카페를 가서 커피를 주문했을 떄, 바리스타가 원두 몇알을 넣고, 어떤 기계를 사용하는지 관심 X


## 2. 캡슐화
- 다른 객체는 내부의 행위에 관여할 수 X -- 알 필요가 없으니(추상화)
- 캡슐로 싸놓는다 == 
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
- getter : 객체의 속성 조회
- setter : 변경



## 3. 다형성
- 어떤 객체라도 상관 없음 -- 결과만 잘 받으면 됨
- 다른 객체이더라도 내가 요청을 보냈을 때 동일한 응답이 오면 OK
- 관심X (추상화) -> 간섭X (캡슐화) -> 누구라도 상관X


## 4. 상속
- 객체의 공통점 -- 하나의 클래스로부터 받음 --> 당연히 상속 가능


---

왜 클래스가 타입일까?

- 개별 객체를 하나의 타입으로 보는 것(추상화)
- ex) 각각의 개별 존재 -> 하나의 클래스 (학생)  == 타입
<br/>

- 클래스 정의
``` python
class 클래스이름:
  속성, 행위
```
- 인스턴스 생성
<br/>

- 메서드 호출

<br/><br/>

- == 동등 (값이 같은지)
- is 동일 (id값이 같은지)

## 인스턴스 변수

## 클래스 변수
- 모든 인스턴스가 공유하는 값

---

### 인스턴스와 클래스 간의 이름 공간
= 함수의 scope
- 인스턴스 만들었을 때, 
  - 인스턴스 변수가 있으면 그대로 사용
  - 없으면 클래스 변수 호출

---

# OPP 메서드
- 괄호 존재

## 1. 인스턴스 메서드
1. self 
- 인스턴스 메서드에서 무조건 첫번째 인자!! (인스턴스 자기자신)

2. 생성자 메서드 (__init__)
- 괄호 안에 argument를 넣어주면 두번째 parameter로 들어감 (첫번째는 무조건 self)

3. 매직 메서드
``` python
class Person:
  def __init__(self, name):
    self.name = name

person1 = Person('김성준')
# person1은 객체이자, Person의 인스턴스
# '김성준'은 name으로 들어감

print(person1)  # <__main__.Person object at 0x000001A61DDC5DF0>
```

``` python
# 이름을 보이게 하고 싶음 --> 매직 메서드 사용
class Person:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

person1 = Person('김성준') 

print(person1)  # 김성준
```

``` python
class Person:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def __add__(self, other):
    return self.name + other.name

person1 = Person('김성준')
person2 = Person('박승재')

print(person1 + person2)  # 김성준박승재
```

4. 소멸자 메서드

``` python
class Person:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def __del__(self):
    print("삭제되었습니다")


person1 = Person('김성준')
del person1
print(person1.name)

# 오류 name 'person1' is not defined
```

``` python
class Person:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return self.name

  def __del__(self):
    print("삭제되었습니다")

person1 = Person('김성준')
person2 = person1
print(id(person), id(person2))  # 아이디 같음
del person1
print(person2.name)
# 김성준
# 삭제되었습니다

# 1. 오류메시지가 안 뜨는 이유?

# 2. print가 "삭제되었습니다"보다 먼저 나오는 이유?
## del 키워드는 객체를 지우는 게 아니라, 변수가 객체를 가르키는 참조값을 없앰 (포스트잇을 뗀다)


# 즉, 
# 같은 객체에 person1, person2 포스트잇이 붙어있음
# del person1 -- person1 포스트잇이 떼어짐
# print() -- (객체가 가르키는) 변수 출력
```



## 2. 클래스 메서드
- @classmethod 데코레이터 반드시 사용!!
- 첫번째 인자 == cls

- 클래스 내 속성을 활용할 때
- 클래스는 인스턴스 변수 사용 불가 (인스턴스 - 가능 O but 조회만)

- 왠만하면 인스턴스 메서드, 클래스 메서드를 써야할 때만..!

- 속성을 다루지 않고 단지 기능만 다룰 때



## 3. 스태틱 메서드
- 항상 고정된 값이 들어갈 때 (self, cls 필요 없을 때)


``` python
class Person:

  def __init__(self, name):
    self.name = name

  def call_name(self):  # 무조건 self 를 가지고 있어야만 출력 가능
    return f'대전 2반 {self.name} 입니다!'

  @staticmethod
  def hello(): # self를 굳이 가지고 있을 필요 없을 때 
    return '안녕하세요!'

person1 = Person('김성준')
print(person1.call_name())  # 대전 2반 김성준 입니다!
print(person1.hello())
```


<br/><br/>

---

### 메서드 오버라이딩
- 상속받은 메서드를 재정의
- 특정 기능만 바꿀 떄 

<br/><br/>

----

### 캡슐화
- Public Member
  - 어디에서나 호출 가능
  - 가장 일반적

- Protected Member
  - 언더바 1개
  - 느슨하게 제한 (권장사항) - 문법적으로 O , 암묵적으로 X

- Private Member
  - 언더바 2개
  - 강하게 제한
  - 자기자신 안에서만 실행 O
  - 바뀐 이름으로 접근 가능 But 암묵적으로 X


### getter (조회)

``` python
class Person:
  counts = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_age(self):
    return self.__age

person1 = Person('김성준', 25)
print(person1.get_age())  # 25
# 호출로 인한 응답을 출력
```


### setter (변경)
- set해달라고 물어보기~^^


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

person1 = Person('김성준', 25)
print(person1.get_age())  # 25

person1.set_age(30)
print(person1.get_age())  # 30
```

> 객체에 요청 메시지를 보내면, 요청에 맞는 함수를 찾아 응답을 줌

``` python
person1.age = 40  # 이렇게 하면 얼마나 편할까 
```

편하게 쓰면서 getter와 setter의 기능을 사용하기 위해 ==> property객체

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

> class Person:
>
>  def __init__(self, age): <br/>
>    self.age = age
>
>  @property  
>  def **age**(self): <br/>
>    return self._age
>
>  @**age**.setter <br/>
>  def **age**(self, new_age): <br/>
>   if new_age <= 19: <br/>
>      raise ValueError('Too Young For SSAFY') <br/>
>      return
>    
>    self._age = new_age

**굵은 글씨**는 모두 같아야 함