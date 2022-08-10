from itertools import count


def countion_sort(original, k):
    counter = [0] * (k + 1)

    # 1. counter에 original 원소의 빈도수 담기
    for i in original:
        counter[i] += 1

    # 2. 누적(counter 업데이트)
    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]

    # 3. result 생성
    result = [-1] * len(original)

    # 4. result에 정렬하기 (counter를 참조)
    # 거꾸로 가는 이유 : stable(입력한 순서대로 정렬이 됨)
    # 같은 숫자라도 완전히 같지는 않음 -- 정렬 시에도 순서를 지켜줘야 함
    for i in range(len(original) - 1, -1, -1):
        counter[original[i]] -= 1  # 하나씩 정렬하고 있으므로, 하나씩 뺌
        result[counter[original[i]]] = original[i]

    return result


'''

original = [0, 4, 1, 3, 1, 2, 4, 1]

counter = [1, 3, 1, 1, 2]  -- k만큼의 길이

-> 누적 counter = [1, 4, 5, 6, 8]

result = [0, 1, 1, 1, 2, 3, 4, 4]

'''
