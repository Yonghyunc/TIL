# a = '123'

# b = list(a)
# # list : 클래스
# # b는 리스트 클래스로 만들어진 인스턴스 (== 리스트의 인스턴스)
# # 문자열 '123'이 리스트 생성자로 들어가서

# # 인스턴스 vs. 객체
# ## 인스턴스 : 특정한 클래스의 객체
# ## 객체 : 객체 자체

# print(b)  # ['1', '2', '3']

# b.append(3)  # 요청
# print(b)


# class Person:
#     def __init__(self, name):
#         self.name = name


# person1 = Person('김성준')
# # person1은 객체이자, Person의 인스턴스
# # '김성준'은 name으로 들어감

# print(person1)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name


# person1 = Person('김성준')

# print(person1)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

#     def __add__(self, other):
#         return self.name + other.name


# person1 = Person('김성준')
# person2 = Person('박승재')

# print(person1 + person2)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

#     def __del__(self):
#         print("삭제되었습니다")


# person1 = Person('김성준')
# del person1
# print(person1.name)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

#     def __del__(self):
#         print("삭제되었습니다")


# person1 = Person('김성준')
# person2 = person1
# del person1
# print(person2.name)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def call_name(self):  # 무조건 self 를 가지고 있어야만 출력 가능
#         return f'대전 2반 {self.name} 입니다!'

#     @staticmethod
#     def hello():  # self를 굳이 가지고 있을 필요 없을 때
#         return '안녕하세요!'


# person1 = Person('김성준')
# print(person1.call_name())  # 대전 2반 김성준 입니다!
# print(person1.hello())


class Person:
    counts = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call_name(self):
        return f'대전 2반 {self.name} 입니다!'

    @staticmethod
    def hello():
        return '안녕하세요!'


class Student(Person):
    @staticmethod
    def call_name(name):
        # super().call_name()
        return f'대전 2반 {name} 입니다!'


person1 = Person("김성준", 25)
student1 = Student("박승재", 25)
print(student1.call_name("김진호"))

## 오버라이딩
# super로 안된 이유  -- staticmethod 에서는  super를 쓸 수가 없음 (cls, self를 받아오지 않기 때문에)
# 클래스 Person에 있는 call_name은 없어지지 않고, 살아있음
