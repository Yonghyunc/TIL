def f(i, N):
    if i == N:  # 순열 완성
        print(P)
    else:
        for j in range(i, N):  # P[i]에 들어갈 숫자 P[j] 결정
            P[i], P[j] = P[j], P[i]
            f(i + 1, N)
            P[i], P[j] = P[j], P[i]


P = [1, 2, 3]
f(0, 3)
