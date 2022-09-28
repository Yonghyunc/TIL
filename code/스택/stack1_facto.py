def f(n):  # 팩토리얼 n! 1! = 1
    if n == 1:
        return 1
    else:
        return n * f(n - 1)


print(f(20))
