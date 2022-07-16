T = int(input())

for test_case in range(1, T + 1):
    print("#", test_case)
    t = int(input())
    a = ''

    for x in range(1, t + 1):
        lst = list(map(str, input().split()))
        eng = str(lst[0])
        num = int(lst[1])
        res = eng * num
        a += res
    for y in range(0, len(a)+1,10):
        print(a[0:10])
        a = a[10:]