from termios import FF1


def f1(i, N):
    if i == N:
        print(bit)
    else:
        bit[i] = 1  # A[i]가 부분집합에 포함
        f1(i + 1, N)


def f2(i, N):
    global answer
    if i == N:
        s = 0  # 부분 집합의 합
        for i in range(N):
            if bit[i]:
                s += A[i]
                print(A[i], end=' ')
        # print()
        if answer == 10:
            answer += 1  # 부분집합의 합이 10인 경우의 수
    else:
        bit[i] = 1  # A[i]가 부분집합에 포함
        f1(i + 1, N)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
answer = 0
f1(0, 10)
f2(0, 10)
print(answer)
