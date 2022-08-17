'''

재귀 기본형 => f(i, n)
i = 현재 단계
n = 목표

'''


def f(i, N):        # i 현재 단계, N 목표 단계
    if i == N:      # 목표에 도달
        print(i)
        return
    else:           # 다음 단계로
        print(i)
        f(i + 1, N)


f(0, 3)
