sample = [55, 7, 78, 12, 42]
sample_list = [("철수", 55), ("영희", 7), ("민수", 78), ("기영", 12), ("유라", 42)]
# 복합적인 데이터를 정렬할 때 --> key option


def bubble_sort(a):  # 정렬할 List
    for i in range(len(a) - 1, 0, -1):  # 범위의 끝 위치 (역순으로 반복)
        for j in range(0, i):

            # key option
            # if a[j][1] > a[j + 1][1]:

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a


print(bubble_sort(sample))

'''
i     j
-----------
4   0,1,2,3
3   0,1,2,3
2   0,1,2,3
1   0,1,2,3
'''

'''

1 cycle : [7, 55, 12, 42, 78]
2 cycle : [7, 12, 42, 55, 78]
정렬 완료

'''
