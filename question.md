# 질문 & 답변
[1. 문자열 대소 비교](#1-문자열-대소-비교)

[2. 연산자 우선순위](#2-연산자-우선순위)

[3. 인스턴스 메서드 호출](#3-인스턴스-메서드-호출)

[4. 클래스 메서드 호출](#4-클래스-메서드-호출)

[5. Mutable vs. Immutable](#5-mutable-vs-immutable)


<br/><br/>

---

<br/><br/>

## 1. 문자열 대소 비교
`'0' <= user_data['id'][-1] <= '9'`
- 문자열은 아스키 코드 기반해서 비교 가능
- 즉, 문자열 형태의 숫자도 아스키 코드에 근거하여 대소 비교 가능

<br/><br/>

## 2. 연산자 우선순위


0. `()`을 통한 grouping

1. Slicing

2. Indexing

3. 제곱연산자
    `**`

4. 단항연산자 
    `+`, `-` (음수/양수 부호)

5. 산술연산자
    `*`, `/`, `%`
    
6. 산술연산자
    `+`, `-`
 
7. 비교연산자, `in`, `is`

8. `not`

9. `and` 

10. `or`

<br/><br/>

## 3. 인스턴스 메서드 호출
``` python
class Circle:
    pi = 3.14

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return Circle.pi * self.r * self.r

    def circumference(self):
        return 2 * Circle.pi * self.r

    def center(self):
        return (self.x, self.y)
```

``` python
circle = Circle(3, 2, 4)
print(circle.area, circle.circumference)  # <bound method Circle.area of <__main__.Circle object at 0x000002302B6C6D60>> <bound method Circle.circumference of <__main__.Circle object at 0x000002302B6C6D60>>

# 괄호 생략 시 인스턴스 메서드의 덤프값 출력
```

``` python
circle = Circle(3, 2, 4)
print(circle.area(), circle.circumference())  # 28.259999999999998 18.84

# 괄호 안에 self가 생략되어 있음
```

<br/><br/>

## 4. 클래스 메서드 호출
``` python
class Person:

  @classmethod
  def details(cls, name, age):
    cls.name = name
    cls.age = age

  def check_age(cls):
    if cls.age > 19:
      return True
    else:
      return False
```

### 정상 작동
``` python
man = Person()
Person.details("이름", 103)
print(man.check_age())
```

### 오류나는 코드
``` python
man = Person("이름", 102)
print(man.check_age())
```

<br/><br/>

## 5. Mutable vs. Immutable
``` python
a = [1, 2, 3]
b = [4, 5, 6]
c = a.extend(b)
print(c)  # None
print(a)  # [1, 2, 3, 4, 5, 6]


d = 'abc'
e = d.replace('a', 'z')
print(e)  # zbc

# 이유는?
# a는 mutable이기 때문에 b를 넣어주고 굳이 다른 객체를 반환할 필요 X -> c에 들어갈게 없음
# 문자열은 immutable -- 다른 객체 반환
```