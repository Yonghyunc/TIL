class Stack:
    def __init__(self, size):
        self.size = size  # 스택의 길이
        self.items = [None] * self.size  # 스택을 None으로 초기화
        self.top = -1  # 스택의 가장 윗 부분을 가리키는 인덱스(== 최신 데이터를 가리키는 인덱스)

    # 스택이 비었는지 판별하는 함수 (True or False)
    def is_empty(self):
        return self.top == -1
        # True일 경우 (=스택이 비었을 경우) self.top == -1 반환
        # self.top == -1 은 스택의 가장 윗 부분이 -1 이란 뜻이므로 스택이 비어있다는 뜻

    # 스택이 가득 찼는지 판별하는 함수 (True or False)
    def is_full(self):
        return self.top == self.size - 1

    # 스택에 새로운 데이터를 넣는 함수
    def push(self, item):
        if self.is_full():  # 만약 스택이 가득 찼다면
            print('스택이 가득 찼으므로 데이터를 넣을 수 없습니다.')
        else:
            self.top += 1  # 데이터를 새로 넣었으므로 top은 하나가 늘어야 함
            self.items[self.top] = item

    # 스택의 가장 윗 부분 데이터를 조회하는 함수
    def peek(self):
        if self.is_empty():
            print('스택이 비었으므로 데이터를 조회할 수 없습니다.')
        else:
            return self.items[self.top]

    # 스택에 가장 마지막으로 넣은 데이터를 제거하고 반환하는 함수(== 최신 데이터를 제거하고 반환)
    def pop(self):
        if self.is_empty():
            print('스택이 비었으므로 데이터를 뺄 수 없습니다.')
        else:
            value = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1  # 데이터가 제거되었으므로 top은 하나가 줄어야 함
            return value


my_stack = Stack(5)  # 스택 생성
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

"""
스택을 쓸 때마다 이렇게 구현해서 사용해야 한다면, 너무 번거롭다.
파이썬은 스택을 따로 구현할 필요 없이, 리스트 자료형을 스택처럼 사용할 수 있다.
아래를 참고하자.
"""

my_stack = []  # 스택 생성

# push
my_stack.append(1)
my_stack.append(2)

# pop
my_stack.pop()

# peek
print(my_stack[-1])

# is_empty
if not my_stack:
    print('스택이 비었습니다.')

# size와 is_full은 필요없다.
# 파이썬은 리스트의 크기를 자동으로 늘려주고 줄여주기 때문이다.
