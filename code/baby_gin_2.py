'''
5
123123
124467
333444
444456
123444
'''

# 탐욕 기법

t = int(input())
for tc in range(1, t + 1):
    card = int(input())
    c = [0] * 12

    i = 0
    while i < 6:
        c[card % 10] += 1
        card //= 10
        i += 1

    tri = 0
    run = 0
    i = 1
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            run += 1
            continue
        i += 1
    if run + tri == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
