def f1(i, k, t):
    global cnt
    cnt += 1
    if i == k:
        s = 0
        for j in range(10):
            if bit[j]:
                s += A[j]
        if s == t:
            for j in range(10):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        bit[i] = 0
        f1(i + 1, k, t)
        bit[i] = 1
        f1(i + 1, k, t)


def f2(i, k, t, s):
    global cnt
    cnt += 1
    if i == k:
        if t == s:
            for j in range(10):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    elif t <= s:
        return
    else:
        bit[i] = 0
        f2(i + 1, k, t, s)
        bit[i] = 1
        f2(i + 1, k, t, s + A[i])
    return


A = [i for i in range(1, 11)]
bit = [0] * 10
cnt = 0
f1(0, 10, 10)
# f2(0, 10, 10, 0)
print(cnt)
