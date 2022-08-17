def fibo(n):
    if memo[n] == -1:  # 계산된 적이 없으면
        memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]


memo = [-1] * 101
memo[0] = 0
memo[1] = 1

for i in range(101):
    print(i, fibo(i))


# 속도가 훨씬 향상됨!!!!
