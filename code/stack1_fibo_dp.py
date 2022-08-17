def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return


table = [0] * 101
fibo_dp(100)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {table[N]}')
