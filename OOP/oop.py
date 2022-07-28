# 프로그램 --> 확장성 고려


# 절차지향 프로그래밍 1 -- 호출 순서대로 진행

# 나
me_sea = [0] * 15
me_attacked = [False] * 15
me_index = 1

for j in range(3):
    me_sea[me_index + j - 1] = 1


# 컴퓨터
computer_sea = [0] * 15
computer_attacked = [False] * 15
computer_index = 1

for j in range(3):
    computer_sea[computer_index + j - 1] = 1


# 절차지향 프로그래밍 2


def set_ship(index, sea):
    for j in range(3):
        sea[index + j - 1] = 1


me_sea = [0] * 15
me_attacked = [False] * 15
me_index = 1
set_ship(me_index, me_sea)

computer_sea = [0] * 15
computer_attacked = [False] * 15
computer_index = 1
set_ship(computer_index, computer_sea)

## 문제점 -- 플레이어의 수에 따라 변수가 많이 늘어남 (= 확장 한계)


# 프로그램 : 기능 vs. 구조
## 기능 -> 절차지향
## 구조 -> 객체지향


# 객체지향 프로그래밍 -- 프로그램이 확장되며 필요해 짐


# 클래스 = 객체를 만드는 도구 (설계도)
class Player:
    def __init__(self):
        self.sea = [0] * 15
        self.attacked = [False] * 15

    def set_ship(self, index):
        for j in range(3):
            self.sea[index + j - 1] = 1


# 나
me = Player()  # me는 객체
me.set_ship(1)

# 컴퓨터
computer = Player()
computer.set_ship(1)

# 객체 -- 역할 / 책임 / 협력
