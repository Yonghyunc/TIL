# 이해를 위해 다시 한번 보면 좋겠다!!
'''
[ 문제 ]
개의 속성과 행위를 정의하는 Doggy 클래스를 만들어라

[ 구성요소 ]
1. 초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.
2. bark() 메서드를 호출하면 개는 짖을 수 있다.
3. 클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.
    개가 태어나면 num_of_dogs와 birth_of_dogs의 값이 각 1씩 증가한다.
    개가 죽으면 num_of_dogs의 값이 1 감소한다.
4. get_status() 메서드를 호출하면 birth_of_dogs와 num_of_dogs의 수를 출력할 수 있다.
'''


class Doggy:  # 클래스 메서드
    # 클래스 변수 정의
    num_of_dogs = 0
    birth_of_dogs = 0

    # __init__ : 생성자
    def __init__(self, name, breed):  # 인스턴스 메서드 (호출 시, 첫번째 인자를 self 전달)
        # 인스턴스 변수 정의
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    # __del__ : 소멸자
    def __del__(self):  # 인스턴스 메서드
        Doggy.num_of_dogs -= 1

    def bark(self):  # 인스턴스 메서드
        return '왈왈!'

    @classmethod  # 클래스 데코레이터
    def get_status(cls):  # 호출 시 첫번째 인자를 클래스 전달
        return f'Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}'
